---
title: "Knowledge Distillation"
date: 2026-11-19
tags: [technique, efficiency]
category: "효율화·적응"
status: draft
---

> 큰 '선생님' 모델이 정답을 맞히는 요령(확신의 정도까지)을 작은 '학생' 모델에게 과외로 옮겨 담는 효율화 기술

**대표 논문**: Distilling the Knowledge in a Neural Network (2015) · **분류**: 효율화·적응

## 해결한 문제
성능 좋은 큰 모델은 정확하지만 느리고 메모리를 많이 먹어서 휴대폰이나 로봇 온보드에서는 쓰기 어렵습니다. 그렇다고 작은 모델을 그냥 처음부터 학습시키면, 큰 모델이 은근히 알고 있는 '이 둘은 헷갈린다' 같은 미묘한 판단 감각을 배우지 못해 정확도가 뚝 떨어집니다.

## 핵심 아이디어
정답만 알려주는 대신 '이 문제는 고양이 70%, 개 25%, 자동차 5% 같아'라고 확신의 정도까지 알려주는 과외 선생님과 같습니다. 작동 순서는 이렇습니다. (1) 잘 학습된 큰 teacher 모델에 입력을 넣어 각 클래스에 대한 확률 분포를 뽑고, temperature(확률을 일부러 부드럽게 펴주는 값)로 뾰족한 분포를 완만하게 만듭니다. (2) 작은 student 모델이 같은 입력에 대해 같은 확률 분포를 내도록 두 분포의 차이(KL divergence)를 줄이며 학습합니다. (3) 실제 정답(hard label)에 대한 손실과 섞어서, 정답도 맞히면서 선생님의 '감각'도 따라 하게 만듭니다.

## 왜 작동하나
정답 하나만 주는 학습은 '이건 고양이'라는 한 조각 정보뿐이지만, 부드러운 확률 분포에는 '고양이는 개랑 비슷하고 자동차랑은 전혀 다르다'는 클래스 사이의 관계 지도가 통째로 담겨 있습니다. 그래서 student는 훨씬 많은 정보를 한 번에 받아 적은 데이터로도 더 잘 일반화하고, 이 부드러운 신호가 일종의 정규화 역할을 해 과적합도 줄여줍니다.

## 트레이드오프
- teacher를 따로 충분히 잘 학습시켜야 하므로 준비 비용과 시간이 추가로 듭니다.
- teacher가 가진 편향이나 오류까지 student가 그대로 물려받을 수 있습니다.
- temperature 값이나 두 손실의 비율 같은 하이퍼파라미터를 잘 맞춰야 효과가 나고, student가 너무 작으면 담을 수 있는 용량 자체가 부족합니다.

## 계보
**이전**
- Model Compression (2006)
- Soft Targets / Label Smoothing
- Teacher-Student 학습 (Buciluǎ et al., 2006)

**이후**
- FitNets (중간 특징 증류)
- DistilBERT
- TinyBERT
- Attention Transfer
- Decoupled Knowledge Distillation (DKD)
- Self-Distillation
- Consistency Distillation (diffusion 샘플링 가속)

## 피지컬 AI에서의 쓰임
- VLA(로봇이 보고 지시를 이해해 행동하는 모델)나 대형 정책 모델을 로봇 온보드에서 돌아가는 소형 모델로 증류해 지연 시간을 줄이는 용도
- Diffusion Policy처럼 여러 번 샘플링해서 느린 생성형 정책을, 적은 스텝으로 비슷한 행동을 내는 student로 증류해 실시간 제어에 맞추는 용도
- LLM 에이전트에서 큰 모델의 판단·도구 호출 패턴을 작은 모델에 옮겨 API 비용과 응답 시간을 아끼는 용도

## 💡 아이디어 훅
- 정답 확률 대신 teacher의 중간 특징이나 attention 패턴까지 맞추게 하면 어떤 이득이 있을까?
- 여러 teacher(앙상블)의 지식을 하나의 student에 합쳐 담으면 단일 teacher보다 나을까?
- 시뮬레이터에서 학습한 teacher를 실제 로봇용 student로 증류하면 sim-to-real 격차를 줄이는 데 도움이 될까?

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
