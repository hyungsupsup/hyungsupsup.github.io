---
title: "Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation"
tags: [cvpr2025, vla, manipulation]
venue: CVPR 2025
arxiv: "2505.02166"
citations: 10
auto: true
---

> **TL;DR** RGB 이미지 위에 2D visual prompt를 오버레이해 low-level action과 high-level planning을 함께 전달하는 object-centric VLA 조작 방법을 제안한다.

**CVPR 2025** · Xiaoqi Li, Jingyun Xu, Mingxu Zhang, Jiaming Liu, Yan Shen, Iaroslav Ponomarenko 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Object-Centric_Prompt-Driven_Vision-Language-Action_Model_for_Robotic_Manipulation_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2505.02166) · 인용 10회

**주제:** VLA · Manipulation

## 문제
자연어 목표는 모호할 수 있고, goal image나 goal video는 지나치게 세부적인 정보를 제공해 로봇 조작 목표를 효과적으로 전달하기 어렵다.

## 핵심 아이디어
각 key-frame마다 end-effector pose와 접촉 후 이동 방향 같은 목표를 담은 단순한 2D visual prompt를 RGB 이미지에 오버레이하고, 모델이 visual-language prompt를 해석해 SE(3) 공간의 contact pose와 movement direction을 예측하도록 한다.

## 방법
작업 시퀀스의 각 key-frame에 대해 수동 또는 자동으로 2D visual prompt를 생성하고, 모델이 이를 해석해 해당 contact pose와 movement direction을 예측하도록 학습한다. 이후 모든 key-frame 단계를 순차적으로 실행해 long-horizon task를 완수한다.

## 결과
시뮬레이션과 실제 환경에서 평가하여 robust한 manipulation 능력을 보였다.

## 연결
- **기반 대표 논문:** Code as Policies, Diffusion Policy, OpenVLA, RT-1, RT-2, SayCan, UniSim — [[knowledge/map|분야 지도]]

## 초록 (원문)
In robotic manipulation, task goals can be conveyed through various modalities, such as language, goal images, and goal videos. However, natural language can be ambiguous, while images or videos may offer overly detailed specifications. To address these challenges, we propose a novel approach using comprehensive multi-modal prompts that explicitly convey both low-level actions and high-level planning in a simple manner. Specifically, for each key-frame in the task sequence, our method allows for manual or automatic generation of simple and expressive 2D visual prompts overlaid on RGB images. These prompts represent the required task goals, such as the end-effector pose and the desired movement direction after contact. We develop a training strategy that enables the model to interpret these visual-language prompts and predict the corresponding contact poses and movement directions in SE(3) space. Furthermore, by sequentially executing all key-frame steps, the model can complete long-horizon tasks. This approach not only helps the model explicitly understand the task objectives but also enhances its robustness on unseen tasks by providing easily interpretable prompts. We evaluate our method in both simulated and real-world environments, demonstrating its robust manipulation capabilities.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
