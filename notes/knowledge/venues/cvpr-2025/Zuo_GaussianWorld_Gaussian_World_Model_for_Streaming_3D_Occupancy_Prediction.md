---
title: "GaussianWorld: Gaussian World Model for Streaming 3D Occupancy Prediction"
tags: [cvpr2025, world-model, autonomous-driving, embodied-perception]
venue: CVPR 2025
arxiv: "2412.10373"
citations: 94
auto: true
---

> **TL;DR** GaussianWorld는 현재 센서 입력을 조건으로 장면 진화를 3D Gaussian 공간에서 예측하는 world-model 기반 스트리밍 3D occupancy 예측 프레임워크이다.

**CVPR 2025** · Sicheng Zuo, Wenzhao Zheng, Yuanhui Huang, Jie Zhou, Jiwen Lu
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Zuo_GaussianWorld_Gaussian_World_Model_for_Streaming_3D_Occupancy_Prediction_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2412.10373) · 인용 94회

**주제:** World Model · Autonomous Driving · Embodied Perception

## 문제
기존 스트리밍 3D occupancy 예측 방법은 이전 프레임 표현을 융합하지만, 주행 장면의 연속성과 3D 장면 진화가 제공하는 강한 사전 정보를 충분히 활용하지 못한다.

## 핵심 아이디어
3D occupancy 예측을 현재 센서 입력에 조건화된 4D occupancy forecasting 문제로 재정식화하고, 장면 진화를 ego motion alignment, dynamic object movement, newly-observed scene completion으로 분해해 Gaussian world model로 명시적으로 활용한다.

## 방법
GaussianWorld는 정적 장면의 ego motion alignment, 동적 객체의 국소 이동, 새로 관측된 장면의 완성을 세 요인으로 나누어 장면 진화를 모델링한다. 현재 RGB 관측을 고려해 3D Gaussian 공간에서 장면 진화를 추론하고 이를 occupancy 예측에 활용한다.

## 결과
nuScenes에서 GaussianWorld는 추가 연산 없이 single-frame counterpart 대비 mIoU를 over 2% 향상시켰다.

## 연결
- **기반 대표 논문:** World Models (Ha & Schmidhuber) — [[knowledge/map|분야 지도]]
- 인용함 → [[knowledge/venues/cvpr-2025/Zhao_DriveDreamer4D_World_Models_Are_Effective_Data_Machines_for_4D_Driving|DriveDreamer4D: World Models Are Effective Data Machines for 4D Driving Scene Representation]]

## 초록 (원문)
3D occupancy prediction is important for autonomous driving due to its comprehensive perception of the surroundings. To incorporate sequential inputs, most existing methods fuse representations from previous frames to infer the current 3D occupancy. However, they fail to consider the continuity of driving scenarios and ignore the strong prior provided by the evolution of 3D scenes (e.g., only dynamic objects move). In this paper, we propose a world-modelbased framework to exploit the scene evolution for perception. We reformulate 3D occupancy prediction as a 4D occupancy forecasting problem conditioned on the current sensor input. We decompose the scene evolution into three factors: 1) ego motion alignment of static scenes; 2) local movements of dynamic objects; and 3) completion of newly-observed scenes. We then employ a Gaussian world model (GaussianWorld) to explicitly exploit these priors and infer the scene evolution in the 3D Gaussian space considering the current RGB observation. We evaluate the effectiveness of our framework on the widely used nuScenes dataset. Our GaussianWorld improves the performance of the single-frame counterpart by over 2% in mIoU without introducing additional computations.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
