---
title: "Tra-MoE: Learning Trajectory Prediction Model from Multiple Domains for Adaptive Policy Conditioning"
tags: [cvpr2025, vla, imitation-learning, manipulation]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** Tra-MoE는 다양한 out-of-domain 데이터로 instruction-conditioned any-point trajectory prediction model을 학습하고 adaptive policy conditioning으로 robot policy를 guide하는 방법이다.

**CVPR 2025** · Jiange Yang, Haoyi Zhu, Yating Wang, Gangshan Wu, Tong He, Limin Wang
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_Tra-MoE_Learning_Trajectory_Prediction_Model_from_Multiple_Domains_for_Adaptive_CVPR_2025_paper.html)

**주제:** VLA · Imitation Learning · Manipulation

## 문제
단일 통합 로봇 시스템의 일반화를 위해 여러 domain 데이터를 활용하는 것이 중요하지만, diverse out-of-domain 분포를 처리하면서 policy에 유용한 trajectory guidance를 제공하는 것은 어렵다.

## 핵심 아이디어
sparse Top-1 gated MoE architecture로 parameter cooperation과 specialization을 balance하여 large-scale out-of-domain data를 활용하고, predicted trajectory에 대한 2D mask representation을 image observation과 align해 adaptive policy conditioning을 수행한다.

## 방법
Tra-MoE는 current frame에서 instruction이 주어지면 any-point trajectories를 예측하도록 학습되며, sparsely-gated MoE(Top-1 gating)로 token당 constant FLOPs를 유지한다. 예측된 trajectory는 2D mask representation으로 변환되어 image observation과 명시적으로 align되고, 이를 통해 action prediction을 더 flexible하게 guide한다. Simulation과 real-world scenario에서 실험을 수행한다.

## 결과
Simulation 및 real-world 실험에서 Tra-MoE와 adaptive policy conditioning의 효과를 검증했고, Tra-MoE는 dense baseline이 parameter count를 맞춰 scale된 경우에도 일관되게 superior performance를 보였다.

## 초록 (원문)
Learning from multiple domains is a primary factor that influences the generalization of a single unified robot system. In this paper, we aim to learn the trajectory prediction model by using broad out-of-domain data to improve its performance and generalization ability. Trajectory model is designed to predict any-point trajectories in the current frame given an instruction and can provide detailed control guidance for robotic policy learning. To handle the diverse out-of-domain data distribution, we propose a sparsely-gated MoE (Top-1 gating strategy) architecture for trajectory model, coined as Tra-MoE. The sparse activation design enables good balance between parameter cooperation and specialization, effectively benefiting from large-scale out-of-domain data while maintaining constant FLOPs per token. In addition, we further introduce an adaptive policy conditioning technique by learning 2D mask representations for predicted trajectories, which is explicitly aligned with image observations to guide action prediction more flexibly. We perform extensive experiments on both simulation and real-world scenarios to verify the effectiveness of Tra-MoE and adaptive policy conditioning technique. We also conduct a comprehensive empirical study to train Tra-MoE, demonstrating that our Tra-MoE consistently exhibits superior performance compared to the dense baseline model, even when the latter is scaled to match Tra-MoE's parameter count.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
