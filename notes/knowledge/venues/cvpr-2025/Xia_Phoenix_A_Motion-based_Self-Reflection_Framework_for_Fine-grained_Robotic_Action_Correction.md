---
title: "Phoenix: A Motion-based Self-Reflection Framework for Fine-grained Robotic Action Correction"
tags: [cvpr2025, manipulation, imitation-learning]
venue: CVPR 2025
arxiv: "2504.14588"
citations: 29
auto: true
---

> **TL;DR** Phoenix는 MLLM의 semantic reflection을 motion instruction으로 변환해 diffusion policy 기반의 세밀한 로봇 action correction을 수행하는 self-reflection 프레임워크다.

**CVPR 2025** · Wenke Xia, Ruoxuan Feng, Dong Wang, Di Hu
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Xia_Phoenix_A_Motion-based_Self-Reflection_Framework_for_Fine-grained_Robotic_Action_Correction_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2504.14588) · 인용 29회

**주제:** Manipulation · Imitation Learning

## 문제
로봇이 실패에서 회복하려면 self-correction이 필요하지만, MLLM의 semantic reflection을 세밀한 로봇 action 수정 방법으로 연결하기 어렵다.

## 핵심 아이디어
motion instruction을 high-level semantic reflection과 low-level robotic action correction 사이의 bridge로 사용한다. 일반화 요구를 low-level manipulation policy에서 MLLMs 기반 motion adjustment model로 옮긴다.

## 방법
dual-process motion adjustment mechanism으로 MLLM이 semantic reflection을 coarse-grained motion instruction 조정으로 변환한다. multi-task motion-conditioned diffusion policy가 visual observation을 통합해 high-frequency robotic action correction을 수행한다. 또한 dynamic environment와의 interaction을 통해 lifelong learning으로 모델 능력을 자동 개선한다.

## 결과
RoboMimic simulation과 real-world scenarios에서 다양한 manipulation tasks에 대해 우수한 generalization과 robustness를 입증했다.

## 연결
- **기반 대표 논문:** ACT / ALOHA, Code as Policies, Diffusion Policy, Octo, Open X-Embodiment (데이터셋), OpenVLA, PPO — Proximal Policy Optimization, PaLM-E, RT-1, RT-2 — [[knowledge/map|분야 지도]]

## 초록 (원문)
Building a generalizable self-correction system is crucial for robots to recover from failures. Despite advancements in Multimodal Large Language Models (MLLMs) that empower robots with semantic reflection ability for failure, translating semantic reflection into how to correct fine-grained robotic actions remains a significant challenge. To address this gap, we build the Phoenix framework, which leverages motion instruction as a bridge to connect high-level semantic reflection with low-level robotic action correction. In this motion-based self-reflection framework, we start with a dual-process motion adjustment mechanism with MLLMs to translate the semantic reflection into coarse-grained motion instruction adjustment. To leverage this motion instruction for guiding how to correct fine-grained robotic actions, a multi-task motion-conditioned diffusion policy is proposed to integrate visual observations for high-frequency robotic action correction. By combining these two models, we could shift the demand for generalization capability from the low-level manipulation policy to the MLLMs-driven motion adjustment model and facilitate precise, fine-grained robotic action correction. Utilizing this framework, we further develop a lifelong learning method to automatically improve the model's capability from interactions with dynamic environments. The experiments conducted in both the RoboMimic simulation and real-world scenarios prove the superior generalization and robustness of our framework across a variety of manipulation tasks.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
