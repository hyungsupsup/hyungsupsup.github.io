---
title: "Let Humanoids Hike! Integrative Skill Development on Complex Trails"
tags: [cvpr2025, humanoid-locomotion, embodied-perception, navigation]
venue: CVPR 2025
arxiv: "2505.06218"
citations: 12
auto: true
---

> **TL;DR** LEGO-H는 시각 기반 humanoid가 복잡한 trail에서 미래 step을 예측하며 보행과 목표 지향 navigation을 통합해 hiking하도록 학습하는 framework이다.

**CVPR 2025** · Kwan-Yee Lin, Stella X. Yu
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_Let_Humanoids_Hike_Integrative_Skill_Development_on_Complex_Trails_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2505.06218) · 인용 12회

**주제:** Humanoid & Locomotion · Embodied Perception · Navigation

## 문제
기존 humanoid 연구는 locomotion의 motor skill과 semantic navigation이 분리되어 있어, 복잡한 trail에서 장기 목표와 상황 인식, 실제 embodiment 및 local terrain variability를 함께 다루지 못한다.

## 핵심 아이디어
Temporal Vision Transformer로 미래 step을 예측해 local movement와 goal-directed navigation을 통합하고, joint movement pattern의 latent representation과 hierarchical metric learning으로 privileged training에서 real-world training으로의 policy transfer를 가능하게 한다.

## 방법
LEGO-H는 vision을 가진 humanoid가 복잡한 trail을 독립적으로 hiking하도록 학습하는 framework이다. Temporal Vision Transformer가 미래 step을 예측해 locomotion을 guide하며, joint movement pattern의 latent representation과 hierarchical metric learning을 결합해 policy transfer를 수행한다. 이를 통해 predefined motion pattern 없이 다양한 physical 및 environmental challenge를 처리한다.

## 결과
다양한 simulated hiking trail과 서로 다른 morphology의 humanoid 실험에서 LEGO-H의 robustness와 versatility를 보였으며, 향후 humanoid 개발의 강한 기반을 마련했다.

## 연결
- **기반 대표 논문:** Domain Randomization (Tobin et al.), Isaac Gym, PPO — Proximal Policy Optimization, RMA — Rapid Motor Adaptation — [[knowledge/map|분야 지도]]

## 초록 (원문)
Hiking on complex trails demands balance, agility, and adaptive decision-making over unpredictable terrain. Current humanoid research remains fragmented and inadequate for hiking: locomotion focuses on motor skills without long-term goals or situational awareness, while semantic navigation overlooks real-world embodiment and local terrain variability. We propose training humanoids to hike on complex trails, fostering integrative skill development across visual perception, decision making, and motor execution. We develop LEGO-H, a learning framework that enables a humanoid with vision to hike complex trails independently. It has two key innovations. (1) A Temporal Vision Transformer anticipates future steps to guide locomotion, unifying local movement and goal-directed navigation. (2) Latent representations of joint movement patterns combined with hierarchical metric learning allow smooth policy transfer from privileged training to real-world training. These techniques enable LEGO-H to handle diverse physical and environmental challenges without relying on predefined motion patterns. Experiments on diverse simulated hiking trails and humanoids with different morphologies demonstrate LEGO-H's robustness and versatility, establishing a strong foundation for future humanoid development.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
