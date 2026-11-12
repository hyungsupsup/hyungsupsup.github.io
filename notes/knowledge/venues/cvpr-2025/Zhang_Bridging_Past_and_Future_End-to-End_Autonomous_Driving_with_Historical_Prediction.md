---
title: "Bridging Past and Future: End-to-End Autonomous Driving with Historical Prediction and Planning"
tags: [cvpr2025, autonomous-driving]
venue: CVPR 2025
arxiv: "2503.14182"
citations: 70
auto: true
---

> **TL;DR** BridgeAD는 과거의 예측 및 계획 query를 미래 time step별로 재구성해 end-to-end autonomous driving의 일관성과 정확도를 높이는 방법이다.

**CVPR 2025** · Bozhou Zhang, Nan Song, Xin Jin, Li Zhang
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Bridging_Past_and_Future_End-to-End_Autonomous_Driving_with_Historical_Prediction_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.14182) · 인용 70회

**주제:** Autonomous Driving

## 문제
기존 end-to-end autonomous driving은 dense historical BEV feature나 sparse memory bank로 과거 정보를 집계해, motion planning에서 과거 정보를 누락하거나 multi-step 미래 예측/계획 특성과 정렬되지 않는 문제가 있다.

## 핵심 아이디어
motion 및 planning query를 multi-step query로 재정의해 각 미래 time step에 맞는 query를 구분하고, 현재 frame의 historical query는 perception에, 미래 frame의 query는 motion planning에 결합한다.

## 방법
BridgeAD는 과거 prediction과 planning query를 time step에 따라 적절한 end-to-end 시스템 구성 요소에 적용한다. 현재 frame용 historical query는 perception과 결합하고, 미래 frame용 query는 motion planning과 통합해 past와 future를 연결한다. 이를 통해 모든 time step에서 historical insight를 집계해 전체 pipeline의 coherence와 accuracy를 향상시킨다.

## 결과
nuScenes dataset의 open-loop 및 closed-loop 설정에서 BridgeAD가 state-of-the-art 성능을 달성했다고 보고한다.

## 초록 (원문)
End-to-end autonomous driving unifies tasks in a differentiable framework, enabling planning-oriented optimization and attracting growing attention.Current methods aggregate historical information either through dense historical bird's-eye-view (BEV) features or by querying a sparse memory bank, following paradigms inherited from detection.However, we argue that these paradigms either omit historical information in motion planning or fail to align with its multi-step nature, which requires predicting or planning multiple future time steps. In line with the philosophy of "future is a continuation of past", we propose **BridgeAD**, which reformulates motion and planning queries as multi-step queries to differentiate the queries for each future time step. This design enables the effective use of historical prediction and planning by applying them to the appropriate parts of the end-to-end system based on the time steps, which improves both perception and motion planning. Specifically, historical queries for the current frame are combined with perception, while queries for future frames are integrated with motion planning. In this way, we bridge the gap between past and future by aggregating historical insights at every time step, enhancing the overall coherence and accuracy of the end-to-end autonomous driving pipeline. Extensive experiments on the nuScenes dataset in both open-loop and closed-loop settings demonstrate that BridgeAD achieves state-of-the-art performance. We will make our code and models publicly available.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
