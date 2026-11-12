---
title: "Ges3ViG : Incorporating Pointing Gestures into Language-Based 3D Visual Grounding for Embodied Reference Understanding"
tags: [cvpr2025, embodied-perception, dataset-benchmark]
venue: CVPR 2025
arxiv: "2504.09623"
citations: 19
auto: true
---

> **TL;DR** 언어 설명과 pointing gesture를 함께 사용해 3D 장면에서 목표 객체를 찾는 3D-ERU용 데이터 증강 기법과 benchmark, 그리고 Ges3ViG 모델을 제안한 논문이다.

**CVPR 2025** · Atharv Mahesh Mane, Dulanga Weerakoon, Vigneshwaran Subbaraju, Sougata Sen, Sanjay E. Sarma, Archan Misra
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Mane_Ges3ViG__Incorporating_Pointing_Gestures_into_Language-Based_3D_Visual_Grounding_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2504.09623) · 인용 19회

**주제:** Embodied Perception · Dataset & Benchmark

## 문제
기존 3D visual grounding은 주로 언어만 사용하며, human pointing gesture를 함께 활용하는 3D Embodied Reference Understanding(3DERU) 연구와 데이터는 부족하다.

## 핵심 아이디어
Imputer라는 data augmentation framework로 기존 언어 기반 3D scene dataset에 pointing gesture를 추가해 ImputeRefer benchmark를 구축하고, 이를 위한 Ges3ViG 모델을 제안한다.

## 방법
3DERU는 language description과 accompanying pointing gesture를 결합해 3D scene에서 가장 관련 있는 target object를 식별한다. Imputer는 기존 3D scene dataset에 human pointing gesture를 주입해 ImputeRefer를 만들고, Ges3ViG는 이 multimodal reference를 처리하도록 설계된 모델이다.

## 결과
Ges3ViG는 다른 3DERU 모델 대비 accuracy 30% 향상, purely language-based 3D grounding 모델 대비 9% 향상을 달성했다고 보고한다.

## 초록 (원문)
3-Dimensional Embodied Reference Understanding (3DERU) combines a language description and an accompanying pointing gesture to identify the most relevant target object in a 3D scene. Although prior work has explored pure language-based 3D grounding, there has been limited exploration of 3D-ERU, which also incorporates human pointing gestures. To address this gap, we introduce a data augmentation framework-Imputer, and use it to curate a new benchmark dataset-ImputeRefer for 3D-ERU, by incorporating human pointing gestures into existing 3D scene datasets that only contain language instructions. We also propose Ges3ViG, a novel model for 3D-ERU that achieves 30% improvement in accuracy as compared to other 3DERU models and 9% compared to other purely language-based 3D grounding models. Our code and dataset are available at https://github.com/AtharvMane/Ges3ViG.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
