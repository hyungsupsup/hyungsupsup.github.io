---
title: "Towards Long-Horizon Vision-Language Navigation: Platform, Benchmark and Method"
tags: [cvpr2025, navigation, dataset-benchmark]
venue: CVPR 2025
arxiv: "2412.09082"
citations: 111
auto: true
---

> **TL;DR** 장기적 Vision-Language Navigation을 위한 LH-VLN task와 NavGen platform, LHPR-VLN benchmark, MGDM method를 제안한 논문이다.

**CVPR 2025** · Xinshuai Song, Weixing Chen, Yang Liu, Weikai Chen, Guanbin Li, Liang Lin
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Song_Towards_Long-Horizon_Vision-Language_Navigation_Platform_Benchmark_and_Method_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2412.09082) · 인용 111회

**주제:** Navigation · Dataset & Benchmark

## 문제
기존 Vision-Language Navigation 방법은 주로 단일 단계 navigation에 집중해 복잡하고 동적인 환경에서의 다단계·장기 작업 성능이 제한된다.

## 핵심 아이디어
연속된 subtask 전반의 장기 계획과 의사결정 일관성을 강조하는 LH-VLN task를 정의하고, 자동 데이터 생성 platform과 세분화된 평가 지표, 동적 환경용 memory module을 함께 제안한다.

## 방법
NavGen은 bidirectional, multi-granularity generation 방식으로 복잡한 task 구조의 dataset을 자동 생성한다. LHPR-VLN benchmark는 3,260개 task와 평균 150 task steps로 구성되며 ISR, CSR, CGT metric으로 세분화 평가한다. MGDM module은 short-term memory blurring과 long-term memory retrieval을 결합해 동적 환경에서의 navigation 적응성을 높인다.

## 결과
LH-VLN을 위한 첫 benchmark로 3,260개 task, 평균 150 task steps를 제공하고, ISR·CSR·CGT metric과 MGDM을 통해 장기 navigation 평가와 동적 환경 적응을 지원한다.

## 초록 (원문)
Existing Vision-Language Navigation (VLN) methods primarily focus on single-stage navigation, limiting their effectiveness in multi-stage and long-horizon tasks within complex and dynamic environments. To address these limitations, we propose a novel VLN task, named Long-Horizon Vision-Language Navigation (LH-VLN), which emphasizes long-term planning and decision consistency across consecutive subtasks. Furthermore, to support LH-VLN, we develop an automated data generation platform NavGen, which constructs datasets with complex task structures and improves data utility through a bidirectional, multi-granularity generation approach. To accurately evaluate complex tasks, we construct the Long-Horizon Planning and Reasoning in VLN (LHPR-VLN) benchmark consisting of 3,260 tasks with an average of 150 task steps, serving as the first dataset specifically designed for the long-horizon vision-language navigation task. Furthermore, we propose Independent Success Rate (ISR), Conditional Success Rate (CSR), and CSR weight by Ground Truth (CGT) metrics, to provide fine-grained assessments of task completion. To improve model adaptability in complex tasks, we propose a novel Multi-Granularity Dynamic Memory (MGDM) module that integrates short-term memory blurring with long-term memory retrieval to enable flexible navigation in dynamic environments. Our platform, benchmark and method supply LH-VLN with a robust data generation pipeline, comprehensive model evaluation dataset, reasonable metrics, and a novel VLN model, establishing a foundational framework for advancing LH-VLN.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
