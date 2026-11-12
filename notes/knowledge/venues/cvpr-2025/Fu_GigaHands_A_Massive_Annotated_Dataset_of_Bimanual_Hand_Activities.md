---
title: "GigaHands: A Massive Annotated Dataset of Bimanual Hand Activities"
tags: [cvpr2025, dataset-benchmark, manipulation, embodied-perception]
venue: CVPR 2025
arxiv: "2412.04244"
citations: 58
auto: true
---

> **TL;DR** GigaHands는 56명의 피험자와 417개 객체로부터 수집한 34시간 분량의 양손 활동 데이터셋이다.

**CVPR 2025** · Rao Fu, Dingxi Zhang, Alex Jiang, Wanjia Fu, Austin Funk, Daniel Ritchie 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Fu_GigaHands_A_Massive_Annotated_Dataset_of_Bimanual_Hand_Activities_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2412.04244) · 인용 58회

**주제:** Dataset & Benchmark · Manipulation · Embodied Perception

## 문제
기존 데이터셋은 규모, 다양한 손 활동 범위, 상세 주석이 부족해 양손 활동에 대한 대규모 모델을 구축하기 어렵다.

## 핵심 아이디어
마커리스 캡처 환경과 데이터 수집 프로토콜을 통해 3D 손과 객체 추정 및 텍스트 주석을 자동화해 대규모 양손 활동 데이터를 구축한다.

## 방법
56명의 피험자와 417개 객체를 대상으로 183백만 프레임, 14k 모션 클립, 84k 텍스트 주석을 포함하는 데이터셋을 수집한다. 마커리스 설정으로 3D 손과 객체를 자동 추정하고 텍스트 주석 작업을 최소화한다.

## 결과
34시간 분량의 양손 활동 데이터를 제공하며, 텍스트 기반 동작 합성, 손 모션 캡셔닝, 동적 radiance field 재구성 등에 활용될 수 있음을 보인다.

## 연결
- **기반 대표 논문:** Open X-Embodiment (데이터셋), OpenVLA, RT-1, RT-2 — [[knowledge/map|분야 지도]]
- 인용됨 ← [[knowledge/venues/cvpr-2025/Li_ManipTrans_Efficient_Dexterous_Bimanual_Manipulation_Transfer_via_Residual_Learning|ManipTrans: Efficient Dexterous Bimanual Manipulation Transfer via Residual Learning]]

## 초록 (원문)
Understanding bimanual human hand activities is a critical problem in AI and robotics. We cannot build large models of bimanual activities because existing datasets lack the scale, coverage of diverse hand activities, and detailed annotations. We introduce GigaHands, a massive annotated dataset capturing 34 hours of bimanual hand activities from 56 subjects and 417 objects, totaling 14k motion clips derived from 183 million frames paired with 84k text annotations. Our markerless capture setup and data acquisition protocol enable fully automatic 3D hand and object estimation while minimizing the effort required for text annotation. The scale and diversity of GigaHands enable broad applications, including text-driven action synthesis, hand motion captioning, and dynamic radiance field reconstruction.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
