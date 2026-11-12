---
title: "SimLingo: Vision-Only Closed-Loop Autonomous Driving with Language-Action Alignment"
tags: [cvpr2025, autonomous-driving, vla]
venue: CVPR 2025
arxiv: "2503.09594"
citations: 229
auto: true
---

> **TL;DR** SimLingo는 카메라만 사용하는 VLM 기반 모델로 closed-loop 주행, vision-language 이해, language-action alignment를 함께 수행하는 자율주행 모델이다.

**CVPR 2025** · Katrin Renz, Long Chen, Elahe Arani, Oleg Sinavski
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Renz_SimLingo_Vision-Only_Closed-Loop_Autonomous_Driving_with_Language-Action_Alignment_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.09594) · 인용 229회

**주제:** Autonomous Driving · VLA

## 문제
기존 LLM 기반 자율주행 연구는 주행 성능과 vision-language 이해를 동시에 달성하기 어렵고, VQA 기반 이해가 행동 공간과 정렬되지 않아 모델의 답변이 실제 주행 행동과 불일치할 수 있다.

## 핵심 아이디어
closed-loop driving, vision-language understanding, language-action alignment의 세 과제를 함께 처리하는 VLM 기반 모델을 제안하며, LiDAR 같은 고가 센서 없이 카메라만 사용한다.

## 방법
SimLingo는 vision language model(VLM)을 기반으로 카메라 입력만 사용해 closed-loop 주행을 수행한다. 또한 vision-language 이해와 language-action alignment를 함께 학습해 언어 답변이 행동 공간과 일관되도록 한다.

## 결과
SimLingo는 CARLA simulator의 Bench2Drive benchmark에서 state-of-the-art 성능을 달성하고 CARLA challenge 2024에서 우승했으며, 높은 주행 성능을 유지하면서 다양한 language-related task에서도 강한 결과를 보인다.

## 연결
- **기반 대표 논문:** OpenVLA, RT-2, π0  (flow matching) — [[knowledge/map|분야 지도]]

## 초록 (원문)
Integrating large language models (LLMs) into autonomous driving has attracted significant attention with the hope of improving generalization and explainability. However, existing methods often focus on either driving or vision-language understanding but achieving both high driving performance and extensive language understanding remains challenging. In addition, the dominant approach to tackle vision-language understanding is using visual question answering. However, for autonomous driving, this is only useful if it is aligned with the action space. Otherwise, the model's answers could be inconsistent with its behavior. Therefore, we propose a model that can handle three different tasks: (1) closed-loop driving, (2) vision-language understanding, and (3) language-action alignment. Our model SimLingo is based on a vision language model (VLM) and works using only camera, excluding expensive sensors like LiDAR. SimLingo obtains state-of-the-art performance on the widely used CARLA simulator on the Bench2Drive benchmark and is the winning entry at the CARLA challenge 2024. Additionally, we achieve strong results in a wide variety of language-related tasks while maintaining high driving performance.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
