---
title: "TANGO: Training-free Embodied AI Agents for Open-world Tasks"
tags: [cvpr2025, navigation, embodied-perception]
venue: CVPR 2025
arxiv: "2412.10402"
citations: 44
auto: true
---

> **TL;DR** TANGO는 LLM이 주어진 primitive들을 조합해 별도 학습 없이 다양한 embodied AI 작업을 수행하는 training-free 에이전트 접근법이다.

**CVPR 2025** · Filippo Ziliotto, Tommaso Campari, Luciano Serafini, Lamberto Ballan
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Ziliotto_TANGO_Training-free_Embodied_AI_Agents_for_Open-world_Tasks_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2412.10402) · 인용 44회

**주제:** Navigation · Embodied Perception

## 문제
Embodied agent가 여러 open-world 작업을 수행하려면 작업마다 별도 학습이 필요하다는 문제를 해결하고자 한다.

## 핵심 아이디어
PointGoal Navigation 모델과 memory-based exploration policy를 기반 primitive로 두고, LLM이 few in-context examples만으로 primitive를 조합해 작업별 프로그램을 구성하게 한다.

## 방법
단일 PointGoal Navigation 모델과 memory-based exploration policy가 에이전트를 세계 안에서 안내하는 foundational primitive로 사용된다. LLM은 prompt에 주어진 소수의 in-context examples를 바탕으로 primitive들을 조합해 특정 작업을 해결한다. 이 과정에서 추가 fine-tuning 없이 하나의 모델로 다양한 작업을 처리한다.

## 결과
Open-Set ObjectGoal Navigation, Multi-Modal Lifelong Navigation, Open Embodied Question Answering에서 별도 fine-tuning 없이 challenging zero-shot 시나리오에서 state-of-the-art 결과를 달성했다.

## 연결
- **기반 대표 논문:** Code as Policies — [[knowledge/map|분야 지도]]

## 초록 (원문)
Large Language Models (LLMs) have demonstrated excellent capabilities in composing various modules together to create programs that can perform complex reasoning tasks on images. In this paper, we propose TANGO, an approach that extends the program composition via LLMs already observed for images, aiming to integrate those capabilities into embodied agents capable of observing and acting in the world. Specifically, by employing a simple PointGoal Navigation model combined with a memory-based exploration policy as a foundational primitive for guiding an agent through the world, we show how a single model can address diverse tasks without additional training. We task an LLM with composing the provided primitives to solve a specific task, using only a few in-context examples in the prompt. We evaluate our approach on three key Embodied AI tasks: Open-Set ObjectGoal Navigation, Multi-Modal Lifelong Navigation, and Open Embodied Question Answering, achieving state-of-the-art results without any specific fine-tuning in challenging zero-shot scenarios.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
