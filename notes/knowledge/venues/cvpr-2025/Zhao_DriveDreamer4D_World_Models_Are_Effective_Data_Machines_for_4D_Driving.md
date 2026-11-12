---
title: "DriveDreamer4D: World Models Are Effective Data Machines for 4D Driving Scene Representation"
tags: [cvpr2025, world-model, autonomous-driving, simulation-sim2real]
venue: CVPR 2025
arxiv: "2410.13571"
citations: 152
auto: true
---

> **TL;DR** DriveDreamer4D는 world model을 데이터 생성기로 활용해 자율주행 장면의 4D 재구성 성능을 향상시키는 방법이다.

**CVPR 2025** · Guosheng Zhao, Chaojun Ni, Xiaofeng Wang, Zheng Zhu, Xueyang Zhang, Yida Wang 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_DriveDreamer4D_World_Models_Are_Effective_Data_Machines_for_4D_Driving_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2410.13571) · 인용 152회

**주제:** World Model · Autonomous Driving · Simulation & Sim2Real

## 문제
기존 NeRF 및 3DGS 기반 센서 시뮬레이션은 학습 데이터 분포와 가까운 전방 주행 상황에 치우쳐 있어 lane change, acceleration, deceleration 같은 복잡한 maneuver를 렌더링하는 데 한계가 있다. 또한 기존 자율주행 world model은 2D 비디오 생성에 머물러 동적 주행 환경의 spatiotemporal coherence를 충분히 담지 못한다.

## 핵심 아이디어
World model을 data machine으로 사용해 새로운 trajectory 비디오를 합성하고, structured condition으로 traffic element의 spatial-temporal consistency를 제어한다. 또한 real data와 synthetic data를 함께 활용하는 cousin data training strategy로 4DGS를 최적화한다.

## 방법
DriveDreamer4D는 world model prior를 활용해 novel trajectory videos를 생성하고, 이때 structured conditions를 명시적으로 사용해 교통 요소의 시공간 일관성을 제어한다. 생성된 synthetic data와 real data를 cousin data training strategy로 결합해 4DGS 기반 4D driving scene representation을 최적화한다. 저자들은 이를 driving scenario에서 video generation model로 4D reconstruction을 개선한 첫 사례라고 주장한다.

## 결과
DriveDreamer4D는 novel trajectory view에서 FID를 PVG, S3Gaussian, Deformable-GS 대비 각각 32.1%, 46.4%, 16.3% 상대적으로 개선했다. 또한 comprehensive user study와 NTA-IoU의 22.6%, 43.5%, 15.6% 상대적 증가로 driving agent의 spatiotemporal coherence 향상을 검증했다.

## 연결
- 인용됨 ← [[knowledge/venues/cvpr-2025/Zuo_GaussianWorld_Gaussian_World_Model_for_Streaming_3D_Occupancy_Prediction|GaussianWorld: Gaussian World Model for Streaming 3D Occupancy Prediction]]
- 인용됨 ← [[knowledge/venues/cvpr-2025/Ni_ReconDreamer_Crafting_World_Models_for_Driving_Scene_Reconstruction_via_Online|ReconDreamer: Crafting World Models for Driving Scene Reconstruction via Online Restoration]]

## 초록 (원문)
Closed-loop simulation is essential for advancing end-to-end autonomous driving systems. Contemporary sensor simulation methods, such as NeRF and 3DGS, rely predominantly on conditions closely aligned with training data distributions, which are largely confined to forward-driving scenarios. Consequently, these methods face limitations when rendering complex maneuvers (e.g., lane change, acceleration, deceleration). Recent advancements in autonomous-driving world models have demonstrated the potential to generate diverse driving videos. However, these approaches remain constrained to 2D video generation, inherently lacking the spatiotemporal coherence required to capture intricacies of dynamic driving environments.In this paper, we introduce DriveDreamer4D, which enhances 4D driving scene representation leveraging world model priors. Specifically, we utilize the world model as a data machine to synthesize novel trajectory videos, where structured conditions are explicitly leveraged to control the spatial-temporal consistency of traffic elements. Besides, the cousin data training strategy is proposed to facilitate merging real and synthetic data for optimizing 4DGS. To our knowledge, DriveDreamer4D is the first to utilize video generation models for improving 4D reconstruction in driving scenarios.Experimental results reveal that DriveDreamer4D significantly enhances generation quality under novel trajectory views, achieving a relative improvement in FID by 32.1%, 46.4%, and 16.3% compared to PVG, S3Gaussian, and Deformable-GS. Moreover, DriveDreamer4D markedly enhances the spatiotemporal coherence of driving agents, which is verified by a comprehensive user study and the relative increases of 22.6%, 43.5%, and 15.6% in the NTA-IoU metric.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
