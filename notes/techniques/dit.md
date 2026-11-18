---
title: "DiT"
date: 2026-11-19
tags: [technique, architecture]
category: "아키텍처 모듈"
status: draft
---

> 이미지 생성 diffusion 모델의 뼈대인 U-Net을 ViT처럼 transformer로 갈아 끼운 것 — 이미지를 작은 퍼즐 조각(패치)으로 잘라 '단어'처럼 서로 대화시키는 방식

**대표 논문**: Scalable Diffusion Models with Transformers (2022, arXiv / ICCV 2023) · **분류**: 아키텍처 모듈

## 해결한 문제
기존 diffusion 모델은 대부분 U-Net(해상도를 줄였다 늘리는 CNN 기반 구조)을 노이즈 예측기로 썼다. 이 구조는 해상도별 층을 사람이 설계한 느낌이라, 모델을 키울 때 '그냥 크게 만들면 좋아진다'는 예측 가능한 확장이 어려웠다. 반면 ViT 계열 transformer는 언어·비전에서 크기를 키울수록 성능이 꾸준히 오르는 스케일링 특성을 이미 보여주고 있었다.

## 핵심 아이디어
비유하자면 '완성 그림을 작은 퍼즐 조각으로 잘라 탁자에 늘어놓고, 각 조각이 서로 대화하며 전체 그림을 맞춰가는 방식'이다. 실제로는 (1) VAE(이미지를 작은 압축 표현으로 바꿔주는 인코더)로 이미지를 작은 latent 격자로 압축하고, (2) 그 격자를 일정 크기 패치로 잘라 각 패치를 토큰으로 만들고 위치 정보를 붙인 뒤, (3) transformer 블록 여러 층에 통과시키며 각 블록에서 timestep(노이즈 세기)과 class 같은 조건을 adaLN-Zero(조건에 맞춰 정규화 계수를 조정하고, 초기엔 0으로 꺼두는 방식)로 주입하고, (4) 마지막 선형 레이어로 각 패치의 노이즈를 예측한다.

## 왜 작동하나
transformer는 모든 패치가 한 층에서 바로 서로를 보기 때문에, CNN이 국소 영역을 층층이 넓혀가며 얻는 전역 정보를 훨씬 직접적으로 얻는다. 또 토큰 수·층 수·폭을 늘리면 성능이 예측 가능하게 따라 오르는 스케일링 특성이 있어서, '더 큰 모델 = 더 좋은 생성'이라는 공식을 diffusion에도 그대로 쓸 수 있게 했다. adaLN-Zero로 조건을 넣으면 학습 초반에 조건 경로가 0으로 꺼진 상태에서 시작해 학습이 안정적이다.

## 트레이드오프
- 이미지를 패치로 나누면 해상도가 올라갈수록 토큰 수가 제곱으로 늘어 계산량과 메모리가 급격히 비싸진다.
- U-Net이 갖고 있던 다중 해상도 구조라는 '공짜 힌트'가 없어서, 같은 품질을 내려면 더 많은 데이터와 학습 연산이 필요할 수 있다.
- 성능 상한이 VAE의 압축 품질에 묶여 있어, VAE가 버린 디테일은 transformer가 아무리 커도 되살리기 어렵다.

## 계보
**이전**
- [[techniques/ddpm|DDPM (U-Net 기반 diffusion)]]
- ADM / Guided Diffusion (U-Net + classifier guidance)
- Latent Diffusion Models (Stable Diffusion의 latent 공간 diffusion)
- [[techniques/vit|ViT (Vision Transformer)]]

**이후**
- SiT (interpolant 기반 transformer diffusion)
- PixArt-α / PixArt-Σ
- Stable Diffusion 3의 MMDiT
- FLUX
- Lumina, HunyuanDiT 등 DiT 계열 T2I 모델

## 피지컬 AI에서의 쓰임
- 로봇 정책의 diffusion head: 관측을 토큰으로 넣고 transformer가 미래 행동 궤적(연속 action chunk)의 노이즈를 예측하도록 학습 (Diffusion Policy 계열의 transformer 백본).
- VLA(비전-언어-행동) 모델에서 언어·이미지·행동 토큰을 한 transformer에 함께 넣고, 행동 부분만 diffusion 방식으로 생성하는 구조.
- 월드모델/비디오 생성: 로봇 카메라 영상의 다음 프레임들을 latent 패치 단위로 예측해 '상상 속 롤아웃'을 만드는 데 사용.

## 💡 아이디어 훅
- 로봇 궤적처럼 1차원 시계열(관절 값 나열)에도 '패치 토큰화 + adaLN 조건 주입'을 그대로 쓸 수 있을까?
- adaLN-Zero로 조건을 넣는 방식을 timestep·언어 지시문·힘 센서 값 등 여러 조건에 동시에 적용하면 어떤 이점이 있을까?
- 패치 크기를 키우면 속도는 빨라지고 디테일은 떨어질 텐데, 로봇의 거친 동작 계획과 정밀 조작을 서로 다른 패치 해상도로 나눠 처리할 수 있을까?

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
