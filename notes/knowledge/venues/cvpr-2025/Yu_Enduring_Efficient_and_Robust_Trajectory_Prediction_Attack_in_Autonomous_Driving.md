---
title: "Enduring, Efficient and Robust Trajectory Prediction Attack in Autonomous Driving via Optimization-Driven Multi-Frame Perturbation Framework"
tags: [cvpr2025, autonomous-driving, embodied-perception]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** LiDAR 유도 다중 프레임 최적화 기반 적대적 위치 탐색으로 자율주행 trajectory prediction을 지속적이고 효율적이며 robust하게 공격하는 프레임워크를 제안한다.

**CVPR 2025** · Yi Yu, Weizhen Han, Libing Wu, Bingyi Liu, Enshu Wang, Zhuangzhuang Zhang
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Yu_Enduring_Efficient_and_Robust_Trajectory_Prediction_Attack_in_Autonomous_Driving_CVPR_2025_paper.html)

**주제:** Autonomous Driving · Embodied Perception

## 문제
기존 trajectory prediction 공격은 단일 시점 공격에 의존해 일시적이고 필터링에 취약하며 배포 환경의 불확실성 때문에 실제 적용이 제한된다.

## 핵심 아이디어
적대적 차량 근처에 객체를 전략적으로 배치하고 multi-frame single-point attack으로 연속 상태 perturbation을 생성하며, 세 가지 loss로 adversarial object 위치를 최적화해 지속성·효율성·robust성을 달성한다.

## 방법
LiDAR-induced attack framework로 여러 프레임에 걸쳐 단일 지점 공격을 연속 적용해 trajectory prediction을 오도한다. 위치 탐색 단계에서 adversarial object를 크기 제약 없는 점으로 취급하고 세 가지 specialized loss functions로 위치를 최적화한다. 이를 통해 특정 attack point와 adversarial object 속성에 대한 의존을 줄인다.

## 결과
광범위한 실험을 통해 제안 프레임워크의 우수한 성능과 robustness를 확인했다.

## 초록 (원문)
Trajectory prediction plays a crucial role in autonomous driving systems, and exploring its vulnerability has garnered widespread attention. However, existing trajectory prediction attack methods often rely on single-point attacks to make efficient perturbations. This limits their applications in real-world scenarios due to the transient nature of single-point attacks, their susceptibility to filtration, and the uncertainty regarding the deployment environment. To address these challenges, this paper proposes a novel LiDAR-induced attack framework to impose multi-frame attacks by optimization-driven adversarial location search, achieving endurance, efficiency, and robustness. This framework strategically places objects near the adversarial vehicle to implement an attack and introduces three key innovations. First, successive state perturbations are generated using a multi-frame single-point attack strategy, effectively misleading trajectory predictions over extended time horizons. Second, we efficiently optimize adversarial objects' locations through three specialized loss functions to achieve desired perturbations. Lastly, we improve robustness by treating the adversarial object as a point without size constraints during the location search phase and reduce dependence on both the specific attack point and the adversarial object's properties. Extensive experiments confirm the superior performance and robustness of our framework.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
