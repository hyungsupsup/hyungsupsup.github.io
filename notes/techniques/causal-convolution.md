---
title: "Causal Convolution"
date: 2026-11-20
tags: [technique, architecture]
category: "아키텍처 모듈"
status: draft
---

> 미래를 몰래 보지 않고 과거와 현재만 참고하는 1D 컨볼루션(입력 시퀀스에 작은 필터를 밀어 붙여 가중합을 계산하는 연산)입니다.

**대표 논문**: WaveNet: A Generative Model for Raw Audio (2016) · **분류**: 아키텍처 모듈

## 해결한 문제
RNN/LSTM(시간 순서대로 상태를 이어가는 순환 신경망)은 시간축을 하나씩 계산해야 해서 병렬화가 느리고, 긴 시퀀스에서 학습이 불안정할 수 있었습니다. 일반 컨볼루션은 주변 입력을 함께 보므로 예측이나 생성에서 미래 정보를 우연히 참고하면 성능이 과대평가될 수 있었습니다.

## 핵심 아이디어
마치 요리사가 다음에 넣을 재료를 미리 보지 않고 지금까지 넣은 재료만 맛보는 것과 같습니다. 컨볼루션 필터가 시간 t에서 t 이전과 t의 입력만 보도록 왼쪽만 패딩(입력 끝을 빈 값으로 채워 크기를 유지하는 것)하고, 여러 층을 쌓아 참고 범위를 넓힙니다. 필요하면 dilation(필터 간격을 벌려 더 먼 과거를 보는 기법)으로 긴 과거를 빠르게 봅니다.

## 왜 작동하나
미래를 차단해 학습과 추론의 정보 누수를 막으면서도, 컨볼루션이라 시간 축을 병렬로 계산할 수 있습니다. 층을 쌓거나 dilation을 쓰면 RNN처럼 매 스텝 순차 계산 없이도 긴 과거를 참고할 수 있습니다.

## 트레이드오프
- 한 층의 참고 범위가 제한되어 긴 의존성은 여러 층으로 해결해야 합니다.
- 시퀀스 초반에는 과거가 부족해 출력이 불안정할 수 있습니다.
- 생성할 때는 여전히 다음 토큰이나 프레임을 하나씩 만들어야 해 추론이 완전히 병렬은 아닙니다.

## 계보
**이전**
- RNN
- LSTM
- GRU
- standard 1D convolution
- autoregressive models

**이후**
- Temporal Convolutional Network (TCN)
- WaveNet
- causal Transformer
- Mamba/State Space Models
- causal video diffusion temporal layers

## 피지컬 AI에서의 쓰임
- 로봇의 과거 관절/IMU(관성 측정 장치)/카메라 시퀀스로 다음 동작을 예측할 때, 미래 센서 값을 몰래 보지 않고 현실적인 제어 추론을 할 수 있습니다.
- VLA(비전-언어-액션) 모델에서 토큰이나 동작을 순서대로 생성할 때, 이미 생성된 과거 동작만 참고하도록 안정화하는 데 쓸 수 있습니다.
- 월드모델 rollout(모델이 과거 관측으로 미래를 순서대로 예측해 보는 것)에서 시간축 블록에 causal convolution을 넣어 현재까지의 관측으로 다음 프레임을 예측하는 구조를 만들 수 있습니다.

## 💡 아이디어 훅
- Causal convolution과 attention을 섞으면 긴 과거는 convolution으로 빠르게 보고, 중요한 과거만 attention으로 정밀하게 보는 하이브리드는 어떨까?
- 로봇 시뮬레이션에서 teacher forcing(학습 때 정답 과거를 넣어주는 방식)과 causal convolution을 결합해 학습/추론 차이를 줄일 수 있을까?
- Video diffusion에서 temporal layer를 causal convolution으로 바꾸면 실시간 스트리밍 생성이 더 쉬워질까?

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
