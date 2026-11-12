---
title: "SplatFlow: Self-Supervised Dynamic Gaussian Splatting in Neural Motion Flow Field for Autonomous Driving"
tags: [cvpr2025, autonomous-driving, embodied-perception]
venue: CVPR 2025
arxiv: "2411.15482"
citations: 25
auto: true
---

> **TL;DR** SplatFlow는 tracked 3D bounding box 없이 Neural Motion Flow Field 내 self-supervised dynamic Gaussian Splatting으로 4D 공간-시간 표현을 학습해 동적 도시 장면 재구성과 novel view RGB/depth/flow 합성을 수행한다.

**CVPR 2025** · Su Sun, Cheng Zhao, Zhuoyang Sun, Yingjie Victor Chen, Mei Chen
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Sun_SplatFlow_Self-Supervised_Dynamic_Gaussian_Splatting_in_Neural_Motion_Flow_Field_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2411.15482) · 인용 25회

**주제:** Autonomous Driving · Embodied Perception

## 문제
기존 dynamic Gaussian Splatting은 복잡한 동적 도시 장면에서 비싼 수동 라벨링 기반 object-level supervision에 의존해 실제 응용에서 확장성이 제한된다.

## 핵심 아이디어
NMFF를 이용해 LiDAR points와 Gaussians의 시간적 motion을 continuous motion flow field로 모델링하고 static background와 dynamic objects를 3D/4D Gaussian primitives로 분해한다. 또한 2D foundation model feature를 4D space-time representation에 distill해 dynamic object identification을 개선한다.

## 방법
SplatFlow는 time-dependent 4D Gaussian representation과 NMFF를 unified framework로 통합한다. NMFF는 각 4D Gaussian의 시간 간 correspondences를 모델링해 temporal features를 aggregate하고 dynamic components의 cross-view consistency를 향상한다. Waymo와 KITTI Dataset에서 평가된다.

## 결과
Waymo와 KITTI Dataset에서 dynamic urban scenarios의 image reconstruction 및 novel view synthesis 모두 SOTA 성능을 검증했다.

## 초록 (원문)
Most existing Dynamic Gaussian Splatting methods for complex dynamic urban scenarios rely on accurate object-level supervision from expensive manual labeling, limiting their scalability in real-world applications. In this paper, we introduce SplatFlow, a Self-Supervised Dynamic Gaussian Splatting within Neural Motion Flow Fields (NMFF) to learn 4D space-time representations without requiring tracked 3D bounding boxes, enabling accurate dynamic scene reconstruction and novel view RGB/depth/flow synthesis. SplatFlow designs a unified framework to seamlessly integrate time-dependent 4D Gaussian representation within NMFF, where NMFF is a set of implicit functions to model temporal motions of both LiDAR points and Gaussians as continuous motion flow fields. Leveraging NMFF, SplatFlow effectively decomposes static background and dynamic objects, representing them with 3D and 4D Gaussian primitives, respectively. NMFF also models the correspondences of each 4D Gaussian across time, which aggregates temporal features to enhance cross-view consistency of dynamic components. SplatFlow further improves dynamic object identification by distilling features from 2D foundation models into 4D space-time representation. Comprehensive evaluations conducted on the Waymo and KITTI Datasets validate SplatFlow's state-of-the-art (SOTA) performance for both image reconstruction and novel view synthesis in dynamic urban scenarios.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
