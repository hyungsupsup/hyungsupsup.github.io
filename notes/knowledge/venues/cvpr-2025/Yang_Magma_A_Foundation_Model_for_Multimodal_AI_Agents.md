---
title: "Magma: A Foundation Model for Multimodal AI Agents"
tags: [cvpr2025, vla, manipulation, embodied-perception]
venue: CVPR 2025
arxiv: "2502.13130"
citations: 195
auto: true
---

> **TL;DR** Magma는 디지털 및 물리 세계의 멀티모달 에이전트 작업을 위해 VL 이해 능력과 시공간적 action grounding/planning 능력을 결합한 foundation model이다.

**CVPR 2025** · Jianwei Yang, Reuben Tan, Qianhui Wu, Ruijie Zheng, Baolin Peng, Yongyuan Liang 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_Magma_A_Foundation_Model_for_Multimodal_AI_Agents_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2502.13130) · 인용 195회

**주제:** VLA · Manipulation · Embodied Perception

## 문제
기존 vision-language 모델은 언어적 이해는 뛰어나지만 visual-spatial world에서 객체를 ground하고 행동으로 연결하는 능력이 부족하여 UI navigation부터 robot manipulation까지의 agentic task를 수행하기 어렵다.

## 핵심 아이디어
이미지의 actionable visual objects를 Set-of-Mark(SoM)로, 비디오의 object movements를 Trace-of-Mark(ToM)로 labeling하여 action grounding과 action planning을 직접 학습시킨다.

## 방법
Magma는 images, videos, robotics data를 포함한 대규모 heterogeneous dataset으로 학습된다. SoM은 클릭 가능한 버튼이나 조작 대상과 같은 actionable object를 표시해 action grounding을 돕고, ToM은 인간 손이나 robotic arm의 움직임 trace를 표시해 action planning을 돕는다. 이를 통해 VL 이해 능력을 유지하면서 시공간적 intelligence를 강화한다.

## 결과
Magma는 UI navigation과 robotic manipulation task에서 새로운 state-of-the-art 결과를 달성하여 해당 task에 특화된 기존 모델들을 능가했다. 또한 훨씬 큰 dataset으로 학습된 대형 multimodal model들과 비교해도 강한 multimodal understanding 능력을 유지한다.

## 연결
- **기반 대표 논문:** Octo, Open X-Embodiment (데이터셋), OpenVLA, PaLM-E, RT-1, RT-2, SimplerEnv — 시뮬레이션으로 실제 정책 평가 — [[knowledge/map|분야 지도]]

## 초록 (원문)
We present Magma, a foundation model that serves multimodal AI agentic tasks in both the digital and physical worlds. Magma is a significant extension of vision-language (VL) models in that it not only retains the VL understanding ability (verbal intelligence) of the latter, but is also equipped with the ability to ground and act in the visual-spatial world (spatial-temporal intelligence). To endow agentic capabilities for tasks ranging from UI navigation to robot manipulation, Magma is trained on large amounts of heterogeneous datasets that span from images, videos to robotics data, where actionable visual objects (e.g. clickable buttons in GUI) in images are labeled by Set-of-Mark (SoM) for action grounding, and object movements (e.g. trace of human hands or robotic arms) in videos are labeled by Trace-of-Mark (ToM) for action planning. Extensive experiments show that SoM and ToM help bridge the gap between verbal and action abilities and significantly enhance spatio-temporal intelligence which is fundamental to agentic tasks, as shown in Fig.1. In particular, Magma creates new state-of-the-art results on UI navigation and robotic manipulation tasks, outperforming previous models that are specifically tailored to these tasks. Moreover, Magma preserves strong multimodal understanding ability and compares favorably to popular large multimodal models that are trained on much larger datasets. We have made our model and code public for reproducibility at https://microsoft.github.io/Magma.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
