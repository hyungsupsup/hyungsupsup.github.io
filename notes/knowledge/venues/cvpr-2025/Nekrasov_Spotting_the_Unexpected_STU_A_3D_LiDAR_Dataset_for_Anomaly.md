---
title: "Spotting the Unexpected (STU): A 3D LiDAR Dataset for Anomaly Segmentation in Autonomous Driving"
tags: [cvpr2025, dataset-benchmark, autonomous-driving, embodied-perception]
venue: CVPR 2025
arxiv: "2505.02148"
citations: 18
auto: true
---

> **TL;DR** 자율주행 차량의 안전한 주행을 위해 LiDAR와 카메라, 시퀀스 정보를 포함한 3D 도로 이상 탐지/분할 데이터셋 STU를 제안하고 baseline을 평가한 논문이다.

**CVPR 2025** · Alexey Nekrasov, Malcolm Burdorf, Stewart Worrall, Bastian Leibe, Julie Stephany Berrio Perez
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Nekrasov_Spotting_the_Unexpected_STU_A_3D_LiDAR_Dataset_for_Anomaly_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2505.02148) · 인용 18회

**주제:** Dataset & Benchmark · Autonomous Driving · Embodied Perception

## 문제
자율주행 차량은 도로 위의 예상치 못한 물체나 이상을 탐지해야 하지만, 3D 이상 탐지 및 분할 연구는 2D에 비해 부족하고 기존 데이터셋은 AV에서 흔히 쓰이는 고품질 멀티모달 데이터를 갖추지 못했다.

## 핵심 아이디어
LiDAR와 카메라 데이터, 시퀀스 정보를 함께 포함하고 다양한 거리 범위에서 이상 탐지가 가능하도록 dense 3D semantic labeling을 제공하는 최초의 공개 도로 이상 분할 데이터셋을 제시한다.

## 방법
자율주행 시나리오에서 수집한 LiDAR 및 카메라 기반 멀티모달 데이터에 dense 3D semantic label과 sequential information을 구성한다. 여러 3D segmentation baseline 모델을 데이터셋에 맞게 적용 및 평가하여 3D anomaly detection의 어려움을 분석한다. 데이터셋과 평가 코드를 공개하여 다양한 접근법의 테스트와 성능 비교를 가능하게 한다.

## 결과
3D segmentation baseline 평가를 통해 자율주행 환경에서의 3D anomaly detection이 지닌 도전 과제를 부각했으며, 데이터셋과 평가 코드를 공개할 예정이다.

## 초록 (원문)
To operate safely, autonomous vehicles (AVs) need to detect and handle unexpected objects or anomalies on the road. While significant research exists for anomaly detection and segmentation in 2D, research progress in 3D is underexplored. Existing datasets lack high-quality multimodal data that are typically found in AVs. This paper presents a novel dataset for anomaly segmentation in driving scenarios. To the best of our knowledge, it is the first publicly available dataset focused on road anomaly segmentation with dense 3D semantic labeling, incorporating both LiDAR and camera data, as well as sequential information to enable anomaly detection across various ranges. This capability is critical for the safe navigation of autonomous vehicles. We adapted and evaluated several baseline models for 3D segmentation, highlighting the challenges of 3D anomaly detection in driving environments. Our dataset and evaluation code will be openly available, facilitating the testing and performance comparison of different approaches.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
