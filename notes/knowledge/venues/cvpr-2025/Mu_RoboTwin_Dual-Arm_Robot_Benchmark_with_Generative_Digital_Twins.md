---
title: "RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins"
tags: [cvpr2025, dataset-benchmark, manipulation, simulation-sim2real]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** RoboTwin은 3D 생성 모델과 LLM을 활용해 양팔 로봇용 다양한 전문가 데이터셋과 실제 정렬 평가 벤치마크를 생성하는 프레임워크이다.

**CVPR 2025** · Yao Mu, Tianxing Chen, Zanxin Chen, Shijia Peng, Zhiqian Lan, Zeyu Gao 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Mu_RoboTwin_Dual-Arm_Robot_Benchmark_with_Generative_Digital_Twins_CVPR_2025_paper.html)

**주제:** Dataset & Benchmark · Manipulation · Simulation & Sim2Real

## 문제
양팔 협응 및 복잡한 물체 조작 연구에 필요한 다양하고 고품질인 시연 데이터와 실제 환경에 정렬된 평가 벤치마크가 부족하다.

## 핵심 아이디어


## 방법
RoboTwin은 3D 생성 기반 모델로 현실적이고 상호작용 가능한 객체 디지털 트윈과 시나리오를 만든다. 또한 공간 관계 인식 코드 생성 프레임워크가 작업을 분해하고 공간 제약을 결정하여 로봇 이동 코드를 생성한다. 이를 통해 시뮬레이션과 실제 데이터를 포함한 표준화된 평가 벤치마크를 제공한다.

## 결과
COBOT Magic Robot 플랫폼에서 검증했으며, RoboTwin 생성 데이터로 사전학습 후 제한된 실제 샘플로 미세조정한 정책은 실제 데이터만 학습한 모델 대비 단일팔 작업에서 70% 이상, 양팔 작업에서 40% 이상 성공률 향상을 보였다.

## 초록 (원문)
In the rapidly advancing field of robotics, dual-arm coordination and complex object manipulation are essential capabilities for developing advanced autonomous systems. However, the scarcity of diverse, high-quality demonstration data and real-world-aligned evaluation benchmarks severely limits such development. To address this, we introduce RoboTwin, a generative digital twin framework that uses 3D generative foundation models and large language models to produce diverse expert datasets and provide a real-world-aligned evaluation platform for dual-arm robotic tasks. Specifically, RoboTwin creates varied digital twins of objects from single 2D images, generating realistic and interactive scenarios. It also introduces a spatial relation-aware code generation framework that combines object annotations with large language models to break down tasks, determine spatial constraints, and generate precise robotic movement code. Our framework offers a comprehensive benchmark with both simulated and real-world data, enabling standardized evaluation and better alignment between simulated training and real-world performance. We validated our approach using the open-source COBOT Magic Robot platform. Policies pre-trained on RoboTwin-generated data and fine-tuned with limited real-world samples demonstrate significant potential for enhancing dual-arm robotic manipulation systems by improving success rates by over 70% for single-arm tasks and over 40% for dual-arm tasks compared to models trained solely on real-world data.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
