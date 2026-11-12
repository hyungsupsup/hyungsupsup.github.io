---
title: "Universal Actions for Enhanced Embodied Foundation Models"
tags: [cvpr2025, vla, simulation-sim2real]
venue: CVPR 2025
arxiv: "2501.10105"
citations: 117
auto: true
---

> **TL;DR** UniAct는 다양한 로봇의 이질적인 action space를 Universal Action Space로 통합해 cross-embodiment embodied foundation model을 가능하게 하는 프레임워크다.

**CVPR 2025** · Jinliang Zheng, Jianxiong Li, Dongxiu Liu, Yinan Zheng, Zhihao Wang, Zhonghong Ou 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Zheng_Universal_Actions_for_Enhanced_Embodied_Foundation_Models_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2501.10105) · 인용 117회

**주제:** VLA · Simulation & Sim2Real

## 문제
여러 로봇의 crowd-sourced embodied dataset은 물리적 embodiment와 제어 인터페이스가 달라 action space가 크게 이질적이므로, cross-embodiment data를 활용한 embodied foundation model 구축이 어렵다.

## 핵심 아이디어
로봇 간 공유되는 구조적 특징을 활용해 일반적인 행동을 포착하는 Universal Action Space를 학습하고, 여기에 embodiment-specific details를 더해 이질적인 실제 명령으로 빠르게 변환한다.

## 방법
UniAct는 Universal Action Space에서 동작하는 embodied foundation modeling 프레임워크로, 다양한 로봇의 universal action을 학습해 cross-domain data 활용과 cross-embodiment 일반화를 향상시킨다. 학습된 universal action은 embodiment-specific details를 추가하는 방식으로 각 로봇의 이질적인 actionable command로 효율적으로 변환되어 새 로봇에 빠르게 적응할 수 있다.

## 결과
0.5B 크기의 UniAct는 다양한 실제 및 simulation 로봇 평가에서 14X 더 큰 SOTA embodied foundation model들을 능가하며 뛰어난 cross-embodiment 제어 및 적응 능력을 보였다.

## 연결
- **기반 대표 논문:** ACT / ALOHA, BC-Z, DDPM, DROID (데이터셋), Diffusion Policy, Genie, LIBERO, Octo, Open X-Embodiment (데이터셋), OpenVLA, PaLM-E, RT-1, RT-2, SayCan — [[knowledge/map|분야 지도]]

## 초록 (원문)
Training on diverse, internet-scale data is a key factor in the success of recent large foundation models. Yet, using the same recipe for building embodied agents has faced noticeable difficulties. Despite the availability of many crowd-sourced embodied datasets, their action spaces often exhibit significant heterogeneity due to distinct physical embodiment and control interfaces for different robots, causing substantial challenges in developing embodied foundation models using cross-embodiment data. In this paper, we introduce UniAct, a new embodied foundation modeling framework operating in the Universal Action Space. Our learned universal actions capture the generic behaviors across diverse robots by exploiting their shared structural features, and enable enhanced cross-domain data utilization and cross-embodiment generalizations by eliminating the notorious heterogeneity. Moreover, the universal actions can be efficiently translated back to heterogeneous actionable commands by simply adding embodiment-specific details, from which fast adaptation to new robots becomes simple and straightforward. Our 0.5B instantiation of UniAct outperforms 14X larger SOTA embodied foundation models in extensive evaluations on various real-world and simulation robots, showcasing exceptional cross-embodiment control and adaptation capability, highlighting the crucial benefit of adopting universal actions.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
