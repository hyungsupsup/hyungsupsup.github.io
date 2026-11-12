---
title: "Tartan IMU: A Light Foundation Model for Inertial Positioning in Robotics"
tags: [cvpr2025, embodied-perception, other]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** Tartan IMU는 다양한 로봇 플랫폼에서 일반화 가능한 IMU 기반 상태 추정을 위한 경량 foundation model이다.

**CVPR 2025** · Shibo Zhao, Sifan Zhou, Raphael Blanchard, Yuheng Qiu, Wenshan Wang, Sebastian Scherer
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_Tartan_IMU_A_Light_Foundation_Model_for_Inertial_Positioning_in_CVPR_2025_paper.html)

**주제:** Embodied Perception · Other

## 문제
기존 learning IMU odometry는 특정 데이터셋에 학습되어 일반화가 부족하고 overfitting에 취약해 실제 로봇 적용이 제한된다.

## 핵심 아이디어
100시간 이상의 multi-platform 데이터로 일반 운동 지식을 학습한 foundation model에 LoRA와 online test-time adaptation을 결합해 unseen task 적응과 실시간 운용 중 학습을 가능하게 한다.

## 방법
3단계로, 먼저 multi-platform 데이터로 pre-trained foundation model을 구축하고, LoRA로 1.1 M trainable parameters만으로 새로운 task에 positive transfer하며, online test-time adaptation으로 training/testing 경계를 없애 200 FPS real-time으로 운용 중 지속 학습한다.

## 결과
pre-trained model은 specialized models 대비 ATE에서 36% 개선을 달성했고, LoRA는 1.1 M trainable parameters로 적응하며, online adaptation은 200 FPS real-time 동작을 지원한다.

## 초록 (원문)
Despite recent advances in deep learning, most existing learning IMU odometry methods are trained on specific datasets, lack generalization, and are prone to overfitting, which limits their real-world application. To address these challenges, we present Tartan IMU, a foundation model designed for generalizable, IMU-based state estimation across diverse robotic platforms. Our approach consists of three-stage: First, a pre-trained foundation model leverages over 100 hours of multi-platform data to establish general motion knowledge, achieving 36% improvement in ATE over specialized models. Second, to adapt to previously unseen tasks, we employ the Low-Rank Adaptation (LoRA), allowing positive transfer with only 1.1 M trainable parameters. Finally, to support robotics deployment, we introduce online test-time adaptation, which eliminates the boundary between training and testing, allowing the model to continuously "learn as it operates" at 200 FPS in real-time.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
