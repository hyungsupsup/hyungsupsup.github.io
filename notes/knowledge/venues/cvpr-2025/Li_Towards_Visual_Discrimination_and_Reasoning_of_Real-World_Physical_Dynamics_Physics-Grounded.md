---
title: "Towards Visual Discrimination and Reasoning of Real-World Physical Dynamics: Physics-Grounded Anomaly Detection"
tags: [cvpr2025, dataset-benchmark, embodied-perception]
venue: CVPR 2025
arxiv: "2503.03562"
citations: 14
auto: true
---

> **TL;DR** 로봇 팔과 모터로 수집한 실제 물리 동역학 기반 산업 이상 탐지 비디오 데이터셋 Phys-AD와 물리적 원인 설명 평가 지표 PAEval을 제안한 논문이다.

**CVPR 2025** · Wenqiao Li, Yao Gu, Xintao Chen, Xiaohao Xu, Ming Hu, Xiaonan Huang 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Towards_Visual_Discrimination_and_Reasoning_of_Real-World_Physical_Dynamics_Physics-Grounded_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.03562) · 인용 14회

**주제:** Dataset & Benchmark · Embodied Perception

## 문제
기존 Industrial Anomaly Detection(IAD) 알고리즘은 정적이고 의미적으로 단순한 데이터셋에서 개발·평가되어, 물리적 이해와 추론이 필요한 실제 환경과 괴리가 있다.

## 핵심 아이디어
실제 로봇 팔과 모터를 사용해 수집한 최초의 대규모 실제 물리 기반 비디오 이상 탐지 데이터셋 Phys-AD를 제안하고, 이상 탐지뿐 아니라 물리적 원인 설명 능력을 평가하는 PAEval 지표를 도입한다.

## 방법
Phys-AD는 22개 실제 객체 범주에 걸쳐 6400개 이상의 비디오와 47종의 이상 유형을 포함하며, 로봇 팔 및 모터와의 상호작용에서 발생하는 동적이고 의미적으로 풍부한 장면을 제공한다. 이 데이터셋에서 unsupervised AD, weakly-supervised AD, video-understanding AD의 세 설정으로 최신 이상 탐지 방법들을 벤치마크한다. 또한 PAEval은 visual-language foundation model이 이상을 탐지하고 그 물리적 원인을 정확히 설명하는 능력을 평가하도록 설계되었다.

## 결과
벤치마크는 최신 방법들이 물리 기반 이상을 처리하는 데 한계가 있음을 보여주며, PAEval을 통해 visual-language foundation model의 탐지 및 물리적 원인 설명 능력을 평가한다.

## 초록 (원문)
Humans detect real-world object anomalies by perceiving, interacting, and reasoning based on object-conditioned physical knowledge. The long-term goal of Industrial Anomaly Detection (IAD) is to enable machines to autonomously replicate this skill. However, current IAD algorithms are largely developed and tested on static, semantically simple datasets, which diverge from real-world scenarios where physical understanding and reasoning are essential.To bridge this gap, we introduce the Physics Anomaly Detection (Phys-AD) dataset, the first large-scale, real-world, physics-grounded video dataset for industrial anomaly detection. Collected using a real robot arm and motor, Phys-AD provides a diverse set of dynamic, semantically rich scenarios. The dataset includes more than 6400 videos across 22 real-world object categories, interacting with robot arms and motors, and exhibits 47 types of anomalies. Anomaly detection in Phys-AD requires visual reasoning, combining both physical knowledge and video content to determine object abnormality.We benchmark state-of-the-art anomaly detection methods under three settings: unsupervised AD, weakly-supervised AD, and video-understanding AD, highlighting their limitations in handling physics-grounded anomalies. Additionally, we introduce the Physics Anomaly Explanation (PAEval) metric, designed to assess the ability of visual-language foundation models to not only detect anomalies but also provide accurate explanations for their underlying physical causes. Our project is available at https://guyao2023.github.io/Phys-AD/.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
