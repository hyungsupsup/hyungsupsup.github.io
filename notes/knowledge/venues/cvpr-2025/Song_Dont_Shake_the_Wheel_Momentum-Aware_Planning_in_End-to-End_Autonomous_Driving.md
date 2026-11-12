---
title: "Don't Shake the Wheel: Momentum-Aware Planning in End-to-End Autonomous Driving"
tags: [cvpr2025, autonomous-driving]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** MomAD는 trajectory momentum과 perception momentum을 도입해 end-to-end 자율주행의 one-shot trajectory 예측을 안정화하고 장기 일관성을 개선하는 프레임워크이다.

**CVPR 2025** · Ziying Song, Caiyan Jia, Lin Liu, Hongyu Pan, Yongchang Zhang, Junming Wang 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Song_Dont_Shake_the_Wheel_Momentum-Aware_Planning_in_End-to-End_Autonomous_Driving_CVPR_2025_paper.html)

**주제:** Autonomous Driving

## 문제
기존 end-to-end 자율주행 프레임워크는 one-shot trajectory prediction에 의존해 제어가 불안정해지고 단일 프레임 인식의 occlusion에 취약할 수 있다.

## 핵심 아이디어
과거 경로와 정렬되는 planning query를 선택하고 historical query와 cross-attend하여 trajectory 및 perception momentum을 활용하는 점이 핵심이다.

## 방법
MomAD는 Hausdorff Distance 기반 Topological Trajectory Matching(TTM)으로 prior path와 일치하는 최적 planning query를 선택한다. Momentum Planning Interactor(MPI)는 선택된 query를 historical query와 cross-attend해 static/dynamic perception 정보를 확장하고 long-horizon trajectory를 재생성한다. 또한 training 중 robust instance denoising을 적용해 동적 환경과 detection error로 인한 noise를 줄이며, Trajectory Prediction Consistency(TPC) metric으로 planning stability를 평가한다.

## 결과
nuScenes에서 MomAD는 SOTA 방법보다 >3s의 장기 일관성을 달성했고, Turning-nuScenes에서 6s prediction horizon 기준 collision rate를 26% 줄이고 TPC를 0.97m(33.45%) 개선했다. Bench2Drive closed-loop에서는 success rate가 최대 16.3% 향상되었다.

## 초록 (원문)
End-to-end autonomous driving frameworks enable seamless integration of perception and planning but often rely on one-shot trajectory prediction, which may lead to unstable control and vulnerability to occlusions in single-frame perception. To address this, we propose the Momentum-Aware Driving (MomAD) framework, which introduces trajectory momentum and perception momentum to stabilize and refine trajectory predictions. MomAD comprises two core components: (1) Topological Trajectory Matching (TTM) employs Hausdorff Distance to select the optimal planning query that aligns with prior paths to ensure coherence; (2) Momentum Planning Interactor (MPI) cross-attends the selected planning query with historical queries to expand static and dynamic perception files. This enriched query, in turn, helps regenerate long-horizon trajectory and reduce collision risks. To mitigate noise arising from dynamic environments and detection errors, we introduce robust instance denoising during training, enabling the planning model to focus on critical signals and improve its robustness. We also propose a novel Trajectory Prediction Consistency (TPC) metric to quantitatively assess planning stability. Experiments on the nuScenes dataset demonstrate that MomAD achieves superior long-term consistency (>3s) compared to SOTA methods. Moreover, evaluations on the curated Turning-nuScenes shows that MomAD reduces the collision rate by 26% and improves TPC by 0.97m (33.45%) over a 6s prediction horizon, while closed-loop on Bench2Drive demonstrates an up to 16.3% improvement in success rate.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
