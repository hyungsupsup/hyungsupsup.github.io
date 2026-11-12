---
title: "Think Small, Act Big: Primitive Prompt Learning for Lifelong Robot Manipulation"
tags: [cvpr2025, manipulation, other]
venue: CVPR 2025
arxiv: "2504.00420"
citations: 25
auto: true
---

> **TL;DR** PPL은 재사용 및 확장 가능한 primitive prompt를 통해 평생 로봇 조작을 달성하는 방법이다.

**CVPR 2025** · Yuanqi Yao, Siao Liu, Haoming Song, Delin Qu, Qizhi Chen, Yan Ding 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Yao_Think_Small_Act_Big_Primitive_Prompt_Learning_for_Lifelong_Robot_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2504.00420) · 인용 25회

**주제:** Manipulation · Other

## 문제
기존 experience replay나 parameter-efficient 방법은 스킬 간에 공유되는 primitive를 활용하지 못해 지속적인 스킬 습득과 지식 전이에 한계가 있다.

## 핵심 아이디어
다중 스킬 사전학습에서 motion-aware primitive prompt를 학습하고, 새 스킬 학습 시 기존 pretrained prompt는 고정한 채 새 prompt를 결합·최적화해 지식을 전이한다.

## 방법
2단계 학습 scheme으로, 먼저 여러 스킬에서 semantic 및 motion shared primitive를 포착하는 primitive prompt 집합을 학습한다. 이후 lifelong span에서 새로운 prompt를 frozen pretrained prompt와 concatenate하여 최적화함으로써 old skill에서 new skill로의 knowledge transfer를 촉진한다.

## 결과
대규모 skill dataset을 구축하고 simulation과 real-world task에서 광범위한 실험을 수행하여 PPL이 state-of-the-art 방법보다 우수한 성능을 보임을 입증했다.

## 연결
- **기반 대표 논문:** LIBERO — [[knowledge/map|분야 지도]]

## 초록 (원문)
Learning a generalist robot that can effectively leverage prior knowledge for continuous skill acquisition remains significantly challenging. Despite the success of experience replay and parameter-efficient methods in maintaining knowledge across skills, naively applying these methods causes a failure to leverage the shared primitives between skills. To tackle these issues, we propose Primitive Prompt Learning (PPL), to achieve lifelong robot manipulation via reusable and extensible primitives. Within our two stage learning scheme, we first learn a set of primitive prompts to model primitives through multi-skills pre-training stage, where motion-aware prompts are learned to capture semantic and motion shared primitives across different skills. Secondly, when acquiring new skills in lifelong span, new prompts are concatenated and optimized with frozen pretrained prompts, boosting the learning via knowledge transfer from old skills to new ones. For evaluation, we construct a large-scale skill dataset and conduct extensive experiments in both simulation and real-world tasks, demonstrating PPL's superior performance over state-of-the-art methods.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
