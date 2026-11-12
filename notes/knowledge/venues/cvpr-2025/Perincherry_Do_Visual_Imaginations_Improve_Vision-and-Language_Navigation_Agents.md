---
title: "Do Visual Imaginations Improve Vision-and-Language Navigation Agents?"
tags: [cvpr2025, navigation, embodied-perception]
venue: CVPR 2025
arxiv: "2503.16394"
citations: 23
auto: true
---

> **TL;DR** VLN agent에게 instruction의 landmark를 text-to-image diffusion model로 시각화한 imagination을 추가 modality로 제공해 navigation 성능을 높이는 방법을 연구한다.

**CVPR 2025** · Akhil Perincherry, Jacob Krantz, Stefan Lee
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Perincherry_Do_Visual_Imaginations_Improve_Vision-and-Language_Navigation_Agents_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.16394) · 인용 23회

**주제:** Navigation · Embodied Perception

## 문제
VLN agent가 unseen environment에서 자연어 instruction만으로 navigation할 때, instruction에 암시된 sub-goal의 시각적 단서를 활용하면 성능을 향상시킬 수 있는지 검증하는 문제를 다룬다.

## 핵심 아이디어
segmented instruction의 landmark reference에 대해 text-to-image diffusion model로 visual imagination을 생성하고, 이를 navigation cue로 제공하며 referring expression과 연관짓도록 auxiliary loss를 추가한다.

## 방법
Instruction을 segment하고 landmark reference를 추출한 뒤 text-to-image diffusion model로 sub-goal visual representation을 합성한다. 생성된 imagination을 VLN agent의 추가 modality로 입력하고, 해당 referring expression과의 관계를 학습하도록 auxiliary loss를 부여한다. 여러 agent에 적용해 language instruction만 사용하는 baseline과 navigation 성능을 비교한다.

## 결과
제안 방법은 agent 전반에서 success rate (SR)를 약 1 point, success scaled by inverse path length (SPL)를 최대 약 0.5 point 향상시켰으며, 이는 language instruction만 의존할 때보다 visual understanding을 강화함을 시사한다.

## 초록 (원문)
Vision-and-Language Navigation (VLN) agents are tasked with navigating an unseen environment using natural language instructions. In this work, we study if visual representations of sub-goals implied by the instructions can serve as navigational cues and lead to increased navigation performance. To synthesize these visual representations or "imaginations", we leverage a text-to-image diffusion model on landmark references contained in segmented instructions. These imaginations are provided to VLN agents as an added modality to act as landmark cues and an auxiliary loss is added to explicitly encourage relating these with their corresponding referring expressions. Our findings reveal an increase in success rate (SR) of ~1 point and up to ~0.5 points in success scaled by inverse path length (SPL) across agents. These results suggest that the proposed approach reinforces visual understanding compared to relying on language instructions alone.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
