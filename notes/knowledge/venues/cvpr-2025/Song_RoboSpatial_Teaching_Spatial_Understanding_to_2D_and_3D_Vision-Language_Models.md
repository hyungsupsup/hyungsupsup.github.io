---
title: "RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics"
tags: [cvpr2025, dataset-benchmark, embodied-perception, manipulation]
venue: CVPR 2025
arxiv: "2411.16537"
citations: 233
auto: true
---

> **TL;DR** RoboSpatial은 로봇의 공간 이해를 위해 2D egocentric 이미지와 3D 스캔을 함께 제공하는 대규모 데이터셋이다.

**CVPR 2025** · Chan Hee Song, Valts Blukis, Jonathan Tremblay, Stephen Tyree, Yu Su, Stan Birchfield
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Song_RoboSpatial_Teaching_Spatial_Understanding_to_2D_and_3D_Vision-Language_Models_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2411.16537) · 인용 233회

**주제:** Dataset & Benchmark · Embodied Perception · Manipulation

## 문제
기존 vision-language model은 일반 목적 이미지 데이터로 학습되어 ego-, world-, object-centric 기준틀 이해 등 로봇에 필요한 정교한 공간 추론에 어려움을 겪는다.

## 핵심 아이디어
실내 및 tabletop 장면의 2D egocentric 이미지와 3D 스캔을 결합하고 풍부한 공간 관계를 주석한 RoboSpatial 데이터셋을 제안한다.

## 방법
RoboSpatial은 1M images, 5k 3D scans, 3M annotated spatial relationships로 구성되며, 2D 이미지와 3D 스캔을配对해 2D와 3D 모두에 활용 가능하게 한다. 이 데이터로 학습한 모델은 공간 이해 기반 작업에 사용된다.

## 결과
RoboSpatial로 학습한 모델은 spatial affordance prediction, spatial relationship prediction, robotics manipulation과 같은 downstream 작업에서 baseline을 능가한다.

## 연결
- **기반 대표 논문:** Code as Policies, Octo, Open X-Embodiment (데이터셋), OpenVLA, RT-2, SayCan — [[knowledge/map|분야 지도]]

## 초록 (원문)
Spatial understanding is a crucial capability that enables robots to perceive their surroundings, reason about their environment, and interact with it meaningfully. In modern robotics, these capabilities are increasingly provided by vision-language models. However, these models face significant challenges in spatial reasoning tasks, as their training data are based on general-purpose image datasets that often lack sophisticated spatial understanding. For example, datasets frequently do not capture reference frame comprehension, yet effective spatial reasoning requires understanding whether to reason from ego-, world-, or object-centric perspectives. To address this issue, we introduce RoboSpatial, a large-scale dataset for spatial understanding in robotics. It consists of real indoor and tabletop scenes, captured as 3D scans and egocentric images, and annotated with rich spatial information relevant to robotics. The dataset includes 1M images, 5k 3D scans, and 3M annotated spatial relationships, and the pairing of 2D egocentric images with 3D scans makes it both 2Dand 3Dready. Our experiments show that models trained with RoboSpatial outperform baselines on downstream tasks such as spatial affordance prediction, spatial relationship prediction, and robotics manipulation.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
