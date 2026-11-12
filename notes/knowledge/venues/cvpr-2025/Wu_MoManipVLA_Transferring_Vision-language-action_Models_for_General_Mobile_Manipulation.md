---
title: "MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation"
tags: [cvpr2025, vla, manipulation]
venue: CVPR 2025
arxiv: "2503.13446"
citations: 64
auto: true
---

> **TL;DR** 고정 베이스용 pre-trained VLA 모델을 mobile manipulation에 전이하는 효율적인 policy adaptation framework인 MoManipVLA를 제안한다.

**CVPR 2025** · Zhenyu Wu, Yuheng Zhou, Xiuwei Xu, Ziwei Wang, Haibin Yan
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_MoManipVLA_Transferring_Vision-language-action_Models_for_General_Mobile_Manipulation_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.13446) · 인용 64회

**주제:** VLA · Manipulation

## 문제
기존 mobile manipulation은 대규모 학습 부족으로 다양한 task와 environment에 일반화하기 어렵고, 최신 VLA 모델은 뛰어난 일반화 능력에도 불구하고 fixed-base manipulation용으로 개발되었다.

## 핵심 아이디어
Pre-trained VLA 모델로 end-effector waypoint를 생성하고, mobile base와 robot arm의 motion planning objective 및 bi-level optimization을 통해 물리적 실행 가능성을 높인 mobile manipulation trajectory를 생성한다.

## 방법
VLA 모델을 활용해 일반화 능력이 높은 end-effector waypoint를 예측한다. Mobile base와 robot arm을 위한 motion planning objective를 설계해 trajectory의 physical feasibility를 최대화한다. Bi-level objective optimization에서 upper-level은 manipulator policy space를 확장하는 base movement waypoint를 예측하고, lower-level은 manipulation을 완료할 최적 end-effector trajectory를 선택한다.

## 결과
OVMM과 real world 실험에서 state-of-the-art mobile manipulation보다 4.2% 높은 success rate를 달성했고, pre-trained VLA 모델의 강한 generalization ability 덕분에 real world deployment에 only requires 50 training cost를 보인다.

## 연결
- **기반 대표 논문:** Diffusion Policy, Mobile ALOHA, Open X-Embodiment (데이터셋), OpenVLA, RT-1, π0  (flow matching) — [[knowledge/map|분야 지도]]
- 인용됨 ← [[knowledge/venues/cvpr-2025/Wu_AffordDP_Generalizable_Diffusion_Policy_with_Transferable_Affordance|AffordDP: Generalizable Diffusion Policy with Transferable Affordance]]

## 초록 (원문)
Mobile manipulation is the fundamental challenge for robotics to assist humans with diverse tasks and environments in everyday life. However, conventional mobile manipulation approaches often struggle to generalize across different tasks and environments because of the lack of large-scale training.In contrast, recent advances in vision-language-action (VLA) models have shown impressive generalization capabilities, but these foundation models are developed for fixed-base manipulation tasks.Therefore, we propose an efficient policy adaptation framework to transfer pre-trained VLA models of fix-base manipulation to mobile manipulation, so that high generalization ability across tasks and environments can be achieved in mobile manipulation policy.Specifically, we utilize pre-trained VLA models to generate waypoints of the end-effector with high generalization ability. We design motion planning objectives for the mobile base and the robot arm, which aim at maximizing the physical feasibility of the trajectory. Finally, we present an efficient bi-level objective optimization framework for trajectory generation, where the upper-level optimization predicts waypoints for base movement to enhance the manipulator policy space, and the lower-level optimization selects the optimal end-effector trajectory to complete the manipulation task. Extensive experimental results on OVMM and the real world demonstrate that our method achieves a 4.2% higher success rate than the state-of-the-art mobile manipulation, and only requires 50 training cost for real world deployment due to the strong generalization ability in the pre-trained VLA models.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
