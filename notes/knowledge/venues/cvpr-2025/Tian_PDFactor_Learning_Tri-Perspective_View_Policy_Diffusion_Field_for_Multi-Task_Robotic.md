---
title: "PDFactor: Learning Tri-Perspective View Policy Diffusion Field for Multi-Task Robotic Manipulation"
tags: [cvpr2025, vla, manipulation, imitation-learning]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** PDFactor는 triplane 기반 latent diffusion field로 6-DoF action 분포를 모델링해 multi-task robotic manipulation을 수행하는 프레임워크다.

**CVPR 2025** · Jingyi Tian, Le Wang, Sanping Zhou, Sen Wang, Jiayi Li, Haowen Sun 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Tian_PDFactor_Learning_Tri-Perspective_View_Policy_Diffusion_Field_for_Multi-Task_Robotic_CVPR_2025_paper.html)

**주제:** VLA · Manipulation · Imitation Learning

## 문제
시각 관찰과 자연어 지시를 이용한 로봇 조작에서 기존 explicit/implicit action 분포 모델은 정확도와 효율성 사이의 trade-off를 달성하기 어렵다.

## 핵심 아이디어
3D point cloud를 세 개의 orthogonal feature plane으로 분해하고 tri-perspective view transformer로 observation space에 정렬된 dense cubic features를 생성해 임의 위치의 6-DoF action probability distribution을 나타내는 latent diffusion field를 만든다.

## 방법
PDFactor는 point cloud를 세 orthogonal plane으로 투영하고 tri-perspective view transformer를 통해 dense cubic features를 latent diffusion field로 생성한다. 작은 denoising network를 parameterized loss function이자 action gradient decoder로 사용해 inference 시 latent diffusion field에서 action을 샘플링한다. 이를 통해 explicit representation의 spatial awareness와 implicit representation의 arbitrary resolution을 함께 활용한다.

## 결과
RLBench simulation의 다양한 manipulation task에서 state-of-the-art 접근법을 능가하며, 제한된 수의 human demonstrations로부터 multi-task policies를 효과적으로 학습해 다양한 real-world manipulation task에서 promising accuracy를 달성한다.

## 초록 (원문)
Robotic manipulation based on visual observations and natural language instructions is a long-standing challenge in robotics. Yet prevailing approaches model action distribution by adopting explicit or implicit representations, which often struggle to achieve a trade-off between accuracy and efficiency. In response, we propose PDFactor, a novel framework that models action distribution with a hybrid triplane representation. In particular, PDFactor decomposes 3D point cloud into three orthogonal feature planes and leverages a tri-perspective view transformer to produce dense cubic features as a latent diffusion field aligned with observation space representing 6-DoF action probability distribution at an arbitrary location. We employ a small denoising network conceptually as both a parameterized loss function measuring the quality of the learned latent features and an action gradient decoder to sample actions from the latent diffusion field during inference. This design enables our PDFactor to benefit from spatial awareness of explicit representation and arbitrary resolution of implicit representation, rendering it with manipulation accuracy, inference efficiency, and model scalability. Experiments demonstrate that PDFactor outperforms state-of-the-art approaches across a diverse range of manipulation tasks in RLBench simulation. Moreover, PDFactor can effectively learn multi-task policies from a limited number of human demonstrations, achieving promising accuracy in a variety of real-world manipulation tasks.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
