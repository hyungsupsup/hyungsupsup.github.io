---
title: "Optimus-2: Multimodal Minecraft Agent with Goal-Observation-Action Conditioned Policy"
tags: [cvpr2025, vla, dataset-benchmark]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** Optimus-2는 MLLM 기반 고수준 계획과 Goal-Observation-Action Conditioned Policy(GOAP)를 결합한 Minecraft 에이전트로, MGOA 데이터셋을 활용해 다양한 open-world 작업을 수행한다.

**CVPR 2025** · Zaijing Li, Yuquan Xie, Rui Shao, Gongwei Chen, Dongmei Jiang, Liqiang Nie
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Optimus-2_Multimodal_Minecraft_Agent_with_Goal-Observation-Action_Conditioned_Policy_CVPR_2025_paper.html)

**주제:** VLA · Dataset & Benchmark

## 문제
Minecraft와 같은 open-world에서 다양한 작업의 행동 패턴을 학습하려면 observation, action, language 사이의 복잡한 관계를 모델링해야 한다. 또한 장기 작업과 open-ended 지시를 함께 처리하는 에이전트를 만드는 것이 어렵다.

## 핵심 아이디어
고수준 planning을 담당하는 MLLM과 low-level control을 담당하는 GOAP를 분리하고, Action-guided Behavior Encoder로 observation-action의 인과 관계를 fixed-length behavior tokens로 압축해 language instruction과 정렬하는 것이 핵심이다.

## 방법
GOAP의 Action-guided Behavior Encoder는 각 timestep의 observation-action 인과 관계를 모델링하고 historical observation-action sequence와 동적으로 상호작용해 behavior tokens를 만든다. 이후 MLLM이 behavior tokens를 open-ended language instructions와 align하여 action을 autoregressively 예측한다. High-level planning은 MLLM이 수행하며, 25,000 videos, 8 atomic tasks, about 30M goal-observation-action pairs를 포함한 MGOA dataset을 제안한다.

## 결과
Optimus-2는 Minecraft의 atomic tasks, long-horizon tasks, open-ended instruction tasks에서 superior performance를 보였다. MGOA dataset과 automated construction method도 Minecraft 에이전트 학습을 위한 기여로 제시된다.

## 초록 (원문)
Building an agent that can mimic human behavior patterns to accomplish various open-world tasks is a long-term goal. To enable agents to effectively learn behavioral patterns across diverse tasks, a key challenge lies in modeling the intricate relationships among observations, actions, and language. To this end, we propose Optimus-2, a novel Minecraft agent that incorporates a Multimodal Large Language Model (MLLM) for high-level planning, alongside a Goal-Observation-Action Conditioned Policy (GOAP) for low-level control. GOAP contains (1) an Action-guided Behavior Encoder that models causal relationships between observations and actions at each timestep, then dynamically interacts with the historical observation-action sequence, consolidating it into fixed-length behavior tokens, and (2) an MLLM that aligns behavior tokens with open-ended language instructions to predict actions auto-regressively. Moreover, we introduce a high-quality Minecraft Goal-Observation-Action (MGOA) dataset, which contains 25,000 videos across 8 atomic tasks, providing about 30M goal-observation-action pairs. The automated construction method, along with the MGOA dataset, can contribute to the community's efforts in training Minecraft agents. Extensive experimental results demonstrate that Optimus-2 exhibits superior performance across atomic tasks, long-horizon tasks, and open-ended instruction tasks in Minecraft.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
