---
title: "DIO: Decomposable Implicit 4D Occupancy-Flow World Model"
tags: [cvpr2025, world-model, autonomous-driving, embodied-perception]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** DIO는 sparse LiDAR 관측으로부터 instance별로 분해 가능한 4D occupancy-flow를 추정하고 미래 horizon까지 예측하는 world model이다.

**CVPR 2025** · Christopher Diehl, Quinlan Sykora, Ben Agro, Thomas Gilles, Sergio Casas, Raquel Urtasun
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Diehl_DIO_Decomposable_Implicit_4D_Occupancy-Flow_World_Model_CVPR_2025_paper.html)

**주제:** World Model · Autonomous Driving · Embodied Perception

## 문제
Sparse LiDAR 관측만으로 현재 장면의 occupancy-flow를 추정하고 instance별 형상을 완성하며, 미래의 occupancy-flow 변화까지 예측하는 것이 문제이다.

## 핵심 아이디어
장면 occupancy-flow를 개별 instance로 분해할 수 있는 decomposable implicit 4D world model을 제안하고, off-the-shelf 3D detector의 instance prompt를 유연하게 받아들이는 prompt representation을 사용한다.

## 방법
DIO는 sparse LiDAR 관측으로부터 scene occupancy-flow를 추정하고 이를 individual instances로 분해한다. 현재 시점의 instance shape를 완성할 뿐 아니라 future horizon에 걸친 occupancy-flow evolution을 forecast한다. 또한 3D detectors와 같은 off-the-shelf 모델의 instance prompts를 입력으로 활용할 수 있다.

## 결과
Argoverse 2 dataset에서 4D semantic occupancy completion 및 forecasting task의 state-of-the-art 성능을 달성했고, LiDAR point cloud forecasting으로의 transfer에서도 Argoverse 4D occupancy forecasting challenge에서 모든 baselines 대비 first를 기록했다.

## 초록 (원문)
We present DIO, a flexible world model that can estimate the scene occupancy-flow from a sparse set of LiDAR observations, and decompose it into individual instances. DIO can not only complete instance shapes at the present time, but also forecast their occupancy-flow evolution over a future horizon. Thanks to its flexible prompt representation, DIO can take instance prompts from off-the-shelf models like 3D detectors, achieving state-of-the-art performance in the task of 4D semantic occupancy completion and forecasting on the Argoverse 2 dataset. Moreover, our world model can easily and effectively be transferred to downstream tasks like LiDAR point cloud forecasting, ranking first compared to all baselines in the Argoverse 4D occupancy forecasting challenge.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
