---
title: "ManipTrans: Efficient Dexterous Bimanual Manipulation Transfer via Residual Learning"
tags: [cvpr2025, manipulation, imitation-learning, dataset-benchmark]
venue: CVPR 2025
arxiv: "2503.21860"
citations: 142
auto: true
---

> **TL;DR** ManipTrans는 인간의 양손 조작 기술을 시뮬레이션의 dexterous robotic hands로 효율적으로 전이하는 2단계 residual learning 방법이며, DexManipNet 데이터셋을 구축한다.

**CVPR 2025** · Kailin Li, Puhao Li, Tengyu Liu, Yuyang Li, Siyuan Huang
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Li_ManipTrans_Efficient_Dexterous_Bimanual_Manipulation_Transfer_via_Residual_Learning_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.21860) · 인용 142회

**주제:** Manipulation · Imitation Learning · Dataset & Benchmark

## 문제
기존 reinforcement learning이나 실제 teleoperation으로는 대규모의 정밀하고 인간과 유사한 양손 조작 시퀀스를 얻기 어렵다.

## 핵심 아이디어
일반적인 trajectory imitator를 pre-train한 뒤 interaction constraints 아래 residual module을 fine-tune하여 복잡한 양손 작업을 효율적으로 학습하고 정확히 실행한다.

## 방법
먼저 hand motion을 모방하는 generalist trajectory imitator를 pre-train하고, 이후 interaction constraints 하에서 특정 residual module을 fine-tune한다. 이를 통해 simulation에서 human bimanual skills를 dexterous robotic hands로 transfer한다. 또한 여러 hand-object dataset을 robotic hands로 transfer해 DexManipNet을 만든다.

## 결과
ManipTrans는 success rate, fidelity, efficiency에서 state-of-the-art 방법을 능가하며, DexManipNet은 3.3K episodes의 robotic manipulation을 포함하고 쉽게 확장 가능해 dexterous hands의 policy training과 real-world deployments를 지원한다.

## 연결
- **기반 대표 논문:** ACT / ALOHA, Diffusion Policy, Isaac Gym, Open X-Embodiment (데이터셋), PPO — Proximal Policy Optimization, RT-1, RT-2, UMI — Universal Manipulation Interface — [[knowledge/map|분야 지도]]
- 인용함 → [[knowledge/venues/cvpr-2025/Fu_GigaHands_A_Massive_Annotated_Dataset_of_Bimanual_Hand_Activities|GigaHands: A Massive Annotated Dataset of Bimanual Hand Activities]]

## 초록 (원문)
Human hands play a central role in interacting, motivating increasing research in dexterous robotic manipulation. Data-driven embodied AI algorithms demand precise, large-scale, human-like manipulation sequences, which are challenging to obtain with conventional reinforcement learning or real-world teleoperation. To address this, we introduce ManipTrans, a novel two-stage method for efficiently transferring human bimanual skills to dexterous robotic hands in simulation. ManipTrans first pre-trains a generalist trajectory imitator to mimic hand motion, then fine-tunes a specific residual module under interaction constraints, enabling efficient learning and accurate execution of complex bimanual tasks. Experiments show that ManipTrans surpasses state-of-the-art methods in success rate, fidelity, and efficiency. Leveraging ManipTrans, we transfer multiple hand-object datasets to robotic hands, creating DexManipNet, a large-scale dataset featuring previously unexplored tasks like pen capping and bottle unscrewing. DexManipNet comprises 3.3K episodes of robotic manipulation and is easily extensible, facilitating further policy training for dexterous hands and enabling real-world deployments.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
