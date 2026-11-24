---
title: "Structured Pruning"
date: 2026-11-25
tags: [technique, efficiency]
category: "효율화·적응"
status: draft
---

> 가중치 하나하나를 자르는 대신, 쓸모없는 필터·채널·attention head 같은 덩어리를 통째로 뽑아 모델의 모양을 깔끔하게 줄이는 방법

**대표 논문**: Pruning Filters for Efficient ConvNets (2017) · **분류**: 효율화·적응

## 해결한 문제
예전에는 unstructured pruning(개별 가중치만 0으로 만드는 방식)이 많았지만, GPU는 0이 여기저기 흩어져 있으면 연산량을 크게 줄이기 어려웠다. 그래서 모델은 작아진 것 같아도 실제 속도·메모리 이득이 작았다.

## 핵심 아이디어
비유하자면 책장에서 책 한 권만 빼는 게 아니라, 쓸모없는 칸이나 서랍 전체를 통째로 빼는 것이다. 먼저 필터, 채널, attention head, 행/열 같은 구조 단위를 중요도 점수로 평가한다. 점수가 낮은 단위를 통째로 제거하고, 남은 모델로 fine-tuning(다시 학습)해 성능을 회복한다. 결과적으로 convolution(합성곱)이나 matrix multiplication(행렬 곱)의 크기가 실제로 줄어든다.

## 왜 작동하나
구조 단위로 자르면 GPU/TPU가 좋아하는 규칙적인 작은 행렬만 남는다. 메모리 접근과 연산이 한 덩어리로 줄어 실제 latency(지연시간)과 power(전력)가 개선된다. unstructured pruning보다 하드웨어 이득이 예측 가능하고 크다.

## 트레이드오프
- 너무 많이 자르면 중요한 특징까지 날아가 정확도가 크게 떨어진다.
- 자른 뒤 재학습이 필요해 시간과 데이터가 든다.
- 하드웨어/레이어마다 자를 수 있는 단위가 달라 적용이 번거롭다.

## 계보
**이전**
- Unstructured weight pruning
- Magnitude pruning
- L1 regularization

**이후**
- Block-sparse pruning
- Channel pruning
- Attention-head pruning
- Sparse Transformers
- Pruning-aware NAS

## 피지컬 AI에서의 쓰임
- 로봇 온디바이스 VLA(비전-언어-행동 모델)에서 attention head나 MLP 채널을 잘라 GPU/엣지 NPU에서 제어 루프 지연을 줄인다.
- 자율주행 perception CNN의 convolution filter를 잘라 카메라 스트림 처리 속도를 높인다.
- 로봇용 diffusion policy나 world model의 UNet/transformer 블록을 구조적으로 잘라 추론 메모리를 줄인다.

## 💡 아이디어 훅
- VLA에서 특정 작업(파지, 이동)에만 중요한 head를 찾아 작업별로 다른 구조를 자르면 어떨까?
- 월드모델의 future prediction 정확도와 pruning 강도를 실시간으로 조절할 수 있을까?
- 로봇이 실패한 장면에서 중요도가 올라간 채널을 다시 살리는 dynamic structured pruning이 가능할까?

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
