---
title: "DiSRT-In-Bed: Diffusion-Based Sim-to-Real Transfer Framework for In-Bed Human Mesh Recovery"
tags: [cvpr2025, simulation-sim2real, embodied-perception]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** Overhead depth 이미지로부터 침대 위 인체 mesh를 복원하기 위해 대규모 synthetic data와 diffusion 기반 sim-to-real 전이를 활용하는 프레임워크를 제안한다.

**CVPR 2025** · Jing Gao, Ce Zheng, Laszlo A. Jeni, Zackory Erickson
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Gao_DiSRT-In-Bed_Diffusion-Based_Sim-to-Real_Transfer_Framework_for_In-Bed_Human_Mesh_Recovery_CVPR_2025_paper.html)

**주제:** Simulation & Sim2Real · Embodied Perception

## 문제
침대 위 인체 mesh 복원은 수면 모니터링, 재활 지원, 욕창 예방 등 healthcare 응용에 중요하지만, privacy와 비용 제약으로 대규모 실제 데이터를 수집하기 어렵고 기존 방법은 실제 데이터 의존도가 높아 다양한 침대 환경으로 일반화하기 어렵다.

## 핵심 아이디어
대규모 synthetic data와 제한적이거나 전혀 없는 real sample을 함께 활용하고, diffusion model로 synthetic data와 real data 사이의 gap을 연결해 실제 침대 자세 및 신체 추론의 일반화를 지원한다.

## 방법
Overhead depth images를 입력으로 in-bed human mesh recovery를 수행한다. Diffusion model이 synthetic data와 real data 사이의 domain gap을 bridge하도록 학습되어 real-world in-bed pose 및 body inference로 전이된다. Extensive experiments와 ablation studies로 다양한 healthcare scenario에서의 robustness와 adaptability를 검증한다.

## 결과
Extensive experiments와 ablation studies를 통해 framework의 효과를 검증했으며, 다양한 healthcare scenario에서 robustness와 adaptability가 significant improvements를 보였다고 주장한다.

## 초록 (원문)
In-bed human mesh recovery can be crucial and enabling for several healthcare applications, including sleep pattern monitoring, rehabilitation support, and pressure ulcer prevention. However, it is difficult to collect large real-world visual datasets in this domain, in part due to privacy and expense constraints, which in turn presents significant challenges for training and deploying deep learning models. Existing in-bed human mesh estimation methods often rely heavily on real-world data, limiting their ability to generalize across different in-bed scenarios, such as varying coverings and environmental settings. To address this, we propose a Sim-to-Real Transfer Framework for in-bed human mesh recovery from overhead depth images, which leverages large-scale synthetic data alongside limited or no real-world samples. We introduce a diffusion model that bridges the gap between synthetic data and real data to support generalization in real-world in-bed pose and body inference scenarios. Extensive experiments and ablation studies validate the effectiveness of our framework, demonstrating significant improvements in robustness and adaptability across diverse healthcare scenarios. Project page can be found at https://jing-g2.github.io/DiSRT-In-Bed/.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
