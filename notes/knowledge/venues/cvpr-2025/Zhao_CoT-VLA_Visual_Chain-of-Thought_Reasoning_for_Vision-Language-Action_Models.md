---
title: "CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models"
tags: [cvpr2025, vla, manipulation, world-model]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** CoT-VLA는 미래 이미지 프레임을 visual goal로 예측한 뒤 action sequence를 생성하는 visual chain-of-thought 기반 7B VLA 모델이다.

**CVPR 2025** · Qingqing Zhao, Yao Lu, Moo Jin Kim, Zipeng Fu, Zhuoyang Zhang, Yecheng Wu 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.html)

**주제:** VLA · Manipulation · World Model

## 문제
기존 VLA 모델은 직접적인 입력-출력 매핑에 집중해 복잡한 manipulation 작업에 필요한 중간 추론과 temporal planning 능력이 부족하다.

## 핵심 아이디어
action을 바로 생성하기 전에 미래 이미지 프레임을 autoregressive하게 예측해 visual goal로 사용하는 explicit visual chain-of-thought reasoning을 VLA에 도입한다.

## 방법
CoT-VLA는 visual token과 action token을 이해하고 생성할 수 있는 7B VLA로, 미래 이미지 프레임을 visual goal로 예측한 뒤 그 목표를 달성하기 위한 짧은 action sequence를 생성한다.

## 결과
실험 결과 CoT-VLA는 real-world manipulation tasks에서 state-of-the-art VLA 모델보다 17%, simulation benchmarks에서 6% 더 높은 성능을 보였다.

## 초록 (원문)
Vision-language-action models (VLAs) have shown potential in leveraging pretrained vision-language models and diverse robot demonstrations for learning generalizable sensorimotor control. While this paradigm effectively utilizes large-scale data from both robotic and non-robotic sources, current VLAs primarily focus on direct input--output mappings, lacking the intermediate reasoning steps crucial for complex manipulation tasks. As a result, existing VLAs lack temporal planning or reasoning capabilities. In this paper, we introduce a method that incorporates explicit visual chain-of-thought (CoT) reasoning into vision-language-action models (VLAs) by predicting future image frames autoregressively as visual goals before generating a short action sequence to achieve these goals. We introduce CoT-VLA, a state-of-the-art 7B VLA that can understand and generate visual and action tokens. Our experimental results demonstrate that CoT-VLA achieves strong performance, outperforming the state-of-the-art VLA model by 17% in real-world manipulation tasks and 6% in simulation benchmarks. Videos are available at: https://cot-vla.github.io/.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
