---
title: "MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic Data"
tags: [cvpr2025, imitation-learning, manipulation, simulation-sim2real]
venue: CVPR 2025
arxiv: "2501.04595"
citations: 9
auto: true
---

> **TL;DR** MobileH2R은 대규모 합성 데이터만으로 이동형 로봇의 일반화 가능한 인간-로봇 물체 전달(H2MR) 기술을 학습하는 프레임워크다.

**CVPR 2025** · Zifan Wang, Ziqing Chen, Junyu Chen, Jilong Wang, Yuxin Yang, Yunze Liu 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_MobileH2R_Learning_Generalizable_Human_to_Mobile_Robot_Handover_Exclusively_from_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2501.04595) · 인용 9회

**주제:** Imitation Learning · Manipulation · Simulation & Sim2Real

## 문제
기존 고정 베이스 인간-로봇 전달과 달리, 이동성을 활용한 넓은 작업 공간에서 물체를 안정적으로 받는 일반화 가능한 H2MR 기술을 실제 시연 없이 학습하는 것이 문제다.

## 핵심 아이디어
실제 세계 시연 없이 시뮬레이터에서 고품질 합성 데이터를 대규모로 생성하고, 이를 닫힌 루프 베이스-팔 협응 정책으로 증류하면 일반화 가능한 전달 기술을 얻을 수 있다는 점이다.

## 방법
다양한 전신 인간 모션 합성 데이터를 생성하는 확장 가능한 파이프라인과 안전하고 모방하기 쉬운 시연을 자동 생성하는 방법을 제안한다. 이렇게 만든 대규모 시연을 효율적인 4D imitation learning으로 증류하여 베이스와 팔이 협응하는 닫힌 루프 정책을 학습한다.

## 결과
시뮬레이터와 실제 환경 평가에서 모든 경우에 baseline 대비 최소 +15% 성공률 향상을 보였고, 대규모·다양한 합성 데이터가 로봇 학습을 크게 향상시킴을 검증했다.

## 연결
- **기반 대표 논문:** Open X-Embodiment (데이터셋) — [[knowledge/map|분야 지도]]

## 초록 (원문)
This paper introduces MobileH2R, a framework for learning generalizable vision-based human-to-mobile-robot (H2MR) handover skills. Unlike traditional fixed-base handovers, this task requires a mobile robot to reliably receive objects in a large workspace enabled by its mobility. Our key insight is that generalizable handover skills can be developed in simulators using high-quality synthetic data, without the need for real-world demonstrations. To achieve this, we propose a scalable pipeline for generating diverse synthetic full-body human motion data, an automated method for creating safe and imitation-friendly demonstrations, and an efficient 4D imitation learning method for distilling large-scale demonstrations into closed-loop policies with base-arm coordination. Experimental evaluations in both simulators and the real world show significant improvements (at least +15% success rate) over baseline methods in all cases. Experiments also validate that large-scale and diverse synthetic data greatly enhances robot learning, highlighting our scalable framework.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
