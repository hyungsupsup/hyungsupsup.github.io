---
title: "Flow Matching"
date: 2026-11-20
tags: [technique, generative]
category: "생성모델"
status: draft
---

> Flow Matching은 소음에서 데이터로 가는 '바람길(속도장)'을 학습해, 이미지를 마치 물줄기를 따라 흐르듯 만들어내는 생성모델이다.

**대표 논문**: Flow Matching for Generative Modeling (2022) · **분류**: 생성모델

## 해결한 문제
기존 diffusion model(이미지를 노이즈에서 복원하는 생성모델)은 이미지를 조금씩 망가뜨렸다가 다시 복원하는 복잡한 확률 과정을 여러 단계로 반복해야 해서 학습과 샘플링이 무거웠다. Continuous Normalizing Flow(데이터를 연속 변환으로 생성하는 모델)는 유연하지만 학습이 불안정하고 정확한 속도장을 찾기 어려웠다.

## 핵심 아이디어
비유하자면, 눈사람(소음)에서 조각상(데이터)으로 가는 가장 짧은 물길을 미리 정하고, 그 물길을 따라 흐르는 속도만 배우는 것이다. 먼저 소음과 실제 데이터를 직선으로 이어 중간 상태를 만들고, 그 구간에서 '어디로 얼마나 빨리 가야 하는지'를 나타내는 속도 벡터를 계산한다. 네트워크는 이 속도 벡터를 예측하도록 간단히 회귀 학습한다. 샘플링할 때는 소음에서 시작해 네트워크가 알려주는 속도를 따라 ODE(미분방정식)를 조금씩 적분하면 데이터가 나온다.

## 왜 작동하나
복잡한 score matching(데이터 분포의 기울기를 맞추는 학습) 대신 '속도 예측'이라는 직관적인 목표만 배우므로 학습이 단순해진다. 경로가 직선에 가까우면 샘플링 단계 수를 줄여도 결과가 안정적이고, Continuous Normalizing Flow보다 더 유연한 벡터장을 쓸 수 있다.

## 트레이드오프
- 샘플링할 때 ODE solver(미분방정식 수치 계산기)를 여러 번 호출해야 해서 한 번에 끝나는 GAN(생성적 적대 신경망)보다 느릴 수 있다.
- 경로가 완전히 직선이 아니면 작은 오차가 누적되어 이미지 품질이 떨어질 수 있다.
- 데이터 분포가 매우 복잡하면 속도장을 정확히 배우기 어렵고, 학습 데이터와 모델 크기에 민감하다.

## 계보
**이전**
- Diffusion Models
- Score-based Generative Models
- Continuous Normalizing Flows
- Neural ODEs

**이후**
- [[techniques/rectified-flow|Rectified Flow]]
- Stochastic Interpolants
- Flow Matching with Optimal Transport
- Diffusion/Flow Distillation

## 피지컬 AI에서의 쓰임
- 로봇 정책(VLA: Vision-Language-Action, 보고 말하고 움직이는 로봇 모델)에서 여러 단계의 동작을 한 덩어리로 생성할 때, diffusion policy보다 적은 단계로 action chunk를 뽑아 실시간 제어에 유리하다.
- 월드모델이 다음 프레임이나 물체 상태를 생성할 때, 소음에서 실제 관측으로 가는 속도장을 학습해 비디오/상태 예측을 빠르게 만든다.
- 이미지 생성에서 text-to-image 모델이 latent space(이미지를 압축한 벡터 공간)의 소음에서 이미지로 흐르는 경로를 학습해, 고해상도 생성과 편집에 쓸 수 있다.

## 💡 아이디어 훅
- 로봇의 연속 동작을 '소음에서 목표 동작까지 흐르는 속도장'으로 보면, 충돌 회피나 안전 제약을 속도장에 어떻게 넣을까?
- Flow Matching의 직선 경로를 더 직선에 가깝게 만드는 Rectified Flow를 LLM의 토큰 생성이나 action token 생성에 적용할 수 있을까?
- VLA에서 여러 action chunk를 병렬로 생성할 때, 조건부 Flow Matching을 쓰면 시간 일관성과 반응 속도를 동시에 잡을 수 있을까?

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
