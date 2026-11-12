---
title: "CheckManual: A New Challenge and Benchmark for Manual-based Appliance Manipulation"
tags: [cvpr2025, manipulation, dataset-benchmark, simulation-sim2real]
venue: CVPR 2025
arxiv: "2506.09343"
citations: 14
auto: true
---

> **TL;DR** CheckManual은 가전제품 매뉴얼을 이해해 조작 계획을 세우는 로봇을 평가하기 위한 최초의 manual-based appliance manipulation 벤치마크와 ManualPlan 베이스라인을 제안한다.

**CVPR 2025** · Yuxing Long, Jiyao Zhang, Mingjie Pan, Tianshu Wu, Taewhan Kim, Hao Dong
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Long_CheckManual_A_New_Challenge_and_Benchmark_for_Manual-based_Appliance_Manipulation_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2506.09343) · 인용 14회

**주제:** Manipulation · Dataset & Benchmark · Simulation & Sim2Real

## 문제
기존 매뉴얼 관련 연구는 question-answering에 제한되어 있고, 조작 연구는 여러 페이지의 매뉴얼이 가전제품 부품 기능과 상호작용 방법, 작업 단계를 제공한다는 점을 활용하지 못한다.

## 핵심 아이디어
CAD 가전 모델을 기반으로 large model-assisted human-revised 데이터 생성 파이프라인을 통해 매뉴얼을 만들고, 이를 이용한 새로운 manipulation challenge와 평가 지표, simulator 환경을 구축한다.

## 방법
CheckManual은 가전제품 매뉴얼 기반 조작을 위한 벤치마크로, 매뉴얼 생성 파이프라인과 simulator 환경 및 평가 지표를 제공한다. 또한 매뉴얼을 바탕으로 조작을 계획하는 최초의 manual-based manipulation planning model인 ManualPlan을 제안해 베이스라인을 설정한다.

## 결과
논문은 최초의 manual-based appliance manipulation 벤치마크 CheckManual과 최초의 manual-based manipulation planning model ManualPlan을 제시하고, 이를 위한 베이스라인 그룹을 제공한다.

## 연결
- **기반 대표 논문:** OpenVLA, RT-1, RT-2, SayCan — [[knowledge/map|분야 지도]]
- 인용함 → [[knowledge/venues/cvpr-2025/Pan_OmniManip_Towards_General_Robotic_Manipulation_via_Object-Centric_Interaction_Primitives_as|OmniManip: Towards General Robotic Manipulation via Object-Centric Interaction Primitives as Spatial Constraints]]

## 초록 (원문)
Correct use of electrical appliances has significantly improved human life quality. Unlike simple tools that can be manipulated with common sense, different parts of electrical appliances have specific functions defined by manufacturers. If we want the robot to heat bread by microwave, we should enable them to review the microwave's manual first. From the manual, it can learn about component functions, interaction methods, and representative task steps about appliances. However, previous manual-related works remain limited to question-answering tasks while existing manipulation researchers ignore the manual's important role and fail to comprehend multi-page manuals. In this paper, we propose the first manual-based appliance manipulation benchmark CheckManual. Specifically, we design a large model-assisted human-revised data generation pipeline to create manuals based on CAD appliance models. With these manuals, we establish novel manual-based manipulation challenges, metrics, and simulator environments for model performance evaluation. Furthermore, we propose the first manual-based manipulation planning model ManualPlan to set up a group of baselines for the CheckManual benchmark.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
