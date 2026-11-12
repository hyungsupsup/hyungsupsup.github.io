---
title: "RoboSense: Large-scale Dataset and Benchmark for Egocentric Robot Perception and Navigation in Crowded and Unstructured Environments"
tags: [cvpr2025, dataset-benchmark, embodied-perception, navigation]
venue: CVPR 2025
arxiv: "2408.15503"
citations: 16
auto: true
---

> **TL;DR** RoboSense는 Camera, LiDAR, Fisheye 센서 기반의 egocentric 로봇 인식 및 navigation을 위한 대규모 multimodal dataset과 benchmark를 제안한다.

**CVPR 2025** · Haisheng Su, Feixiang Song, Cong Ma, Wei Wu, Junchi Yan
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Su_RoboSense_Large-scale_Dataset_and_Benchmark_for_Egocentric_Robot_Perception_and_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2408.15503) · 인용 16회

**주제:** Dataset & Benchmark · Embodied Perception · Navigation

## 문제
군중 및 비정형 환경에서 truncation과 occlusion으로 인해 near-field egocentric perception 성능이 부족하며, 이를 위한 대규모 로봇 중심 데이터가 부족하다.

## 핵심 아이디어
자율주행 데이터와 달리 near-field 주변 장애물에 초점을 맞춘 egocentric multi-sensor 수집 플랫폼과 360° view annotation을 갖춘 RoboSense dataset을 구축하고, near-field 3D perception 및 prediction을 위한 새로운 matching criterion을 정의한다.

## 방법
Camera, LiDAR, Fisheye의 3가지 센서로 유연한 구성이 가능한 egocentric multi-sensor 수집 플랫폼을 구축한다. RoboSense는 360° view에서 3D bounding box와 ID가 annotation된 동기화 데이터와 trajectory를 포함하며, 이를 기반으로 6개의 task를 정식화하고 분석 및 benchmark를 제공한다.

## 결과
RoboSense는 133K 이상의 synchronized data, 1.4M 3D bounding box 및 IDs, 216K trajectories, 7.6K temporal sequences를 포함하고, near range 주변 장애물 annotation이 KITTI와 nuScenes보다 각각 270x, 18x 많다.

## 초록 (원문)
Reliable embodied perception from an egocentric perspective is challenging yet essential for autonomous navigation technology of intelligent mobile agents. With the growing demand of social robotics, near-field scene understanding becomes an important research topic in the areas of egocentric perceptual tasks related to navigation in both crowded and unstructured environments. Due to the complexity of environmental conditions and difficulty of surrounding obstacles owing to truncation and occlusion, the perception capability under this circumstance is still inferior. To further enhance the intelligence of mobile robots, in this paper, we setup an egocentric multi-sensor data collection platform based on 3 main types of sensors (Camera, LiDAR and Fisheye), which supports flexible sensor configurations to enable dynamic sight of view from ego-perspective, capturing either near or farther areas. Meanwhile, a large-scale multimodal dataset is constructed, named RoboSense, to facilitate egocentric robot perception. Specifically, RoboSense contains more than 133K synchronized data with 1.4M 3D bounding box and IDs annotated in the full 360^ \circ view, forming 216K trajectories across 7.6K temporal sequences. It has 270xand 18xas many annotations of surrounding obstacles within near ranges as the previous datasets collected for autonomous driving scenarios such as KITTI and nuScenes. Moreover, we define a novel matching criterion for near-field 3D perception and prediction metrics. Based on RoboSense, we formulate 6 popular tasks to facilitate the future research development, where the detailed analysis as well as benchmarks are also provided accordingly. Data desensitization measures have been conducted for privacy protection.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
