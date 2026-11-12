---
title: "GENMANIP: LLM-driven Simulation for Generalizable Instruction-Following Manipulation"
tags: [cvpr2025, manipulation, simulation-sim2real, dataset-benchmark]
venue: CVPR 2025
arxiv: "2506.10966"
citations: 31
auto: true
---

> **TL;DR** GenManip은 LLM 기반 장면 그래프로 다양한 instruction-following manipulation task를 자동 생성하는 사실적 tabletop 시뮬레이션 플랫폼과 200개 시나리오의 GenManip-Bench를 제안한다.

**CVPR 2025** · Ning Gao, Yilun Chen, Shuai Yang, Xinyi Chen, Yang Tian, Hao Li 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Gao_GENMANIP_LLM-driven_Simulation_for_Generalizable_Instruction-Following_Manipulation_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2506.10966) · 인용 31회

**주제:** Manipulation · Simulation & Sim2Real · Dataset & Benchmark

## 문제
실제 환경의 로봇 manipulation은 일반화가 어렵지만, 기존 시뮬레이션 플랫폼은 다양한 instruction과 scenario에 대한 policy 적응을 충분히 탐구하지 못한다. 또한 instruction-following foundation model의 일반화 능력을 공정하게 비교할 환경이 부족하다.

## 핵심 아이디어
LLM-driven task-oriented scene graph를 이용해 10K annotated 3D object assets로 대규모의 diverse task를 자동 합성하는 파이프라인을 구축하고, human-in-the-loop 보정을 거친 200개 시나리오 benchmark로 일반화를 체계적으로 평가한다.

## 방법
GenManip은 tabletop simulation에서 LLM이 task-oriented scene graph를 생성해 다양한 manipulation task와 장면을 자동 구성한다. GenManip-Bench는 200개 시나리오로 modular manipulation system과 end-to-end policy를 비교 평가한다. Modular system은 foundation model을 perception, reasoning, planning에 통합하고, end-to-end policy는 scalable data collection으로 학습된다.

## 결과
실험 결과 data scaling은 end-to-end 방법에 이점을 주지만, foundation model을 결합한 modular system이 diverse scenario에서 더 효과적으로 일반화한다.

## 연결
- **기반 대표 논문:** ACT / ALOHA, Code as Policies, Domain Randomization (Tobin et al.), Isaac Gym, LIBERO, Mobile ALOHA, Octo, Open X-Embodiment (데이터셋), RT-1, RT-2, SimplerEnv — 시뮬레이션으로 실제 정책 평가 — [[knowledge/map|분야 지도]]

## 초록 (원문)
Robotic manipulation in real-world settings remains challenging, especially regarding robust generalization. Existing simulation platforms lack sufficient support for exploring how policies adapt to varied instructions and scenarios. Thus, they lag behind the growing interest in instruction-following foundation models like LLMs, whose adaptability is crucial yet remains underexplored in fair comparisons. To bridge this gap, we introduce GenManip, a realistic tabletop simulation platform tailored for policy generalization studies. It features an automatic pipeline via LLM-driven task-oriented scene graph to synthesize large-scale, diverse tasks using 10K annotated 3D object assets. To systematically assess generalization, we present GenManip-Bench, a benchmark of 200 scenarios refined via human-in-the-loop corrections. We evaluate two policy types: (1) modular manipulation systems integrating foundation models for perception, reasoning, and planning, and (2) end-to-end policies trained through scalable data collection. Results show that while data scaling benefits end-to-end methods, modular systems enhanced with foundation models generalize more effectively across diverse scenarios. We anticipate this platform to facilitate critical insights for advancing policy generalization in realistic conditions. All code will be made publicly available.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
