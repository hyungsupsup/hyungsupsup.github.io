---
title: "Multi-Head Attention"
date: 2026-11-17
tags: [technique, attention]
category: "Attention·시퀀스"
status: draft
---

> 쿼리·키·값을 서로 다른 여러 개의 학습된 선형 사영으로 나누어 병렬로 scaled dot-product attention을 수행하고 결과를 concat하는 attention 구성 방식.

**대표 논문**: Attention Is All You Need (2017) · **분류**: Attention·시퀀스

## 해결한 문제
기존 seq2seq의 단일 attention은 하나의 정렬(alignment) 분포만 만들어 '무엇에 주목하는가'를 한 가지 관점으로만 표현했다. 또한 RNN 기반 인코더-디코더는 순차 계산 때문에 시퀀스 길이에 대해 병렬화가 안 되고 장거리 의존성에서 gradient가 약해졌다. Multi-Head Attention은 attention 자체를 여러 부분공간(subspace)으로 분해해 표현력을 늘리면서, recurrence 없이도 토큰 간 임의 거리 상호작용을 한 번에 계산하도록 만들었다.

## 핵심 아이디어
각 head $i$는 학습된 사영 $W_i^Q, W_i^K, W_i^V$로 $Q,K,V$를 낮은 차원 $d_k = d_{model}/h$로 보내고, 독립적으로 $\mathrm{head}_i = \mathrm{softmax}(Q_iK_i^\top/\sqrt{d_k})V_i$를 계산한다. head들의 출력을 concat한 뒤 출력 사영 $W^O$로 다시 $d_{model}$ 차원으로 섞는다: $\mathrm{MultiHead}(Q,K,V)=\mathrm{Concat}(\mathrm{head}_1,\dots,\mathrm{head}_h)W^O$. 각 head가 서로 다른 관계(위치적 근접, 구문적 의존, 특정 토큰 추적 등)를 담당하도록 표현 공간을 나누는 것이 핵심이며, 총 연산량은 $d_{model}$ 차원의 단일 head attention과 비슷하게 유지된다. $\sqrt{d_k}$ 스케일링은 $d_k$가 커질 때 dot-product 분산이 커져 softmax가 포화되는 것을 막는다.

## 왜 작동하나
여러 head의 평균을 내는 대신 concat+사영으로 서로 다른 주의 패턴을 보존하면서 조합할 수 있어, 단일 softmax 분포가 갖는 '하나의 날카로운 선택' 제약을 완화한다. 각 head가 저차원 부분공간에서 계산하므로 파라미터 수와 FLOPs를 크게 늘리지 않고도 다양한 관계 가설을 병렬로 검증하는 앙상블처럼 동작한다. 또한 attention 행렬 계산이 토큰 축에 대해 완전 병렬화 가능해 GPU/TPU 활용률이 높다.

## 트레이드오프
- 시퀀스 길이 $N$에 대해 $O(N^2)$ 시간·메모리 — 고해상도 이미지 토큰이나 긴 로봇 에피소드에서 병목
- KV cache가 head 수 $h$에 비례해 커져 autoregressive 디코딩 및 실시간 로봇 제어에서 메모리·대역폭 부담
- 학습 후 상당수 head가 pruning 가능할 만큼 중복(redundant)하다는 보고 — head 수가 곧 표현력은 아님
- locality·translation equivariance 같은 귀납적 편향이 없어 위치 인코딩에 의존
- head별 역할이 해석 가능하다는 보장이 약해 디버깅·안전성 분석이 어려움

## 계보
**이전**
- Additive (Bahdanau) Attention
- Dot-Product Attention (Luong)
- Single-Head Seq2Seq Attention
- ConvS2S

**이후**
- Multi-Query Attention (MQA)
- [[techniques/grouped-query-attention|Grouped-Query Attention (GQA)]]
- Multi-head Latent Attention (MLA)
- [[techniques/flash-attention|FlashAttention]]
- Linear Attention / Performer
- Cross-Attention (encoder-decoder 변형)
- Head pruning / attention head analysis

## 피지컬 AI에서의 쓰임
- RT-1, RT-2 — Transformer 정책 백본에서 이미지 토큰과 언어 instruction 토큰 간 cross-attention
- OpenVLA — Llama 2 백본(GQA 사용)의 attention으로 vision patch + language + action token 결합
- Octo — transformer policy 블록에서 observation history와 task 토큰을 attention으로 융합
- Diffusion Policy — 관측 시퀀스를 cross-attention key/value로 두고 action denoising step이 query
- ACT / ALOHA — action chunk 예측 transformer의 attention
- VIMA — multimodal prompt token에 대한 cross-attention으로 로봇 조작
- π0 (PaliGemma 기반 VLA) — vision-language prefix에 action expert가 attention
- HPT (Heterogeneous Pre-trained Transformers) — 이종 로봇 embodiment 토큰을 attention으로 정렬

## 💡 아이디어 훅
- vision / language / proprioception / tactile 토큰별로 head를 명시적으로 분리 배정하면(mixture-of-heads) modality 충돌이 줄어드는가?
- head별 KV cache를 공유·압축해 제어 주기(예: 50–100Hz) 실시간 VLA 추론 latency를 줄이는 설계
- tactile·force 토큰에 반응하는 head를 찾아 접촉 이벤트 검출기로 재활용(attention head probing for contact)
- 서로 다른 시간 스케일(단기 반사 / 장기 계획)을 담당하는 head를 계층적으로 배치한 temporal multi-head attention
- head별 attention entropy를 불확실성 신호로 사용해 로봇 정책의 OOD·실패 사전 감지
- 월드모델에서 head를 latent dynamics factor(물체 수, 물리량)별로 분해하는 factorized multi-head attention
- embodiment별 head pruning / head-wise LoRA로 로봇 간 전이학습 비용 절감

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
