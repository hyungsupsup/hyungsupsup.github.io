---
title: "VidBot: Learning Generalizable 3D Actions from In-the-Wild 2D Human Videos for Zero-Shot Robotic Manipulation"
tags: [cvpr2025, manipulation, embodied-perception]
venue: CVPR 2025
arxiv: "2503.07135"
citations: 82
auto: true
---

> **TL;DR** VidBot은 인터넷의 2D 인간 비디오에서 3D affordance를 학습해 zero-shot 로봇 조작을 가능하게 하는 프레임워크이다.

**CVPR 2025** · Hanzhi Chen, Boyang Sun, Anran Zhang, Marc Pollefeys, Stefan Leutenegger
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_VidBot_Learning_Generalizable_3D_Actions_from_In-the-Wild_2D_Human_Videos_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.07135) · 인용 82회

**주제:** Manipulation · Embodied Perception

## 문제
실제 로봇 학습은 데이터 수집 비용과 embodiment gap 때문에 확장성이 낮다. 인간 비디오를 활용해 물리적 로봇 학습을 최소화하면서 조작 능력을 전이하는 문제를 다룬다.

## 핵심 아이디어
monocular RGB 인간 비디오에서 depth foundation model과 structure-from-motion으로 metric-scale 3D hand trajectory를 추출해 embodiment-agnostic 3D affordance 표현을 만든다. coarse-to-fine affordance learning과 diffusion 기반 trajectory 생성으로 novel scene과 embodiment에 일반화한다.

## 방법
VidBot은 비디오에서 temporally consistent한 3D hand trajectory를 복원하고, pixel space에서 coarse action을 식별한 뒤 diffusion model로 fine-grained interaction trajectory를 생성한다. Test-time constraints를 사용해 context-aware interaction planning을 수행하며, 학습된 3D affordance로 zero-shot manipulation을 실행한다.

## 결과
13 manipulation tasks의 zero-shot settings에서 counterparts를 크게 능가하고 real-world robot systems에 seamless하게 배포할 수 있음을 보인다.

## 연결
- **기반 대표 논문:** BC-Z, DDPM, DROID (데이터셋), Diffusion Policy, Isaac Gym, Octo, Open X-Embodiment (데이터셋) — [[knowledge/map|분야 지도]]

## 초록 (원문)
Future robots are envisioned as versatile systems capable of performing a variety of household tasks. The big question remains, how can we bridge the embodiment gap while minimizing physical robot learning, which fundamentally does not scale well. We argue that learning from in-the-wild human videos offers a promising solution for robotic manipulation tasks, as vast amounts of relevant data already exist on the internet. In this work, we present VidBot, a framework enabling zero-shot robotic manipulation using learned 3D affordance from in-the-wild monocular RGB-only human videos. VidBot leverages a pipeline to extract explicit representations from them, namely 3D hand trajectories from videos, combining a depth foundation model with structure-from-motion techniques to reconstruct temporally consistent, metric-scale 3D affordance representations agnostic to embodiments. We introduce a coarse-to-fine affordance learning model that first identifies coarse actions from the pixel space and then generates fine-grained interaction trajectories with a diffusion model, conditioned on coarse actions and guided by test-time constraints for context-aware interaction planning, enabling substantial generalization to novel scenes and embodiments. Extensive experiments demonstrate the efficacy of VidBot, which significantly outperforms counterparts across 13 manipulation tasks in zero-shot settings and can be seamlessly deployed across robot systems in real-world environments. VidBot paves the way for leveraging everyday human videos to make robot learning more scalable.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
