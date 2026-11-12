---
title: "FIction: 4D Future Interaction Prediction from Video"
tags: [cvpr2025, embodied-perception, world-model]
venue: CVPR 2025
arxiv: "2412.00932"
citations: 12
auto: true
---

> **TL;DR** 비디오로부터 사람이 다음에 어떤 객체와 어디서 어떻게 상호작용할지를 4D로 예측하는 FIction을 제안한다.

**CVPR 2025** · Kumar Ashutosh, Georgios Pavlakos, Kristen Grauman
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Ashutosh_FIction_4D_Future_Interaction_Prediction_from_Video_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2412.00932) · 인용 12회

**주제:** Embodied Perception · World Model

## 문제
기존 방법은 2D 비디오 프레임에 국한되어 '무엇'만 예측하고, 물리적으로 grounding된 '어디서'와 '어떻게'를 놓친다.

## 핵심 아이디어
과거 비디오에서 사람의 행동과 환경을 융합해 미래 상호작용의 3D 위치와 실행 포즈를 함께 예측한다.

## 방법
입력 비디오에서 사람의 과거 행동과 주변 환경 정보를 통합하고, 미래 시간 구간의 상호작용 객체, 3D 위치, 그리고 bending/reaching/pulling 등의 포즈를 예측한다. Ego-Exo4D의 다양한 활동과 실제 환경에서 평가한다.

## 결과
Ego-Exo4D에서 기존 autoregressive 및 lifted 2D video 모델보다 substantially 우수하며 30% 이상의 relative gains를 보인다.

## 초록 (원문)
Anticipating how a person will interact with objects in an environment is essential for activity understanding, but existing methods are limited to the 2D space of video frames--capturing physically ungrounded predictions of "what" and ignoring the "where" and "how". We introduce FIction for 4D future interaction prediction from videos. Given an input video of a human activity, the goal is to predict which objects at what 3D locations the person will interact with in the next time period (e.g., cabinet, fridge), and how they will execute that interaction (e.g., poses for bending, reaching, pulling). Our novel model FIction fuses the past video observation of the person's actions and their environment to predict both the "where" and "how" of future interactions. Through comprehensive experiments on a variety of activities and real-world environments in Ego-Exo4D, we show that our proposed approach outperforms prior autoregressive and (lifted) 2D video models substantially, with more than 30% relative gains.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
