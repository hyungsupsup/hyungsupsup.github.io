---
title: "GEM: A Generalizable Ego-Vision Multimodal World Model for Fine-Grained Ego-Motion, Object Dynamics, and Scene Composition Control"
tags: [cvpr2025, world-model, autonomous-driving, embodied-perception]
venue: CVPR 2025
arxiv: "2412.11198"
citations: 95
auto: true
---

> **TL;DR** GEM은 reference frame, sparse features, human poses, ego-trajectories를 이용해 미래 프레임을 예측하는 일반화 가능한 ego-vision multimodal world model이다.

**CVPR 2025** · Mariam Hassan, Sebastian Stapf, Ahmad Rahimi, Pedro M B Rezende, Yasaman Haghighi, David Brüggemann 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Hassan_GEM_A_Generalizable_Ego-Vision_Multimodal_World_Model_for_Fine-Grained_Ego-Motion_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2412.11198) · 인용 95회

**주제:** World Model · Autonomous Driving · Embodied Perception

## 문제
기존 world model은 object dynamics, ego-agent motion, human poses를 세밀하게 제어하면서 장기간 일관된 미래를 생성하는 데 한계가 있다.

## 핵심 아이디어
GEM은 ego-trajectory와 human pose, sparse features를 조건으로 사용해 object dynamics와 ego-motion, human poses를 명시적으로 제어하고 RGB와 depth를 함께 생성한다.

## 방법
Reference frame과 sparse features, human poses, ego-trajectories를 입력으로 받아 미래 프레임의 RGB와 depth를 예측한다. 장기 생성의 안정성을 위해 autoregressive noise schedules를 도입하고, autonomous driving, egocentric human activities, drone flights 등 4000+ hours의 multimodal 데이터를 사용한다. Depth maps, ego-trajectories, human poses는 pseudo-label로 얻는다.

## 결과
GEM은 diverse, controllable scenarios와 long generations에서의 temporal consistency를 잘 생성하며, controllability 평가를 위해 새로운 Control of Object Manipulation (COM) metric을 포함한 평가 프레임워크를 제시한다.

## 연결
- **기반 대표 논문:** Dreamer (v1), UniSim — [[knowledge/map|분야 지도]]

## 초록 (원문)
We present GEM, a Generalizable Ego-vision Multimodal world model that predicts future frames using a reference frame, sparse features, human poses, and ego-trajectories. Hence, our model has precise control over object dynamics, ego-agent motion and human poses. GEM generates paired RGB and depth outputs for richer spatial understanding. We introduce autoregressive noise schedules to enable stable long-horizon generations. Our dataset is comprised of 4000+ hours of multimodal data across domains like autonomous driving, egocentric human activities, and drone flights. Pseudo-labels are used to get depth maps, ego-trajectories, and human poses. We use a comprehensive evaluation framework, including a new Control of Object Manipulation (COM) metric, to assess controllability. Experiments show GEM excels at generating diverse, controllable scenarios and temporal consistency over long generations. Code, models, and datasets are fully open-sourced.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
