---
title: "3D-MVP: 3D Multiview Pretraining for Manipulation"
tags: [cvpr2025, manipulation, embodied-perception]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** 3D-MVP는 RVT의 visual encoder를 대규모 3D 데이터로 masked autoencoding pretraining하여 로봇 manipulation 정책의 일반화를 향상시키는 방법이다.

**CVPR 2025** · Shengyi Qian, Kaichun Mo, Valts Blukis, David F. Fouhey, Dieter Fox, Ankit Goyal
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Qian_3D-MVP_3D_Multiview_Pretraining_for_Manipulation_CVPR_2025_paper.html)

**주제:** Manipulation · Embodied Perception

## 문제
기존 egocentric 데이터 기반 MAE pretraining은 2D 이미지만 사용하므로, 3D 장면 이해가 필요한 로봇 manipulation 응용에 충분하지 않다.

## 핵심 아이디어
RVT의 multi-view transformer를 visual encoder와 action decoder로 분리하고, visual encoder를 Objaverse 같은 대규모 3D 데이터에서 masked autoencoding으로 pretraining한다.

## 방법
RVT는 multi-view transformer로 3D 장면을 이해하고 gripper pose action을 예측한다. 3D-MVP는 이 구조를 visual encoder와 action decoder로 나눈 뒤, visual encoder만 3D 데이터에서 masked autoencoding으로 pretraining한다. 이후 가상 robot manipulation task들에서 평가한다.

## 결과
가상 robot manipulation task suite에서 baselines 대비 향상된 성능을 보였으며, 3D-aware pretraining이 vision-based robotic manipulation 정책의 일반화를 개선하는 유망한 접근임을 시사한다.

## 초록 (원문)
Recent works have shown that visual pretraining on egocentric datasets using masked autoencoders (MAE) can improve generalization for downstream robotics tasks. However, these approaches pretrain only on 2D images, while many robotics applications require 3D scene understanding. In this work, we propose 3D-MVP, a novel approach for 3D Multi-View Pretraining using masked autoencoders. We leverage Robotic View Transformer (RVT), which uses a multi-view transformer to understand the 3D scene and predict gripper pose actions. We split RVT's multi-view transformer into visual encoder and action decoder, and pretrain its visual encoder using masked autoencoding on large-scale 3D datasets such as Objaverse. We evaluate 3D-MVP on a suite of virtual robot manipulation tasks and demonstrate improved performance over baselines. Our results suggest that 3D-aware pretraining is a promising approach to improve generalization of vision-based robotic manipulation policies.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
