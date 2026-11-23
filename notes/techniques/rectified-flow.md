---
title: "Rectified Flow"
date: 2026-11-24
tags: [technique, generative]
category: "생성모델"
status: draft
---

> Rectified Flow는 노이즈에서 이미지를 만드는 구불구불한 경로를 여러 번 고쳐 거의 직선으로 만들어, 몇 걸음 만에 결과물을 뽑을 수 있게 해주는 생성 모델이다.

**대표 논문**: Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow (2022) · **분류**: 생성모델

## 해결한 문제
기존 diffusion/flow 모델은 노이즈에서 데이터로 가는 경로가 휘어서 샘플링할 때 수십~수백 스텝을 계산해야 했다. 그래서 이미지 생성이나 로봇 제어처럼 빠른 응답이 필요한 곳에서 느리고, 다른 데이터 도메인 간 변환도 불안정했다.

## 핵심 아이디어
비유: 산길을 여러 번 다듬어 직선 고속도로로 바꾸는 것과 같다. 먼저 노이즈에서 데이터로 이동하는 velocity field(각 위치에서 어디로 얼마나 움직일지 알려주는 벡터)를 학습한다. 그다음 이 velocity field로 만든 노이즈-데이터 쌍을 다시 연결하도록 새 velocity field를 학습하는 reflow를 반복해 경로를 더 직선에 가깝게 만든다. 경로가 직선에 가까우면 큰 걸음으로도 목표에 도달할 수 있어 1~10 스텝 생성이 가능해진다.

## 왜 작동하나
ODE(시간에 따라 위치가 연속적으로 변하는 방정식)를 풀 때 경로가 직선에 가까우면 일정 속도로 쭉 간다는 근사가 잘 맞는다. 그래서 스텝 수를 줄여도 오차가 작고, 샘플링 속도가 크게 빨라진다. 또한 reflow가 데이터 간 이동 계획을 더 단순하게 만들어 전이 학습에도 유리하다.

## 트레이드오프
- 여러 번 reflow를 돌리려면 학습 계산량과 데이터 생성 비용이 늘어난다.
- 경로를 너무 직선으로 만들면 복잡한 분포에서는 품질이 떨어지거나 특정 결과만 반복 생성할 수 있다.
- 실제 성능은 학습 스케줄, 페어링, regularization에 민감해서 튜닝이 필요하다.

## 계보
**이전**
- Diffusion Models
- [[techniques/flow-matching|Flow Matching]]
- Continuous Normalizing Flows
- Optimal Transport

**이후**
- InstaFlow
- Consistency Models
- MeanFlow
- Stochastic Interpolants

## 피지컬 AI에서의 쓰임
- 로봇 정책(action policy)을 노이즈에서 행동 시퀀스로 생성할 때, reflow로 직선화하면 제어 루프에서 1~수 스텝으로 빠른 행동 생성이 가능해진다.
- VLA(Vision-Language-Action) 모델의 action head가 diffusion/flow 기반일 때, Rectified Flow를 적용해 지연(latency)을 줄이고 실시간 조작에 쓸 수 있다.
- 월드모델이나 시뮬레이션에서 영상/상태 전이를 생성할 때, 적은 스텝으로 여러 미래 궤적을 빠르게 뽑아 계획(planning)에 쓸 수 있다.

## 💡 아이디어 훅
- LLM의 토큰 생성도 노이즈에서 텍스트로의 흐름으로 보고 reflow처럼 경로를 직선화하면 병렬 생성/디코딩을 줄일 수 있을까?
- 로봇의 여러 센서 모달리티(카메라, LiDAR, force)를 하나의 latent로 이동할 때 optimal transport와 reflow를 결합하면 더 안정적인 변환이 될까?
- diffusion policy를 한 스텝으로 줄이는 대신, 직선화 정도를 제어해 속도-품질-안전성을 조절하는 로봇 모드(예: 급회전 vs 정밀조작)를 만들 수 있을까?

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
