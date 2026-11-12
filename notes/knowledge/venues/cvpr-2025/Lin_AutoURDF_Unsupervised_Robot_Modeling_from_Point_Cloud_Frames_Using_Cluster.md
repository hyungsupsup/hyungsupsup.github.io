---
title: "AutoURDF: Unsupervised Robot Modeling from Point Cloud Frames Using Cluster Registration"
tags: [cvpr2025, simulation-sim2real, embodied-perception]
venue: CVPR 2025
arxiv: "2412.05507"
citations: 11
auto: true
---

> **TL;DR** AutoURDF는 포인트 클라우드 프레임만으로 미지의 로봇에 대한 URDF 설명 파일을 비지도 방식으로 생성하는 방법이다.

**CVPR 2025** · Jiong Lin, Lechen Zhang, Kwansoo Lee, Jialong Ning, Judah Goldfeder, Hod Lipson
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_AutoURDF_Unsupervised_Robot_Modeling_from_Point_Cloud_Frames_Using_Cluster_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2412.05507) · 인용 11회

**주제:** Simulation & Sim2Real · Embodied Perception

## 문제
로봇 설명 모델은 시뮬레이션과 제어에 필수적이지만, 이를 만드는 데 많은 수작업이 필요하다. 본 논문은 보지 못한 로봇의 설명 파일을 포인트 클라우드로부터 자동 생성하는 문제를 다룬다.

## 핵심 아이디어
클러스터 기반 포인트 클라우드 registration 모델로 포인트 클러스터의 6-DoF 변환을 추적하고, 클러스터 움직임을 분석해 로봇 구조를 계층적으로 추론한다.

## 방법
각 포인트 클러스터의 6-DoF 변환을 추적하는 cluster-based point cloud registration을 수행한다. 클러스터 이동을 분석하여 moving part segmentation, body topology inference, joint parameter estimation을 순차적으로 해결한다. 최종 파이프라인은 기존 시뮬레이터와 호환되는 robot description file을 생성한다.

## 결과
합성 및 실제 스캔 데이터의 다양한 로봇에서 검증했으며, registration과 body topology estimation 정확도에서 이전 방법보다 우수한 성능을 보인다. 확장 가능한 자동 로봇 모델링 솔루션을 제공한다고 주장한다.

## 초록 (원문)
Robot description models are essential for simulation and control, yet their creation often requires significant manual effort. To streamline this modeling process, we introduce AutoURDF, an unsupervised approach for constructing description files for unseen robots from point cloud frames. Our method leverages a cluster-based point cloud registration model that tracks the 6-DoF transformations of point clusters. Through analyzing cluster movements, we hierarchically address the following challenges: (1) moving part segmentation, (2) body topology inference, and (3) joint parameter estimation. The complete pipeline produces robot description files that are fully compatible with existing simulators. We validate our method across a variety of robots, using both synthetic and real-world scan data. Results indicate that our approach outperforms previous methods in registration and body topology estimation accuracy, offering a scalable solution for automated robot modeling.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
