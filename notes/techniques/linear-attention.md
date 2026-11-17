---
title: "Linear Attention"
date: 2026-11-17
tags: [technique, attention]
category: "Attention·시퀀스"
status: draft
---

> softmax attention의 $\exp(q^\top k)$ 유사도를 커널 특징맵 $\phi(q)^\top\phi(k)$로 분해해, attention을 $O(N^2)$에서 $O(N)$(또는 상수 메모리 recurrent state)으로 바꾸는 기법.

**대표 논문**: Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention (2020) · **분류**: Attention·시퀀스

## 해결한 문제
표준 softmax attention은 시퀀스 길이 $N$에 대해 $N\times N$ attention matrix를 명시적으로 만들어 시간·메모리가 $O(N^2)$이므로, 긴 문맥(다중 카메라 프레임, 긴 로봇 에피소드, 고주파 제어 로그)에서 병목이 된다. 또한 autoregressive 생성 시 매 스텝 KV cache 전체를 다시 훑어야 해 추론 지연이 선형 이상으로 커진다. Linear Attention은 attention을 커널화해 행렬 곱 순서를 바꿈으로써 이 이차 비용을 제거한다.

## 핵심 아이디어
유사도를 $\mathrm{sim}(q,k)=\phi(q)^\top\phi(k)$ (예: $\phi(x)=\mathrm{elu}(x)+1$)로 두면, 출력은 $o_i=\frac{\sum_j \phi(q_i)^\top\phi(k_j)\,v_j}{\sum_j \phi(q_i)^\top\phi(k_j)}=\frac{\phi(q_i)^\top \sum_j \phi(k_j)v_j^\top}{\phi(q_i)^\top\sum_j \phi(k_j)}$가 되어 키-값 쌍을 먼저 합산할 수 있다. 즉 $S_t = S_{t-1} + \phi(k_t)v_t^\top$, $z_t = z_{t-1}+\phi(k_t)$인 고정 크기 상태를 유지하는 RNN으로 재해석되며, 학습 시에는 cumulative sum(associative scan)으로, 추론 시에는 상수 메모리·상수 시간 갱신으로 계산된다. causal 마스킹도 prefix sum만으로 정확히 구현된다.

## 왜 작동하나
softmax의 지수 유사도는 '모든 키를 봐야' 정규화가 되지만, 커널 분해를 쓰면 키-값 정보를 하나의 요약 행렬 $S$에 미리 접어넣을 수 있어 쿼리당 비용이 $O(1)$이 된다. 정보 병목이 생기는 대신, 상태가 고정 크기이므로 시퀀스가 길어져도 비용이 늘지 않고 스트리밍/실시간 갱신에 자연스럽다.

## 트레이드오프
- softmax의 sharp한 선택성(거의 one-hot에 가까운 attention)을 잃어 성능이 softmax attention보다 낮아지는 경향
- 특징맵 $\phi$의 차원 $d_\phi$에 비례하는 상태 메모리($d_\phi \times d_v$)와 근사 오차
- naive 구현은 GPU에서 비효율적 — chunkwise/associative-scan 커널 없이는 wall-clock 이득이 작음
- 긴 문맥에서 'attention dilution'(오래된 정보가 희석됨) 문제, forgetting/decay 설계가 필요
- 비선형 특징맵 선택이 성능을 크게 좌우하며 튜닝이 어렵다

## 계보
**이전**
- Softmax Attention (Scaled Dot-Product Attention)
- Kernel methods / Nadaraya-Watson 비모수 회귀
- Fast Weight Programmers
- Gated RNN (LSTM/GRU)

**이후**
- Performer (FAVOR+ random features)
- cosFormer
- FLASH (gated linear attention, chunkwise parallel)
- RetNet (retentive network, decay 기반)
- GLA (Gated Linear Attention)
- DeltaNet / Delta Rule linear attention
- [[techniques/rwkv|RWKV]]
- EfficientViT (vision용 lightweight linear attention)
- Mamba/S4 계열 SSM (선형 시간 시퀀스 모델 계보)

## 피지컬 AI에서의 쓰임
- 다중 카메라·다중 히스토리 프레임을 입력으로 받는 VLA 정책의 긴 시퀀스 토큰 처리 (구체 모델명 확인 필요)
- 고주파(수백 Hz) 로봇 제어 루프에서 상수 시간 추론이 필요한 on-robot policy backbone
- EfficientViT 계열 경량 백본을 쓰는 실시간 조작/내비게이션 정책
- 월드모델의 긴 latent rollout에서 attention 비용 절감
- 스트리밍 센서(IMU·관절 로그) 처리용 recurrent state 형태의 정책 메모리

## 💡 아이디어 훅
- 선형 attention의 recurrent state $S_t$를 로봇의 episodic memory로 명시적으로 활용 — 태스크 재개/실패 복구에 쓰는 연구
- DeltaNet식 delta rule을 VLA에 넣어 in-context 적응(새 물체·새 도구에 즉시 적응)을 attention 상태로 수행
- chunkwise linear attention + action chunking을 결합해 diffusion policy의 denoising 스텝 비용을 줄이는 조합
- 선형 attention 상태에 decay/gating을 로봇 시간 스케일(제어 주기 vs 계획 주기)에 맞춰 이중화하는 설계
- 월드모델에서 선형 attention 상태를 latent dynamics의 충분통계량으로 보고, 상태 자체를 예측 대상으로 학습
- 선형 attention의 근사 오차가 조작 성공률에 미치는 영향에 대한 체계적 ablation (아직 부족)

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
