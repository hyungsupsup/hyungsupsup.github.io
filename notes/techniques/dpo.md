---
title: "DPO"
date: 2026-11-21
tags: [technique, training]
category: "학습 기법"
status: draft
---

> DPO는 사람 선호 쌍을 보고 보상 모델 없이 바로 '더 좋은 답' 쪽으로 확률을 조정하는 학습법이다.

**대표 논문**: Direct Preference Optimization: Your Language Model is Secretly a Reward Model (2023) · **분류**: 학습 기법

## 해결한 문제
RLHF(Reinforcement Learning from Human Feedback, 사람 선호로 강화학습하는 방식)는 보상 모델, 정책 모델, 참조 모델 등을 따로 쓰고 PPO(Proximal Policy Optimization, 강화학습 정책 최적화 기법)로 학습해야 해서 복잡하고 불안정했다. 사람 선호를 학습하려면 먼저 보상 함수를 만들고 그 보상을 최대화하는 강화학습을 여러 단계로 진행해야 했다. 이 과정은 계산량이 크고 하이퍼파라미터에 민감하며, 보상 모델이 잘못되면 정책도 쉽게 망가졌다.

## 핵심 아이디어
비유하자면, 두 답 중 더 나은 답을 골라주는 평가자가 있을 때 보상 점수를 따로 매기지 않고 바로 '이 답을 더 자주, 저 답을 덜 자주' 하도록 모델을 살짝 밀어주는 것이다. 먼저 같은 질문에 대해 chosen(더 좋은 답)과 rejected(더 나쁜 답) 쌍을 모은다. DPO는 현재 모델과 reference model(원래 모델)이 각 답에 부여하는 log probability(로그 확률) 차이를 계산한다. 이 차이가 reference model 대비 chosen 쪽으로 커지고 rejected 쪽으로 작아지도록 손실 함수를 최소화한다.

## 왜 작동하나
RLHF의 보상 최대화 + KL 페널티(원래 모델에서 너무 멀어지지 않게 하는 제약) 문제를 풀면, 보상 함수를 정책의 로그 확률 차이로 바꿀 수 있다. 그래서 보상 모델과 PPO 루프를 따로 돌리지 않고, 선호 쌍만 있으면 지도학습처럼 안정적으로 학습할 수 있다. 결과적으로 계산과 메모리가 줄고, 보상 모델의 오차가 직접 전파되는 위험도 작아진다.

## 트레이드오프
- 선호 데이터가 편향되거나 noisy하면 모델이 잘못된 '좋아하는 스타일'을 배울 수 있다.
- chosen과 rejected가 너무 비슷하거나 너무 극단적이면 학습 신호가 약하거나 모델이 한쪽으로 치우칠 수 있다.
- reference model과 KL 강도, 학습률 같은 하이퍼파라미터에 따라 성능이 크게 달라질 수 있다.

## 계보
**이전**
- [[techniques/rlhf|RLHF]]
- Reward model + PPO
- Bradley-Terry preference model
- KL-constrained policy optimization

**이후**
- IPO
- KTO
- SimPO
- ORPO
- GRPO

## 피지컬 AI에서의 쓰임
- 로봇 VLA(Vision-Language-Action, 시각·언어·행동을 함께 다루는 로봇 모델)가 같은 상황에서 '더 안전한 동작'과 '위험한 동작' 쌍을 보고, 보상 모델 없이 선호에 맞게 행동을 조정하는 데 쓸 수 있다.
- 시뮬레이션에서 성공한 궤적과 실패한 궤적 쌍으로 로봇 정책의 확률을 조정해, 실제 로봇이 더 자주 성공하는 행동을 선택하게 할 수 있다.
- diffusion(노이즈에서 이미지를 생성하는 모델)이나 world model(로봇이 환경을 예측하는 내부 모델)에서 더 좋은 결과와 나쁜 결과 쌍으로 안전성이나 스타일을 미세조정할 때 DPO 아이디어를 쓸 수 있다.

## 💡 아이디어 훅
- DPO를 로봇 안전 규칙 위반/준수 쌍으로 적용하면 보상 모델 없이도 안전성을 높일 수 있을까?
- 선호 쌍이 아니라 '절대 점수'만 있을 때 DPO처럼 간단하게 쓰는 변형은 무엇이 있을까?
- diffusion이나 world model처럼 확률을 계산하기 어려운 모델에는 DPO의 로그 확률 차이를 어떻게 바꿀 수 있을까?

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
