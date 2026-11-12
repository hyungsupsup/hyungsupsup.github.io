---
title: "RoomTour3D: Geometry-Aware Video-Instruction Tuning for Embodied Navigation"
tags: [cvpr2025, navigation, dataset-benchmark]
venue: CVPR 2025
arxiv: "2412.08591"
citations: 35
auto: true
---

> **TL;DR** 웹 기반 실내 룸 투어 영상으로부터 3D 재구성과 궤적 주석을 활용해 VLN용 대규모 비디오-지시 데이터셋 RoomTour3D를 구축한 연구이다.

**CVPR 2025** · Mingfei Han, Liang Ma, Kamila Zhumakhanova, Ekaterina Radionova, Jingyi Zhang, Xiaojun Chang 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Han_RoomTour3D_Geometry-Aware_Video-Instruction_Tuning_for_Embodied_Navigation_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2412.08591) · 인용 35회

**주제:** Navigation · Dataset & Benchmark

## 문제
VLN은 기존 시뮬레이터의 수동 데이터 큐레이션에 의존해 학습 데이터의 다양성과 규모가 제한되어 있다.

## 핵심 아이디어
온라인 룸 투어 영상의 규모와 다양성을 활용해 실제 실내 공간과 인간 보행 시연에서 개방형 궤적과 내비게이션 지시를 생성한다.

## 방법
RoomTour3D는 웹 기반 룸 투어 영상에서 3D 재구성을 수행해 보행 경로의 3D 궤적을 얻고, 방 유형, 객체 위치, 주변 장면의 3D 형상 정보를 추가로 주석한다. 이를 통해 약 100K개의 개방형 설명 강화 궤적과 약 200K개의 지시, 1847개 룸 투어 환경에서 얻은 17K개의 행동 강화 궤적을 포함한다.

## 결과
RoomTour3D는 CVDN, SOON, R2R, REVERIE 등 여러 VLN 작업에서 유의미한 성능 향상을 가능하게 했으며, 학습 가능한 zero-shot VLN 에이전트 개발을 촉진해 개방형 내비게이션의 가능성과 과제를 보여준다.

## 초록 (원문)
Vision-and-Language Navigation (VLN) suffers from the limited diversity and scale of training data, primarily constrained by the manual curation of existing simulators.To address this, we introduce RoomTour3D, a video-instruction dataset derived from web-based room tour videos that capture real-world indoor spaces and human walking demonstrations. Unlike existing VLN datasets, RoomTour3D leverages the scale and diversity of online videos to generate open-ended human walking trajectories and open-world navigable instructions. To compensate for the lack of navigation data in online videos, we perform 3D reconstruction and obtain 3D trajectories of walking paths augmented with additional information on the room types, object locations and 3D shape of surrounding scenes. Our dataset includes ~100K open-ended description-enriched trajectories with ~200K instructions, and 17K action-enriched trajectories from 1847 room tour environments.We demonstrate experimentally that RoomTour3D enables significant improvements across multiple VLN tasks including CVDN, SOON, R2R, and REVERIE.Moreover, RoomTour3D facilitates the development of trainable zero-shot VLN agents, showcasing the potential and challenges of advancing towards open-world navigation.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
