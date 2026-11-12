---
title: "ReconDreamer: Crafting World Models for Driving Scene Reconstruction via Online Restoration"
tags: [cvpr2025, world-model, autonomous-driving, simulation-sim2real]
venue: CVPR 2025
arxiv: "2411.19548"
citations: 111
auto: true
---

> **TL;DR** ReconDreamer는 world model 지식을 점진적으로 통합해 자율주행 장면 재구성에서 큰 차선 변경 maneuver까지 고품질로 렌더링하는 방법을 제안한다.

**CVPR 2025** · Chaojun Ni, Guosheng Zhao, Xiaofeng Wang, Zheng Zhu, Wenkang Qin, Guan Huang 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Ni_ReconDreamer_Crafting_World_Models_for_Driving_Scene_Reconstruction_via_Online_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2411.19548) · 인용 111회

**주제:** World Model · Autonomous Driving · Simulation & Sim2Real

## 문제
기존 NeRF/3DGS 기반 센서 시뮬레이션은 학습 데이터 분포에 가까운 조건에서는 잘 동작하지만 차선 변경과 같은 새로운 궤적 렌더링에 어려움을 겪고, DriveDreamer4D의 training-free 통합 방식도 multi-lane shift 같은 큰 maneuver에서는 한계가 있다.

## 핵심 아이디어
world model 지식을 점진적으로 통합하고, online restoration을 수행하는 DriveRestorer와 progressive data update 전략을 도입해 큰 maneuver에서도 고품질 렌더링을 가능하게 한다.

## 방법
world model을 기반으로 DriveRestorer가 online restoration을 통해 ghosting artifact를 완화한다. 또한 progressive data update 전략으로 큰 maneuver에 대한 고품질 렌더링을 보장하며, multiple lanes에 걸쳐 최대 6 meters까지의 큰 maneuver를 효과적으로 렌더링하는 첫 방법이다.

## 결과
ReconDreamer는 Street Gaussians 대비 NTA-IoU, NTL-IoU, FID에서 각각 24.87%, 6.72%, 29.97% 상대적 개선을 보였고, 큰 maneuver 렌더링에서 DriveDreamer4D with PVG를 NTA-IoU 기준 195.87% 상대적 개선 및 사용자 연구로 능가했다.

## 연결
- 인용함 → [[knowledge/venues/cvpr-2025/Zhao_DriveDreamer4D_World_Models_Are_Effective_Data_Machines_for_4D_Driving|DriveDreamer4D: World Models Are Effective Data Machines for 4D Driving Scene Representation]]

## 초록 (원문)
Closed-loop simulation is crucial for end-to-end autonomous driving. Existing sensor simulation methods (e.g., NeRF and 3DGS) reconstruct driving scenes based on conditions that closely mirror training data distributions. However, these methods struggle with rendering novel trajectories, such as lane changes. Recent work, DriveDreamer4D, has demonstrated that integrating world model knowledge alleviates these issues. Although the training-free integration approach is efficient, it still struggles to render larger maneuvers, such as multi-lane shifts.Therefore, we introduce ReconDreamer, which enhances driving scene reconstruction through incremental integration of world model knowledge. Specifically, based on the world model, DriveRestorer is proposed to mitigate ghosting artifacts via online restoration. Additionally, we propose the progressive data update strategy to ensure high-quality rendering for larger maneuvers. Notably, ReconDreamer is the first method to effectively render in large maneuvers (e.g., across multiple lanes, spanning up to 6 meters). Additionally, experimental results demonstrate that ReconDreamer outperforms Street Gaussians in the NTA-IoU, NTL-IoU, and FID, with a relative improvement by 24.87%, 6.72%, and 29.97%. Furthermore, ReconDreamer surpasses DriveDreamer4D with PVG during large maneuver rendering, as verified by a relative improvement of 195.87% in the NTA-IoU metric and a comprehensive user study.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
