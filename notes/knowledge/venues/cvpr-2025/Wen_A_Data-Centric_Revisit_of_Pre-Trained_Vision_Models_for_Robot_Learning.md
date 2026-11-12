---
title: "A Data-Centric Revisit of Pre-Trained Vision Models for Robot Learning"
tags: [cvpr2025, embodied-perception, other]
venue: CVPR 2025
arxiv: "2503.06960"
citations: 9
auto: true
---

> **TL;DR** 로봇 학습용 pre-trained vision model(PVM)의 최적 구성과 object-centric representation의 중요성을 분석하고 SlotMIM을 제안한 데이터 중심 연구이다.

**CVPR 2025** · Xin Wen, Bingchen Zhao, Yilun Chen, Jiangmiao Pang, Xiaojuan Qi
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Wen_A_Data-Centric_Revisit_of_Pre-Trained_Vision_Models_for_Robot_Learning_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.06960) · 인용 9회

**주제:** Embodied Perception · Other

## 문제
PVM이 로봇 학습에서 어떤 설정이 최적인지 불명확하며, DINO와 iBOT 등이 non-(single-)object-centric 데이터에서 성능이 떨어지는 문제를 다룬다.

## 핵심 아이디어
non-object-centric 로봇 데이터에서 object-centric representation을 형성하는 능력이 PVM 성공의 핵심임을 발견하고, semantic bottleneck과 cross-view consistency regularization으로 objectness를 유도한다.

## 방법
SlotMIM은 prototype 수를 줄이는 semantic bottleneck을 도입해 object-centric representation의 출현을 유도하고, cross-view consistency regularization으로 multiview invariance를 장려한다. object-centric, scene-centric, web-crawled, ego-centric 데이터로 pre-training하고 image recognition, scene understanding, robot learning에서 평가한다.

## 결과
DINO와 iBOT은 visuomotor control과 perception에서 MAE를 능가하지만 NOC 데이터에서는 한계를 보였고, SlotMIM은 모든 설정에서 prior work 대비 significant improvements를 달성했다. million-scale datasets로 확장할 때 superior data efficiency and scalability도 보였다.

## 연결
- **기반 대표 논문:** Octo, OpenVLA, RT-1, RT-2 — [[knowledge/map|분야 지도]]

## 초록 (원문)
Pre-trained vision models (PVMs) are fundamental to modern robotics, yet their optimal configuration remains unclear. Through systematic evaluation, we find that while DINO and iBOT outperform MAE across visuomotor control and perception tasks, they struggle when trained on non-(single-)object-centric (NOC) data--a limitation strongly correlated with their diminished ability to learn object-centric representations. This investigation indicates that the ability to form object-centric representations from the non-object-centric robotics dataset is the key to success for PVMs. Motivated by this discovery, we designed SlotMIM, a method that induces object-centric representations by introducing a semantic bottleneck to reduce the number of prototypes to encourage the emergence of objectness as well as cross-view consistency regularization for encouraging multiview invariance. Our experiments encompass pre-training on object-centric, scene-centric, web-crawled, and ego-centric data. Across all settings, our approach learns transferrable representations and achieves significant improvements over prior work in image recognition, scene understanding, and robot learning evaluations. When scaled up with million-scale datasets, our method also demonstrates superior data efficiency and scalability. Our code and models are publicly available at https://github.com/CVMI-Lab/SlotMIM.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
