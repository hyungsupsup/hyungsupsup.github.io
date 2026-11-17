---
title: "Grouped-Query Attention"
date: 2026-11-18
tags: [technique, attention]
category: "Attention·시퀀스"
status: draft
---

> Multi-Head Attention과 Multi-Query Attention 사이에서 query head들을 G개 그룹으로 묶어 KV head를 공유하게 함으로써 KV cache 크기와 디코딩 시 메모리 대역폭을 줄이는 attention 변형.

**대표 논문**: GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints (2023) · **분류**: Attention·시퀀스

## 해결한 문제
MHA는 head마다 별도 K/V를 두어 추론 시 KV cache가 커지고, autoregressive 디코딩이 메모리 대역폭 병목에 걸린다. MQA는 KV head를 1개로 줄여 cache를 크게 줄이지만 품질 저하와 학습 불안정이 보고되었다. GQA는 MHA와 MQA 사이의 연속적인 절충점을 제공해 품질 손실을 거의 없애면서 cache를 줄이려 한다.

## 핵심 아이디어
query head 수 $H$, KV head 수 $G$ ($1 \le G \le H$)로 두고, 각 KV head를 $H/G$개의 query head가 공유한다. $G=H$면 MHA, $G=1$이면 MQA가 되는 일반화다. KV cache 크기는 $G/H$로 줄고, 디코딩 시 토큰당 읽어야 하는 K/V 바이트 수도 같은 비율로 감소한다. 기존 MHA checkpoint에서 KV head들을 mean-pooling해 초기화한 뒤, 원 pretraining 연산의 일부(약 5%, 확인 필요)만 uptraining하면 GQA 모델을 얻을 수 있다.

## 왜 작동하나
LLM 디코딩은 연산량보다 KV cache를 매 step 다시 읽는 메모리 대역폭에 의해 지배되므로, KV head 수를 줄이는 것이 지연시간에 직접 효율적이다. 동시에 query head는 그대로 유지되어 표현 다양성과 attention 패턴의 세밀도가 보존되므로, KV까지 1개로 뭉개는 MQA보다 품질 손실이 작다.

## 트레이드오프
- 동일 규모에서 MHA 대비 약간의 품질 저하가 남는다(특히 작은 모델).
- 그룹 수 $G$가 새로운 하이퍼파라미터가 되어 모델별 튜닝이 필요하다.
- prefill 단계의 attention 연산 FLOPs는 크게 줄지 않는다(주 이득은 디코딩 메모리).
- KV cache가 시퀀스 길이에 선형으로 증가하는 문제 자체는 해결하지 못한다.
- uptraining이 필요해 기존 checkpoint를 그대로 쓰려면 추가 학습 비용이 든다.

## 계보
**이전**
- [[techniques/multi-head-attention|Multi-Head Attention (MHA)]]
- Multi-Query Attention (MQA)
- Multi-Head Latent Attention 이전의 KV 공유 계열 기법

**이후**
- Multi-Head Latent Attention (MLA)
- Cross-layer KV sharing 계열 (예: YOCO)
- KV cache quantization/eviction과 결합된 GQA 변형
- Llama 2 70B·Llama 3·Mistral 등 GQA 채택 모델군

## 피지컬 AI에서의 쓰임
- Llama-2/3 백본을 쓰는 VLA(예: OpenVLA 계열)에서 실시간 closed-loop 제어 시 디코딩 지연 감소
- π0/PaliGemma 계열 VLA 백본의 KV cache 메모리 절감으로 on-robot 추론 여유 확보
- autoregressive video/latent 월드모델에서 긴 rollout 시 KV cache 폭증 억제
- 다중 카메라·다중 센서 토큰 스트림을 하나의 컨텍스트로 넣는 정책에서 메모리 예산 관리

## 💡 아이디어 훅
- closed-loop 제어에서 연속 제어 step 간 관측이 겹치는 점을 이용해 GQA KV cache를 재사용/부분 갱신하는 cache-carry 정책 설계
- 카메라별·모달리티별로 KV 그룹을 할당하는 modality-aware grouping이 GQA의 균일 그룹보다 유리한가
- action chunking/flow-matching head와 GQA 백본의 상호작용: KV 압축이 action 정밀도에 주는 영향 측정
- GQA + cross-layer KV sharing을 결합해 on-device 로봇 추론 메모리 한계에 맞춘 초경량 VLA
- 월드모델의 diffusion transformer에는 KV cache 이득이 작다는 점을 역이용해, autoregressive 월드모델과 non-autoregressive 월드모델의 latency-품질 tradeoff 비교
- 레이어별로 그룹 수 $G$를 다르게 주는 adaptive GQA가 로봇 long-horizon 태스크에서 효과적인가

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
