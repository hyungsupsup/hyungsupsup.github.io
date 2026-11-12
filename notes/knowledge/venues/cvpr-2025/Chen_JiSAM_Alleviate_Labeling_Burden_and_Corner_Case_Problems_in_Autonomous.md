---
title: "JiSAM: Alleviate Labeling Burden and Corner Case Problems in Autonomous Driving via Minimal Real-World Data"
tags: [cvpr2025, simulation-sim2real, autonomous-driving, embodied-perception]
venue: CVPR 2025
arxiv: "2503.08422"
citations: 4
auto: true
---

> **TL;DR** JiSAM은 소량의 실제 LiDAR 라벨과 시뮬레이션 데이터를 활용해 자율주행 3D 인식의 라벨링 부담과 corner case 문제를 완화하는 plug-and-play 방법이다.

**CVPR 2025** · Runjian Chen, Wenqi Shao, Bo Zhang, Shaoshuai Shi, Li Jiang, Ping Luo
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_JiSAM_Alleviate_Labeling_Burden_and_Corner_Case_Problems_in_Autonomous_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.08422) · 인용 4회

**주제:** Simulation & Sim2Real · Autonomous Driving · Embodied Perception

## 문제
실제 LiDAR 데이터는 라벨링 비용이 크고 rare traffic participants 같은 corner case가 부족하며, 시뮬레이션 데이터는 샘플 효율성과 sim-to-real gap 때문에 실제 인식 성능 향상에 쓰기 어렵다.

## 핵심 아이디어
시뮬레이션의 labeled LiDAR와 corner case를 활용하되, Jittering augmentation, domain-aware backbone, memory-based Sectorized AlignMent를 결합해 적은 실제 데이터로도 sim-to-real 적응을 가능하게 한다.

## 방법
JiSAM은 plug-and-play 방식으로 synthetic LiDAR point cloud를 실제 3D object detection 학습에 통합한다. Jittering augmentation과 domain-aware backbone으로 도메인 차이를 줄이고, memory-based Sectorized AlignMent로 시뮬레이션과 실제 특징을 정렬한다.

## 결과
NuScenes에서 SOTA 3D object detector와 결합해 전체 실제 데이터로 학습한 모델에 comparable한 성능을 2.5% 실제 라벨만으로 달성했고, 실제 학습셋에 라벨이 없는 객체에서 15 mAPs 이상을 얻었다.

## 연결
- **기반 대표 논문:** Isaac Gym — [[knowledge/map|분야 지도]]

## 초록 (원문)
Deep-learning-based autonomous driving (AD) perception introduces a promising picture for safe and environment-friendly transportation. However, the over-reliance on real labeled data in LiDAR perception limits the scale of on-road attempts. 3D real world data is notoriously time-and-energy-consuming to annotate and lacks corner cases like rare traffic participants. On the contrary, in simulators like CARLA, generating labeled LiDAR point clouds with corner cases is a piece of cake. However, introducing synthetic point clouds to improve real perception is non-trivial. This stems from two challenges: 1) sample efficiency of simulation datasets 2) simulation-to-real gaps. To overcome both challenges, we propose a plug-and-play method called JiSAM, shorthand for Jittering augmentation, domain-aware backbone and memory-based Sectorized AlignMent. In extensive experiments conducted on the famous AD dataset NuScenes, we demonstrate that, with SOTA 3D object detector, JiSAM is able to utilize the simulation data and only labels on 2.5% available real data to achieve comparable performance to models trained on all real data. Additionally, JiSAM achieves more than 15 mAPs on the objects not labeled in the real training set. We will release models and codes.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
