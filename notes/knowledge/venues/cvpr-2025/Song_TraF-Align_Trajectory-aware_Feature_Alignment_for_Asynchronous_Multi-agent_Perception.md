---
title: "TraF-Align: Trajectory-aware Feature Alignment for Asynchronous Multi-agent Perception"
tags: [cvpr2025, autonomous-driving, embodied-perception]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** TraF-Align은 협력 인지에서 에이전트 간 지연으로 생기는 공간·의미 불일치를 feature trajectory 예측과 정렬로 보정하는 프레임워크다.

**CVPR 2025** · Zhiying Song, Lei Yang, Fuxi Wen, Jun Li
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Song_TraF-Align_Trajectory-aware_Feature_Alignment_for_Asynchronous_Multi-agent_Perception_CVPR_2025_paper.html)

**주제:** Autonomous Driving · Embodied Perception

## 문제
협력 인지에서 차량 간 통신 지연으로 인해 ego vehicle의 실시간 관측과 다른 차량의 지연된 데이터 사이에 공간적·의미적 feature 불일치가 발생해 융합이 어려워진다.

## 핵심 아이디어
객체의 feature-level trajectory를 과거 관측부터 ego vehicle의 현재 시점까지 예측하고, 그 경로를 따라 시간 순서의 sampling point를 생성해 현재 query가 관련 과거 feature에 attention하도록 한다.

## 방법
TraF-Align은 feature 흐름 경로를 학습해 객체의 feature trajectory를 예측한다. 이 경로상의 temporally ordered sampling point를 이용해 현재 시점 query를 historical feature와 연결하고, 이를 통해 현재 시점 feature를 재구성하며 여러 프레임 간 semantic interaction을 촉진한다. 그 결과 공간적 misalignment를 보정하고 에이전트 간 semantic consistency를 유지한다.

## 결과
V2V4Real과 DAIR-V2X-Seq 두 real-world dataset 실험에서 TraF-Align이 asynchronous cooperative perception의 새로운 benchmark를 설정했다고 보고한다.

## 초록 (원문)
Cooperative perception presents significant potential for enhancing the sensing capabilities of individual vehicles, however, inter-agent latency remains a critical challenge. Latencies cause misalignments in both spatial and semantic features, complicating the fusion of real-time observations from the ego vehicle with delayed data from others. To address these issues, we propose TraF-Align, a novel framework that learns the flow path of features by predicting the feature-level trajectory of objects from past observations up to the ego vehicle's current time. By generating temporally ordered sampling points along these paths, TraF-Align directs attention from the current-time query to relevant historical features along each trajectory, supporting the reconstruction of current-time features and promoting semantic interaction across multiple frames. This approach corrects spatial misalignment and ensures semantic consistency across agents, effectively compensating for motion and achieving coherent feature fusion. Experiments on two real-world datasets, V2V4Real and DAIR-V2X-Seq, show that TraF-Align sets a new benchmark for asynchronous cooperative perception.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
