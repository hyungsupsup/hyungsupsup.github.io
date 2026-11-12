---
title: "Mitigating the Human-Robot Domain Discrepancy in Visual Pre-training for Robotic Manipulation"
tags: [cvpr2025, manipulation, embodied-perception]
venue: CVPR 2025
arxiv: "2406.14235"
citations: 38
auto: true
---

> **TL;DR** 인간-로봇 비디오 쌍을 활용한 contrastive alignment로 visual pre-training 모델의 human-robot domain discrepancy를 줄여 robotic manipulation 성능을 향상시키는 방법을 제안한다.

**CVPR 2025** · Jiaming Zhou, Teli Ma, Kun-Yu Lin, Zifan Wang, Ronghe Qiu, Junwei Liang
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Zhou_Mitigating_the_Human-Robot_Domain_Discrepancy_in_Visual_Pre-training_for_Robotic_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2406.14235) · 인용 38회

**주제:** Manipulation · Embodied Perception

## 문제
로봇 데모 데이터는 규모와 다양성이 부족해 대규모 인간 활동 데이터로 pre-training하지만, 인간과 로봇의 형태 차이로 인한 human-robot domain discrepancy가 downstream manipulation 일반화를 저해한다.

## 핵심 아이디어
쉽게 얻을 수 있는 paired human-robot video data를 사용해 human-robot contrastive alignment loss로 인간/로봇 비디오의 semantics를 정렬하고, pre-trained model을 parameter-efficient하게 robot domain에 적응시킨다.

## 방법
Paired human-robot video에서 human과 robot 비디오의 semantic을 contrastive alignment loss로 맞춘다. 이를 통해 기존 pre-trained visual model을 robot domain으로 parameter-efficient하게 adaptation한다. Simulated benchmarks와 real-world manipulation tasks에서 single-task 및 language-conditioned multi-task 설정으로 평가한다.

## 결과
20 simulated tasks across two benchmarks와 five real-world tasks에서 기존 pre-trained model 대비 average success rate를 over 7% 향상시켰다.

## 연결
- **기반 대표 논문:** ACT / ALOHA, Diffusion Policy, Open X-Embodiment (데이터셋), PPO — Proximal Policy Optimization, RT-1, RT-2 — [[knowledge/map|분야 지도]]

## 초록 (원문)
Learning generalizable visual representations across different embodied environments is essential for effective robotic manipulation in real-world scenarios. However, the limited scale and diversity of robot demonstration data pose a significant challenge. Recent research has explored leveraging large-scale human activity data for pre-training, but the substantial morphological differences between humans and robots introduce a significant human-robot domain discrepancy, hindering the generalization of these models to downstream manipulation tasks. To overcome this, we propose a novel adaptation paradigm that leverages readily available paired human-robot video data to bridge the domain gap. Our method employs a human-robot contrastive alignment loss to align the semantics of human and robot videos, adapting pre-trained models to the robot domain in a parameter-efficient manner. Experiments on 20 simulated tasks across two different benchmarks and five real-world tasks demonstrate significant improvements. These results span both single-task and language-conditioned multi-task settings, evaluated using two different pre-trained models. Compared to existing pre-trained models, our adaptation method improves the average success rate by over 7% across multiple tasks on both simulated benchmarks and real-world evaluations.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
