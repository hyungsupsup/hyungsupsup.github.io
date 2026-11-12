---
title: "Vision-Language Embodiment for Monocular Depth Estimation"
tags: [cvpr2025, embodied-perception, autonomous-driving]
venue: CVPR 2025
arxiv: "2503.16535"
citations: 19
auto: true
---

> **TL;DR** 카메라의 물리적 특성과 텍스트 prior를 결합해 단안 깊이 추정을 실시간으로 수행하는 embodied perception 방법을 제안한다.

**CVPR 2025** · Jinchang Zhang, Guoyu Lu
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Vision-Language_Embodiment_for_Monocular_Depth_Estimation_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.16535) · 인용 19회

**주제:** Embodied Perception · Autonomous Driving

## 문제
단일 이미지로부터의 3D 복원은 본질적 불확실성이 있으며, 기존 깊이 추정 모델은 주로 이미지 간 관계에 의존해 카메라 자체의 내재적 정보를 충분히 활용하지 못한다.

## 핵심 아이디어
카메라 모델과 물리적 특성을 딥러닝 모델에 embodiment하여 추가 장비 없이 카메라 intrinsic만으로 embodied scene depth를 실시간 계산하고, 이를 RGB 특징 및 환경·깊이 정보를 담은 텍스트 설명과 결합한다.

## 방법
모델은 도로 환경과의 실시간 상호작용을 통해 즉각적인 환경 변화에 따라 embodied scene depth를 계산한다. 이 깊이 정보를 RGB 이미지 특징과 융합해 기하학적·시각적 세부를 함께 활용하며, 환경 내용과 깊이 정보를 포함한 텍스트 설명을 scene understanding prior로 통합한다.

## 결과
실험 결과 embodied depth estimation 방법이 서로 다른 장면에서 모델 성능을 향상시켰으며, 실시간 특성으로 동적 환경에서 지속적으로 인식과 행동을 조정할 수 있음을 보인다.

## 초록 (원문)
Depth estimation is a core problem in robotic perception and vision tasks, but 3D reconstruction from a single image presents inherent uncertainties. Current depth estimation models primarily rely on inter-image relationships for supervised training, often overlooking the intrinsic information provided by the camera itself. We propose a method that embodies the camera model and its physical characteristics into a deep learning model, computing embodied scene depth through real-time interactions with road environments. The model can calculate embodied scene depth in real-time based on immediate environmental changes using only the intrinsic properties of the camera, without any additional equipment. By combining embodied scene depth with RGB image features, the model gains a comprehensive perspective on both geometric and visual details. Additionally, we incorporate text descriptions containing environmental content and depth information as priors for scene understanding, enriching the model's perception of objects. This integration of image and language -- two inherently ambiguous modalities -- leverages their complementary strengths for monocular depth estimation. The real-time nature of the embodied language and depth prior model ensures that the model can continuously adjust its perception and behavior in dynamic environments. Experimental results show that the embodied depth estimation method enhances model performance across different scenes.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
