---
title: "MAGiC-SLAM: Multi-Agent Gaussian Globally Consistent SLAM"
tags: [cvpr2025, embodied-perception, autonomous-driving]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** MAGiC-SLAM은 rigidly deformable 3D Gaussian 표현을 사용해 multi-agent SLAM의 속도와 정확도를 개선한 시스템이다.

**CVPR 2025** · Vladimir Yugay, Theo Gevers, Martin R. Oswald
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Yugay_MAGiC-SLAM_Multi-Agent_Gaussian_Globally_Consistent__SLAM_CVPR_2025_paper.html)

**주제:** Embodied Perception · Autonomous Driving

## 문제
기존 novel view synthesis 가능 SLAM은 single-agent에 제한되고, 최근 distributed neural scene 기반 방법은 느리고 real-world 데이터를 정확히 렌더링하지 못하며 두 agent로 제한되고 tracking 정확도가 낮다.

## 핵심 아이디어
rigidly deformable 3D Gaussian 기반 scene representation을 도입해 시스템을 크게 빠르게 하면서, 새로운 tracking 및 map-merging 메커니즘과 loop closure를 Gaussian SLAM pipeline에 통합한다.

## 방법
여러 agent의 관측으로부터 3D Gaussian scene representation을 구성하고, trajectory drift와 agent 간 관측 불일치를 다루기 위한 tracking 및 map-merging을 수행한다. 또한 loop closure를 Gaussian 기반 SLAM pipeline에 통합해 globally consistent map을 재구성한다.

## 결과
합성 및 real-world 데이터셋에서 평가한 결과, MAGiC-SLAM은 state of the art보다 더 정확하고 빠르다.

## 초록 (원문)
Simultaneous localization and mapping (SLAM) systems with novel view synthesis capabilities are widely used in computer vision, with applications in augmented reality, robotics, and autonomous driving. However, existing approaches are limited to single-agent operation. Recent work has addressed this problem using a distributed neural scene representation. Unfortunately, existing methods are slow, cannot accurately render real-world data, are restricted to two agents, and have limited tracking accuracy. In contrast, we propose a rigidly deformable 3D Gaussian-based scene representation that dramatically speeds up the system. However, improving tracking accuracy and reconstructing a globally consistent map from multiple agents remains challenging due to trajectory drift and discrepancies across agents' observations. Therefore, we propose new tracking and map-merging mechanisms and integrate loop closure in the Gaussian-based SLAM pipeline. We evaluate \ours on synthetic and real-world datasets and find it more accurate and faster than the state of the art.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
