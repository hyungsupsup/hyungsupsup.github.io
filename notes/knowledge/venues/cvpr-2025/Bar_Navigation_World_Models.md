---
title: "Navigation World Models"
tags: [cvpr2025, world-model, navigation]
venue: CVPR 2025
arxiv: "2412.03572"
citations: 400
auto: true
---

> **TL;DR** Navigation World Model(NWM)은 과거 관측과 navigation action을 조건으로 미래 시각 관측을 예측하는 controllable video generation model로 navigation planning에 활용된다.

**CVPR 2025** · Amir Bar, Gaoyue Zhou, Danny Tran, Trevor Darrell, Yann LeCun
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Bar_Navigation_World_Models_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2412.03572) · 인용 400회

**주제:** World Model · Navigation

## 문제
기존 supervised navigation policy는 고정된 행동을 따르며 planning 중 제약 조건을 동적으로 반영하기 어렵다. 복잡한 환경 dynamics를 반영해 navigation trajectory를 예측하고 평가할 수 있는 모델이 필요하다.

## 핵심 아이디어
NWM은 past observation과 navigation action에 조건화된 controllable video generation을 통해 미래 visual observation을 예측하고, 이를 시뮬레이션하여 goal 달성 여부를 평가함으로써 navigation trajectory를 planning한다.

## 방법
Conditional Diffusion Transformer(CDiT)를 human과 robotic agent의 다양한 egocentric video로 학습하고 1 billion parameters로 확장한다. 익숙한 환경에서는 trajectory를 시뮬레이션해 goal 달성 여부를 평가하여 planning하며, external policy에서 샘플링한 trajectory를 ranking할 수도 있다. 또한 단일 입력 이미지로부터 학습된 visual prior를 활용해 낯선 환경의 trajectory를 상상한다.

## 결과
실험에서 from scratch planning과 external policy trajectory ranking 모두에서 효과성을 보였으며, 단일 입력 이미지로 낯선 환경의 trajectory를 상상할 수 있음을 보였다.

## 연결
- **기반 대표 논문:** DDPM, DINO-WM, Dreamer (v1), Genie, UniSim, World Models (Ha & Schmidhuber) — [[knowledge/map|분야 지도]]

## 초록 (원문)
Navigation is a fundamental skill of agents with visual-motor capabilities. We introduce a Navigation World Model (NWM), a controllable video generation model that predicts future visual observations based on past observations and navigation actions. To capture complex environment dynamics, NWM employs a Conditional Diffusion Transformer (CDiT), trained on a diverse collection of egocentric videos of both human and robotic agents, and scaled up to 1 billion parameters. In familiar environments, NWM can plan navigation trajectories by simulating them and evaluating whether they achieve the desired goal. Unlike supervised navigation policies with fixed behavior, NWM can dynamically incorporate constraints during planning. Experiments demonstrate its effectiveness in planning trajectories from scratch or by ranking trajectories sampled from an external policy. Furthermore, NWM leverages its learned visual priors to imagine trajectories in unfamiliar environments from a single input image, making it a flexible and powerful tool for next-generation navigation systems.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
