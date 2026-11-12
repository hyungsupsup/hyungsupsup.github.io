---
title: "HiLoTs: High-Low Temporal Sensitive Representation Learning for Semi-Supervised LiDAR Segmentation in Autonomous Driving"
tags: [cvpr2025, autonomous-driving, embodied-perception]
venue: CVPR 2025
arxiv: "2503.17752"
citations: 13
auto: true
---

> **TL;DR** HiLoTs는 연속 LiDAR 프레임에서 근거리/원거리 객체의 시간 민감도 차이를 반영한 high/low temporal representation을 학습해 semi-supervised LiDAR semantic segmentation 성능을 높인다.

**CVPR 2025** · R.D. Lin, Pengcheng Weng, Yinqiao Wang, Han Ding, Jinsong Han, Fei Wang
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_HiLoTs_High-Low_Temporal_Sensitive_Representation_Learning_for_Semi-Supervised_LiDAR_Segmentation_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.17752) · 인용 13회

**주제:** Autonomous Driving · Embodied Perception

## 문제
기존 semi-supervised LiDAR segmentation은 공간 분포나 단기 시간 정보(예: 인접 두 프레임)에 치중해 자율주행 장면의 풍부한 장기 시간 특성을 충분히 활용하지 못한다.

## 핵심 아이디어
자율주행에서 근거리 객체는 시간적으로 안정적이고 원거리 객체는 변화가 크다는 관찰에 착안해 high-temporal sensitivity와 low-temporal sensitivity representation을 분리 학습하고 cross-attention으로 융합한다.

## 방법
연속 LiDAR 프레임으로부터 high/low temporal sensitivity representation을 추출하고 cross-attention mechanism으로 강화·융합한다. 또한 teacher-student framework로 labeled/unlabeled branch의 representation을 정렬해 대량의 unlabeled data를 효과적으로 활용한다.

## 결과
SemanticKITTI와 nuScenes에서 HiLoTs가 state-of-the-art semi-supervised 방법들을 능가하며 LiDAR+Camera multimodal 접근에 가까운 성능을 달성한다고 보고한다.

## 초록 (원문)
LiDAR point cloud semantic segmentation plays a crucial role in autonomous driving. In recent years, semi-supervised methods have gained popularity due to their significant reduction in annotation labor and time costs. Current semi-supervised methods typically focus on point cloud spatial distribution or consider short-term temporal representations, e.g., only two adjacent frames, often overlooking the rich long-term temporal properties inherent in autonomous driving scenarios. In driving experience, we observe that nearby objects, such as roads and vehicles, remain stable while driving, whereas distant objects exhibit greater variability in category and shape. This natural phenomenon is also captured by LiDAR, which reflects lower temporal sensitivity for nearby objects and higher sensitivity for distant ones. To leverage these characteristics, we propose HiLoTs, which learns high-temporal sensitivity and low-temporal sensitivity representations from continuous LiDAR frames. These representations are further enhanced and fused using a cross-attention mechanism. Additionally, we employ a teacher-student framework to align the representations learned by the labeled and unlabeled branches, effectively utilizing the large amounts of unlabeled data. Experimental results on the SemanticKITTI and nuScenes datasets demonstrate that our proposed HiLoTs outperforms state-of-the-art semi-supervised methods, and achieves performance close to LiDAR+Camera multimodal approaches.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
