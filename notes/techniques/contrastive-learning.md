---
title: "Contrastive Learning (SimCLR)"
date: 2026-11-28
tags: [technique, representation]
category: "표현학습"
status: draft
---

> 같은 사진의 여러 변형은 '친구', 다른 사진은 '남'으로 만들어 비슷한 표현끼리 붙이는 자기지도 학습

**대표 논문**: A Simple Framework for Contrastive Learning of Visual Representations (2020) · **분류**: 표현학습

## 해결한 문제
라벨이 많은 사진 분류는 비싸고, 라벨 없이 배우는 이전 방법들은 색칠·회전 예측처럼 목적이 좁아 실제 작업에 쓸 표현이 약했다. 그래서 '같은 물체/장면은 비슷하게, 다른 것은 다르게'라는 단순한 신호로 좋은 표현을 배우는 방법이 필요했다.

## 핵심 아이디어
마치 같은 사람을 정면/측면/어두운 사진으로 보고 '같은 사람'이라고 익히는 것처럼, 한 이미지를 여러 augmentation(자르기, 색상 변경, 흐림 등)으로 두 개 이상 만든다. 각 변형을 인코더로 벡터로 바꾸고, 같은 원본에서 온 벡터는 가깝게, 다른 원본에서 온 벡터는 멀게 만드는 contrastive loss(비교 손실)를 쓴다. 학습 후 인코더는 조명·각도·배경 변화에 흔들리지 않고 물체의 의미/구조를 잡는 표현을 만든다.

## 왜 작동하나
같은 물체의 여러 변형을 붙이려면 인코더가 색상, 위치, 작은 노이즈 같은 '쓸모없는 차이'를 무시하고 핵심 구조를 찾아야 한다. 다른 물체와 밀어내는 과정은 표현이 서로 겹치지 않게 구분력을 높여, 라벨 없이도 분류·검출·로봇 제어에 쓸 수 있는 일반적 특징을 만든다.

## 트레이드오프
- 좋은 결과를 위해 큰 배치와 많은 negative pair(다른 이미지들)가 필요해 메모리와 계산이 많이 든다.
- augmentation을 잘못 고르면 모델이 색상/크기 같은 단서만 배우고 실제 의미는 놓칠 수 있다.
- 같은 장면인데 다른 물체로 취급하거나, 다른 장면인데 같은 물체로 취급하면 표현이 왜곡될 수 있다.

## 계보
**이전**
- Rotation prediction
- Colorization
- Jigsaw puzzle
- Deep InfoMax
- Contrastive Predictive Coding (CPC)

**이후**
- MoCo
- BYOL
- SimSiam
- [[techniques/dino|DINO]]
- [[techniques/clip|CLIP]]
- VICReg

## 피지컬 AI에서의 쓰임
- 로봇 카메라로 찍은 같은 물체의 여러 각도/조명 이미지를 친구로 묶어, 라벨 없이 물체 인식·그리핑에 쓸 시각 인코더를 만든다.
- VLA(Vision-Language-Action) 모델의 시각 인코더를 사전학습할 때, 같은 장면의 여러 프레임/뷰를 가깝게 만들어 로봇이 시점 변화에 강한 표현을 쓰게 한다.
- 월드모델의 latent representation을 학습할 때, 같은 상태의 여러 관측을 붙이고 다른 상태를 밀어내어 예측·계획에 쓸 안정된 상태 표현을 만든다.

## 💡 아이디어 훅
- 로봇이 같은 물체를 다른 높이/조명에서 봐도 같은 latent로 묶으려면 어떤 augmentation이 가장 안전할까?
- 실패 궤적과 성공 궤적을 negative pair로 쓰면, '이 행동은 위험하다'는 표현을 배울 수 있을까?
- 이미지 대신 토큰/문장/음성/관측 시퀀스를 augmentation해 contrastive loss를 쓰면 어떤 표현이 생길까?

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
