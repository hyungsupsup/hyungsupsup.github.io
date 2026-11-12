---
title: "Code-as-Monitor: Constraint-aware Visual Programming for Reactive and Proactive Robotic Failure Detection"
tags: [cvpr2025, embodied-perception, manipulation]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** VLM이 생성한 코드로 시공간 제약 충족을 평가해 로봇의 반응적·능동적 실패 탐지를 수행하는 Code-as-Monitor를 제안한다.

**CVPR 2025** · Enshen Zhou, Qi Su, Cheng Chi, Zhizheng Zhang, Zhongyuan Wang, Tiejun Huang 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Zhou_Code-as-Monitor_Constraint-aware_Visual_Programming_for_Reactive_and_Proactive_Robotic_Failure_CVPR_2025_paper.html)

**주제:** Embodied Perception · Manipulation

## 문제
개방형(open-set) 로봇 실패를 사후에 반응적으로 식별하는 것과 사전에 능동적으로 예방하는 것을 동시에 달성하기 어렵다.

## 핵심 아이디어
반응적/능동적 실패 탐지를 통합된 시공간 제약 충족 문제로 정식화하고, VLM-generated code로 이를 실시간 평가한다. 제약 관련 엔티티나 부품을 compact geometric constraint elements로 추상화해 추적을 단순화하고 visual prompt로 활용한다.

## 방법
CaM은 VLM을 이용해 제약을 평가하는 코드를 생성하고 실시간 모니터링에 사용한다. constraint elements가 visual prompt로 제공되어 constraint-aware visual programming을 가능하게 하며, 이를 통해 open-set 실패를 반응적·능동적으로 탐지한다. 또한 open-loop control policy와 결합해 closed-loop 시스템으로 확장할 수 있다.

## 결과
세 가지 시뮬레이터와 실제 환경에서 severe disturbances 하에 baselines 대비 28.7% 높은 success rate를 달성하고 execution time을 31.8% 줄였다. cluttered dynamic environments의 long-horizon tasks를 위한 closed-loop 시스템 구성도 가능함을 보인다.

## 초록 (원문)
Automatic detection and prevention of open-set failures are crucial in closed-loop robotic systems. Recent studies often struggle to simultaneously identify unexpected failures reactively after they occur and prevent foreseeable ones proactively. To this end, we propose Code-as-Monitor (CaM), a novel paradigm leveraging the vision-language model (VLM) for both open-set reactive and proactive failure detection. The core of our method is to formulate both tasks as a unified set of spatio-temporal constraint satisfaction problems and use VLM-generated code to evaluate them for real-time monitoring. To enhance the accuracy and efficiency of monitoring, we further introduce constraint elements that abstract constraint-related entities or their parts into compact geometric elements. This approach offers greater generality, simplifies tracking, and facilitates constraint-aware visual programming by leveraging these elements as visual prompts. Experiments show that CaM achieves a 28.7% higher success rate and reduces execution time by 31.8% under severe disturbances compared to baselines across three simulators and a real-world setting. Moreover, CaM can be integrated with open-loop control policies to form closed-loop systems, enabling long-horizon tasks in cluttered scenes with dynamic environments.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
