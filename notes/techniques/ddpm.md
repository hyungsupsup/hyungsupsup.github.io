---
title: "DDPM"
date: 2026-11-21
tags: [technique, generative]
category: "생성모델"
status: draft
---

> 사진을 아주 작은 소음으로 천천히 망가뜨리는 과정을 배우고, 그 역순으로 노이즈 덩어리에서 그림을 복원하는 생성모델

**대표 논문**: Denoising Diffusion Probabilistic Models (2020) · **분류**: 생성모델

## 해결한 문제
DDPM 이전에는 GAN(생성적 적대 신경망)이 학습이 불안정하고, VAE(변분 오토인코더)는 생성 결과가 흐릿한 경우가 많았음. Normalizing Flow(정규화 흐름) 같은 방법도 모델 구조 제약이 커서 복잡한 이미지를 자연스럽게 만들기 어려웠음.

## 핵심 아이디어
비유하자면, 깨끗한 그림에 눈가루를 조금씩 뿌려 완전히 하얀 눈더미로 만드는 과정을 보고, 다시 눈더미에서 그림을 하나씩 긁어내는 법을 배우는 것과 같음. DDPM은 실제 이미지를 여러 단계에 걸쳐 가우시안 노이즈(무작위 소음)로 바꾸는 forward process(앞으로 가는 과정)를 정의하고, 모델은 그 역순으로 노이즈를 조금씩 제거하는 reverse process(뒤로 가는 과정)를 학습함. 학습할 때는 이미지에서 노이즈를 얼마나 넣었는지 알려주고, 모델이 그 노이즈를 예측하게 하거나 원본 이미지를 추정하게 함. 샘플링할 때는 완전한 노이즈에서 시작해 같은 모델을 반복 사용하면서 단계별로 노이즈를 제거해 이미지를 만들어냄.

## 왜 작동하나
한 번에 노이즈에서 이미지를 바로 만드는 대신, 아주 작은 단계로 나누어 문제를 쉽게 만듦. 각 단계는 '조금만 덜 노이즈 낀 이미지'를 예측하는 단순한 학습이므로 GAN처럼 생성자와 판별자가 싸우는 불안정한 구조보다 안정적임. 덕분에 다양한 이미지를 고르게 만들 수 있고, 학습이 비교적 잘 됨.

## 트레이드오프
- 샘플링에 수십~수백 단계가 필요해 GAN보다 느릴 수 있음
- 이미지 해상도가 커지면 계산량과 메모리가 크게 늘어남
- 최고의 선명도나 세부 묘사는 GAN 계열보다 약할 수 있어 후처리나 개선 기법이 필요함

## 계보
**이전**
- Denoising Autoencoder(노이즈 제거 오토인코더)
- [[techniques/score-matching|Score Matching(점수 매칭)]]
- Deep Generative Models(심층 생성모델)
- Variational Autoencoder(VAE)
- Generative Adversarial Network(GAN)

**이후**
- [[techniques/ddim|DDIM(Denoising Diffusion Implicit Models)]]
- Score-Based Generative Modeling through SDEs
- Latent Diffusion Models
- DPM-Solver
- Consistency Models
- [[techniques/rectified-flow|Rectified Flow]]

## 피지컬 AI에서의 쓰임
- 로봇이 여러 단계의 동작을 한 번에 계획할 때, 노이즈에서 시작해 자연스러운 action sequence(동작 시퀀스)를 생성하는 diffusion policy로 사용됨
- VLA(Vision-Language-Action) 모델에서 언어 지시에 맞는 로봇 동작을 생성하는 디코더로 DDPM 계열을 쓸 수 있음
- 월드모델이나 시뮬레이터에서 미래 영상·물체 상태를 생성할 때, 노이즈에서 시작해 일관된 장면 변화를 만드는 생성기로 활용됨

## 💡 아이디어 훅
- DDPM의 노이즈 제거 단계를 로봇의 '작은 동작 수정' 과정으로 바꾸면 더 안정적인 제어기가 될까?
- 이미지 대신 로봇의 관절 각도 시퀀스에 DDPM을 적용하면, 불확실한 환경에서 여러 개의 가능한 동작을 어떻게 고를 수 있을까?
- 샘플링 단계를 줄이는 DDIM이나 consistency model을 VLA에 붙이면, 실시간 로봇 제어에 필요한 속도를 맞출 수 있을까?

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
