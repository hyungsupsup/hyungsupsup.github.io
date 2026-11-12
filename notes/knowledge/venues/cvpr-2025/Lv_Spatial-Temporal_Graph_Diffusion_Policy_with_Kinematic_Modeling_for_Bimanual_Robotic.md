---
title: "Spatial-Temporal Graph Diffusion Policy with Kinematic Modeling for Bimanual Robotic Manipulation"
tags: [cvpr2025, imitation-learning, manipulation]
venue: CVPR 2025
arxiv: "2503.10743"
citations: 41
auto: true
---

> **TL;DR** KStar Diffuser는 양팔 로봇 조작을 위해 공간-시간 그래프와 미분 가능한 kinematics를 결합한 diffusion policy를 제안한다.

**CVPR 2025** · Qi Lv, Hao Li, Xiang Deng, Rui Shao, Yinchuan Li, Jianye Hao 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Lv_Spatial-Temporal_Graph_Diffusion_Policy_with_Kinematic_Modeling_for_Bimanual_Robotic_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.10743) · 인용 41회

**주제:** Imitation Learning · Manipulation

## 문제
기존 양팔 imitation learning은 먼 next-best end-effector pose를 예측한 뒤 inverse kinematics로 관절 각도를 계산하지만, 로봇의 물리적 구조를 고려하지 않아 self-collision이나 interference가 발생할 수 있고 kinematics 제약을 무시해 예측 pose가 실제 관절 한계를 벗어날 수 있다.

## 핵심 아이디어
연속 timestep의 양팔 관절 운동에 따라 dynamic spatial-temporal graph를 구성해 robot-structure condition으로 action denoising에 활용하고, differentiable kinematics로 NBP 학습 목표를 kinematics-aware하게 정규화한다.

## 방법
KStar Diffuser는 physical bimanual joint motions에 따라 dynamic spatial-temporal graph를 유지하며 이를 조건으로 diffusion denoising을 통해 action을 예측한다. 또한 differentiable kinematics를 도입해 next end-effector pose 예측이 kinematics 제약과 일관되도록 최적화 reference를 제공한다.

## 결과
시뮬레이션과 real-world 실험에서 물리적 구조 정보를 효과적으로 활용하고 kinematics-aware action을 생성함을 보인다.

## 연결
- **기반 대표 논문:** ACT / ALOHA, DDPM, Diffusion Policy, Mobile ALOHA, Octo, OpenVLA, RT-1, RT-2, UMI — Universal Manipulation Interface — [[knowledge/map|분야 지도]]

## 초록 (원문)
Despite the significant success of imitation learning in robotic manipulation, its application to bimanual tasks remains highly challenging. Existing approaches mainly learn a policy to predict a distant next-best end-effector pose (NBP) and then compute the corresponding joint rotation angles for motion using inverse kinematics. However, they suffer from two important issues: (1) rarely considering the physical robotic structure , which may cause self-collisions or interferences, and (2) overlooking the kinematics constraint , which may result in the predicted poses not conforming to the actual limitations of the robot joints. In this paper, we propose Kinematics enhanced Spatial-TemporAl gRaph Diffuser (KStar Diffuser). Specifically, (1)to incorporate the physical robot structure information into action prediction, KStar Diffuser maintains a dynamic spatial-temporal graph according to the physical bimanual joint motions at continuous timesteps. This dynamic graph serves as the robot-structure condition for denoising the actions; (2) to make the NBP learning objective consistent with kinematics, we introduce the differentiable kinematics to provide the reference for optimizing KStar Diffuser. This module regularizes the policy to predict more reliable and kinematics-aware next end-effector poses. Experimental results show that our method effectively leverages the physical structural information and generates kinematics-aware actions in both simulation and real-world.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
