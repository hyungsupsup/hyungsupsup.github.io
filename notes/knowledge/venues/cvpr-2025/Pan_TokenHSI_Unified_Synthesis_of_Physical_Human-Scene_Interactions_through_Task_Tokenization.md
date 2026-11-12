---
title: "TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization"
tags: [cvpr2025, humanoid-locomotion, other]
venue: CVPR 2025
arxiv: "2503.19901"
citations: 83
auto: true
---

> **TL;DR** TokenHSI는 humanoid proprioception과 task token을 masking으로 결합한 단일 transformer policy로 다양한 physical human-scene interaction을 통합 합성한다.

**CVPR 2025** · Liang Pan, Zeshi Yang, Zhiyang Dou, Wenjia Wang, Buzhen Huang, Bo Dai 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Pan_TokenHSI_Unified_Synthesis_of_Physical_Human-Scene_Interactions_through_Task_Tokenization_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.19901) · 인용 83회

**주제:** Humanoid & Locomotion · Other

## 문제
기존 HSI 방법은 특정 상호작용 task마다 별도 controller를 학습해, 물건을 들고 앉기처럼 여러 skill 통합이 필요한 복잡한 task를 다루기 어렵다.

## 핵심 아이디어
humanoid proprioception을 shared token으로, 각 task를 distinct task token으로 표현하고 masking mechanism으로 결합해 multi-skill knowledge sharing과 variable-length input adaptation을 가능하게 한다.

## 방법
단일 transformer-based policy가 shared proprioception token과 task token을 입력받아 동작을 생성한다. Masking mechanism으로 task별 token 조합을 제어하고, 추가 task tokenizer 학습으로 interaction target geometry 변경 및 여러 skill coordination을 지원한다.

## 결과
실험에서 TokenHSI가 다양한 HSI task에서 versatility, adaptability, extensibility를 크게 향상시킨다고 주장한다.

## 연결
- **기반 대표 논문:** Isaac Gym, PPO — Proximal Policy Optimization, RT-2 — [[knowledge/map|분야 지도]]

## 초록 (원문)
Synthesizing diverse and physically plausible Human-Scene Interactions (HSI) is pivotal for both computer animation and embodied AI. Despite encouraging progress, current methods mainly focus on developing separate controllers, each specialized for a specific interaction task. This significantly hinders the ability to tackle a wide variety of challenging HSI tasks that require the integration of multiple skills, e.g., sitting down while carrying an object (see Fig. 1). To address this issue, we present TokenHSI, a single, unified transformer-based policy capable of multi-skill unification and flexible adaptation. The key insight is to model the humanoid proprioception as a separate shared token and combine it with distinct task tokens via a masking mechanism. Such a unified policy enables effective knowledge sharing across skills, thereby facilitating the multi-task training. Moreover, our policy architecture supports variable length inputs, enabling flexible adaptation of learned skills to new scenarios. By training additional task tokenizers, we can not only modify the geometries of interaction targets but also coordinate multiple skills to address complex tasks. The experiments demonstrate that our approach can significantly improve versatility, adaptability, and extensibility in various HSI tasks.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
