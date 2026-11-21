---
title: "Diffusion Policy"
date: 2026-11-22
tags: [technique, robotics]
category: "로봇 특화"
status: draft
---

> 로봇의 다음 동작을 한 번에 정답처럼 맞추는 대신, 잡음에서 그림을 그려내듯 여러 단계로 다듬어 만드는 정책 학습법

**대표 논문**: Diffusion Policy: Visuomotor Policy Learning via Action Diffusion (2023) · **분류**: 로봇 특화

## 해결한 문제
기존 행동 복제 정책은 여러 개의 정답이 있는 상황에서 평균적인 동작을 내거나, 복잡한 동작 분포를 잘 표현하지 못해 실수하기 쉬웠다. 특히 카메라 입력에서 로봇 팔 동작을 바로 예측하면 작은 오차가 누적되고, 같은 상황에서도 사람마다 다른 동작이 가능할 때 한 가지 답만 강요하는 문제가 있었다.

## 핵심 아이디어
비유하자면, 처음에는 무작위 소음 덩어리인 동작을 보고 '이 소음을 조금씩 걷어내면 사람이 시연한 좋은 동작이 된다'고 학습하는 것이다. 먼저 로봇 시연 데이터에서 관측과 동작 시퀀스를 준비하고, 모델에게 관측 조건으로 노이즈를 제거하는 방법을 학습시킨다. 추론 시에는 랜덤 노이즈에서 시작해 몇 단계에 걸쳐 동작 시퀀스를 다듬고, 그중 앞부분 동작을 실제로 실행한다.

## 왜 작동하나
Diffusion은 하나의 정답을 맞추는 회귀가 아니라 '가능한 동작들의 분포'를 점진적으로 만들어 내므로, 여러 모드의 동작을 평균으로 뭉개지 않고 표현하기 쉽다. 또한 동작을 한 번에 하나씩만 예측하지 않고 짧은 시퀀스로 함께 생성하면 시간적으로 매끄럽고, 노이즈 제거 학습이 비교적 안정적이다.

## 트레이드오프
- 추론 시 노이즈 제거 단계를 여러 번 반복해야 해서 단순 MLP나 Transformer보다 느릴 수 있다.
- 동작 시퀀스를 미리 생성하면 환경 변화에 즉각 반응하기 어렵고, 자주 다시 계획해야 할 수 있다.
- 데이터 품질과 하이퍼파라미터 튜닝에 민감하며, 간단한 작업에는 과한 계산이 필요할 수 있다.

## 계보
**이전**
- [[techniques/behavior-cloning|Behavior Cloning]]
- Gaussian Mixture Model policy
- Conditional Variational Autoencoder policy
- Energy-Based Model policy
- Diffusion Models (DDPM)

**이후**
- 3D Diffusion Policy
- Diffusion Policy Policy Optimization (DPPO)
- Consistency Policy
- Flow Matching Policy
- Diffusion Transformer policy

## 피지컬 AI에서의 쓰임
- 로봇 팔이 물건을 집거나 삽입하는 작업에서 여러 성공 동작을 학습할 때, 카메라 입력을 보고 동작 시퀀스를 생성하는 데 쓰인다.
- VLA(비전-언어-행동) 모델에서 언어 지시를 조건으로 삼고, Diffusion Policy를 action head로 붙여 로봇 동작을 만드는 데 쓰인다.
- 사람 시연 데이터를 모방할 때, 같은 상황에서도 다양한 동작을 자연스럽게 재현해야 하는 조작·정리·조립 작업에 쓸 수 있다.

## 💡 아이디어 훅
- Diffusion Policy의 노이즈 제거 단계를 줄여도 성능을 유지하려면 어떤 기법을 쓸 수 있을까?
- 로봇이 실패할 것 같은 동작은 노이즈 제거 과정에서 어떻게 걸러낼 수 있을까?
- 언어 조건, 3D 관측, 물리 시뮬레이터 피드백을 Diffusion Policy에 어떻게 함께 넣으면 더 안전한 로봇 정책이 될까?

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
