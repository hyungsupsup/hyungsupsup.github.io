---
title: "Flash Attention"
date: 2026-11-17
tags: [technique, attention]
category: "Attention·시퀀스"
status: draft
---

> Attention 연산을 HBM에 N×N 행렬로 materialize하지 않고, SRAM 단위 tiling + online softmax + backward recomputation으로 IO를 줄여 exact attention을 빠르고 메모리 효율적으로 계산하는 IO-aware kernel 기법.

**대표 논문**: FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness (2022) · **분류**: Attention·시퀀스

## 해결한 문제
기존 attention은 $QK^\top$로 만든 $N\times N$ score 행렬과 softmax 확률을 매번 HBM에 쓰고 다시 읽어야 해서, 연산량은 적은데 메모리 대역폭에 병목이 걸리는 memory-bound 연산이었다. 시퀀스 길이가 길어지면 메모리가 $O(N^2)$으로 폭발해 학습·추론 배치를 키울 수 없었고, sparse/low-rank 근사들은 속도는 얻어도 exact attention을 포기해야 했다.

## 핵심 아이디어
Attention을 $Q,K,V$의 block 단위로 쪼개 SRAM에 올려 부분 계산하고, softmax를 block-wise로 누적하는 online softmax로 전체 행렬 없이도 정확한 결과를 얻는다. 각 block $j$마다 running max $m$, running sum $l$, running output $O$를 갱신한다: $m^{new}=\max(m, \tilde m)$, $l^{new}=e^{m-m^{new}}l + e^{\tilde m-m^{new}}\tilde l$, $O^{new}=\text{diag}(l^{new})^{-1}\big(e^{m-m^{new}}l\,O + e^{\tilde m-m^{new}}\tilde P V_j\big)$. Backward에서는 $N\times N$ attention 확률을 저장하지 않고 forward를 재계산(recomputation)해 $O(N)$ 메모리만 쓴다. 커널 fusion으로 softmax·masking·dropout·matmul을 하나의 CUDA kernel에 묶어 HBM round-trip을 없앤다. 결과적으로 FLOPs는 $O(N^2d)$ 그대로지만 HBM 접근 횟수가 줄어 wall-clock이 크게 단축된다.

## 왜 작동하나
Attention은 arithmetic intensity가 낮아 GPU의 tensor core를 놀게 만드는 전형적 memory-bound 연산이고, 병목이 FLOPs가 아니라 HBM↔SRAM 데이터 이동에 있다. FlashAttention은 타일을 SRAM에 유지한 채 여러 번 재사용하므로 HBM 트래픽을 block 크기만큼 줄이고, online softmax 덕분에 근사 없이도 수치적으로 동일한 결과를 낸다. 즉 '연산을 줄인' 것이 아니라 '데이터를 덜 움직인' 최적화라서 정확도 손실이 없다.

## 트레이드오프
- 점근적 연산량은 그대로 $O(N^2d)$ — 초장문 시퀀스에서는 여전히 quadratic 병목
- backward에서 recomputation을 하므로 FLOPs가 늘어나고, 구현이 복잡해 커널 버그·수치 불안정(fp16/bf16 누적) 위험이 있음
- head dimension·block size·shared memory 제약에 따라 성능이 크게 달라지고, 특수 mask/bias/ALiBi 등을 fuse하려면 커널을 다시 짜야 함
- 시퀀스가 짧거나 배치가 작으면 launch overhead 때문에 이득이 미미
- autoregressive decode 단계(KV cache, batch=1)에서는 병목이 바뀌어 별도 최적화(FlashDecoding, PagedAttention)가 필요
- CUDA/Triton 커널에 대한 하드웨어 의존성이 커서 NPU·모바일 이식성이 떨어짐

## 계보
**이전**
- vanilla scaled dot-product attention
- memory-efficient attention (xFormers)
- gradient checkpointing / activation recomputation
- [[techniques/sparse-attention|sparse attention (Longformer, BigBird)]]
- low-rank attention (Linformer)
- kernel-based attention (Performer)

**이후**
- FlashAttention-2
- FlashAttention-3
- FlashDecoding
- PagedAttention (vLLM)
- Ring Attention
- Striped Attention
- FlexAttention
- FP8 FlashAttention

## 피지컬 AI에서의 쓰임
- VLA 모델(OpenVLA, RT-2 계열, π0 등)의 vision-language backbone 및 action expert attention 구현체
- Diffusion/Flow-matching policy의 transformer block (DiT 계열 action head)
- 비디오 월드모델·video diffusion transformer의 spatiotemporal attention
- 다중 카메라·다중 로봇 토큰을 하나의 긴 시퀀스로 묶는 cross-embodiment 학습
- on-robot 실시간 추론 latency 확보를 위한 fused attention kernel (Jetson 등 edge GPU)

## 💡 아이디어 훅
- VLA의 action chunking 토큰과 관측 토큰을 분리해, action 토큰만 sliding-window attention으로 처리하는 IO-aware 커널 설계
- KV cache가 지배적인 실시간 로봇 제어 루프에서 decode-phase 병목을 겨냥한 FlashDecoding/PagedAttention 변형과 제어 주기(Hz) 보장 연구
- 월드모델의 long-horizon rollout을 위한 Ring/Striped Attention + 로봇 도메인 causal mask fuse
- 3D point cloud / multi-view 토큰처럼 이질적 길이 분포를 갖는 입력에 대한 block-sparse FlashAttention 자동 튜닝
- attention sink·sliding window와 FlashAttention을 결합해 로봇 에피소드 단위 streaming memory를 구현
- quantization(FP8/INT8)과 FlashAttention을 함께 쓸 때 VLA 정책 성능 저하를 정량화하는 벤치마크
- on-device NPU용 tiling 전략 재탐색 — SRAM 계층이 다른 하드웨어에서 online softmax의 이득이 유지되는가

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
