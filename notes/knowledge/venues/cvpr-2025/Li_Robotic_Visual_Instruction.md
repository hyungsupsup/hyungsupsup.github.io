---
title: "Robotic Visual Instruction"
tags: [cvpr2025, vla, manipulation, embodied-perception]
venue: CVPR 2025
arxiv: "2505.00693"
citations: 28
auto: true
---

> **TL;DR** 자연어 대신 손그림 기호로 로봇 작업을 지시하는 RoVI와 이를 해석해 3D 행동으로 변환하는 VIEW 파이프라인을 제안한다.

**CVPR 2025** · Yanbang Li, Ziyang Gong, Haoyang Li, Xiaoqi Huang, Haolan Kang, Guangping Bai 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Robotic_Visual_Instruction_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2505.00693) · 인용 28회

**주제:** VLA · Manipulation · Embodied Perception

## 문제
자연어는 로봇 제어에 필요한 공간적 정밀도가 부족해 모호성과 장황함이 발생한다. 이를 해결하기 위해 공간-시간 정보를 담은 직관적인 로봇 지시 인터페이스가 필요하다.

## 핵심 아이디어
화살표, 원, 색상, 숫자를 활용한 객체 중심 2D 스케치 기반 RoVI를 도입하고, VLM이 이를 해석해 keypoint 추출을 통해 3D 행동 시퀀스로 변환하도록 한다.

## 방법
VIEW는 VLM으로 RoVI 입력을 이해하고 2D 픽셀 공간에서 공간 및 시간 제약을 keypoint로 디코딩한 뒤 실행 가능한 3D action sequence로 변환한다. 또한 edge deployment를 위해 15K 인스턴스의 전용 데이터셋으로 소형 VLM을 fine-tune한다.

## 결과
실제 및 시뮬레이션 환경의 11개 신규 작업에서 검증되었고, VIEW는 multi-step actions, disturbances, trajectory-following requirements가 포함된 미학습 실제 작업에서 87.5% 성공률을 달성했다.

## 연결
- **기반 대표 논문:** Octo, PaLM-E, RT-1, RT-2, SimplerEnv — 시뮬레이션으로 실제 정책 평가 — [[knowledge/map|분야 지도]]

## 초록 (원문)
Recently, natural language has been the primary medium for human-robot interaction. However, its inherent lack of spatial precision for robotic control introduces challenges such as ambiguity and verbosity. To address these limitations, we introduce the ***Robotic Visual Instruction (RoVI)***, a novel paradigm to guide robotic tasks through an object-centric, hand-drawn symbolic representation. RoVI effectively encodes spatial-temporal information into human-interpretable visual instructions through 2D sketches, utilizing arrows, circles, colors, and numbers to direct 3D robotic manipulation. To enable robots to understand RoVI better and generate precise actions based on RoVI, we present ***Visual Instruction Embodied Workflow (VIEW)***, a pipeline formulated for RoVI-conditioned policies. This approach leverages Vision-Language Models (VLMs) to interpret RoVI inputs, decode spatial and temporal constraints from 2D pixel space via keypoint extraction, and then transform them into executable 3D action sequences. We additionally curate a specialized dataset of 15K instances to fine-tune small VLMs for edge deployment, enabling them to effectively learn RoVI capabilities. Our approach is rigorously validated across 11 novel tasks in both real and simulated environments, demonstrating significant generalization capability. Notably, VIEW achieves an 87.5% success rate in real-world scenarios involving unseen tasks that feature multi-step actions, with disturbances, and trajectory-following requirements. Code and Datasets in this paper will be released soon.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
