---
title: "From Multimodal LLMs to Generalist Embodied Agents: Methods and Lessons"
tags: [cvpr2025, vla, reinforcement-learning, simulation-sim2real]
venue: CVPR 2025
arxiv: "2412.08442"
citations: 58
auto: true
---

> **TL;DR** MLLM을 multi-embodiment action tokenizer와 online RL로 Generalist Embodied Agent(GEA)로 확장한 연구이다.

**CVPR 2025** · Andrew Szot, Bogdan Mazoure, Omar Attia, Aleksei Timofeev, Harsh Agrawal, Devon Hjelm 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Szot_From_Multimodal_LLMs_to_Generalist_Embodied_Agents_Methods_and_Lessons_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2412.08442) · 인용 58회

**주제:** VLA · Reinforcement Learning · Simulation & Sim2Real

## 문제
기존 MLLM은 언어와 vision 중심으로 학습되어 Embodied AI, 게임, UI 제어, planning 등 다양한 행동 도메인을 일반화해 수행하기 어렵다.

## 핵심 아이디어
단일 MLLM을 multi-embodiment action tokenizer로 여러 도메인에 grounding되는 Generalist Embodied Agent로 적응시키고, cross-domain data와 online RL의 중요성을 보인다.

## 방법
GEA는 다양한 embodiment를 처리하는 action tokenizer를 통해 하나의 통합 모델로 행동을 출력한다. 대규모 embodied experience 데이터에 supervised learning을 적용하고 interactive simulator에서 online RL을 수행한다. 또한 일반화 성능을 위해 데이터 및 알고리즘 선택을 분석한다.

## 결과
cross-domain data와 online RL이 generalist agent 구축에 중요함을 확인했으며, 최종 GEA는 다양한 benchmark에서 다른 generalist model 및 benchmark-specific approach보다 unseen task에 대한 강한 일반화 성능을 달성했다.

## 연결
- **기반 대표 논문:** Code as Policies, Gato, Octo, Open X-Embodiment (데이터셋), OpenVLA, PPO — Proximal Policy Optimization, PaLM-E, RT-1, RT-2, SayCan — [[knowledge/map|분야 지도]]

## 초록 (원문)
We examine the capability of Multimodal Large Language Models (MLLMs) to tackle diverse domains that extend beyond the traditional language and vision tasks these models are typically trained on. Specifically, our focus lies in areas such as Embodied AI, Games, UI Control, and Planning. To this end, we introduce a process of adapting an MLLM to a Generalist Embodied Agent (GEA). GEA is a single unified model capable of grounding itself across these varied domains through a multi-embodiment action tokenizer. GEA is trained with supervised learning on a large dataset of embodied experiences and with online RL in interactive simulators. We explore the data and algorithmic choices necessary to develop such a model. Our findings reveal the importance of training with cross-domain data and online RL for building generalist agents. The final GEA model achieves strong generalization performance to unseen tasks across diverse benchmarks compared to other generalist models and benchmark-specific approaches.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
