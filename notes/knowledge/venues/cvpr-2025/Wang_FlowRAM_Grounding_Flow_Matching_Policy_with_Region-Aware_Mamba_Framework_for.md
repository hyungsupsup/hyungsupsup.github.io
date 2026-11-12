---
title: "FlowRAM: Grounding Flow Matching Policy with Region-Aware Mamba Framework for Robotic Manipulation"
tags: [cvpr2025, manipulation, imitation-learning]
venue: CVPR 2025
arxiv: "2506.16201"
citations: 21
auto: true
---

> **TL;DR** FlowRAM은 region-aware Mamba와 conditional flow matching을 결합해 고정밀 로봇 조작을 빠르고 효율적으로 수행하는 정책 학습 프레임워크이다.

**CVPR 2025** · Sen Wang, Le Wang, Sanping Zhou, Jingyi Tian, Jiayi Li, Haowen Sun 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_FlowRAM_Grounding_Flow_Matching_Policy_with_Region-Aware_Mamba_Framework_for_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2506.16201) · 인용 21회

**주제:** Manipulation · Imitation Learning

## 문제
기존 diffusion 기반 정책 학습은 추론 시 반복적 denoising 때문에 계산 효율이 낮고, 3D 환경에서 생성 모델의 정보 탐색 잠재력을 충분히 활용하지 못한다.

## 핵심 아이디어
Dynamic Radius Schedule로 global scene에서 fine-grained geometry로 전환하는 adaptive perception을 수행하고, state space model로 multimodal 정보를 선형 복잡도로 통합하며, conditional flow matching으로 deterministic vector field를 회귀해 action pose를 학습한다.

## 방법
FlowRAM은 Dynamic Radius Schedule을 통해 영역 인식형 3D 지각을 적응적으로 수행한다. 이어 state space model을 사용해 multimodal 정보를 선형 계산 복잡도로 통합하고, conditional flow matching으로 action pose를 deterministic vector field 회귀 방식으로 학습한다.

## 결과
RLBench에서 state-of-the-art 성능을 달성했으며, 특히 고정밀 작업에서 기존 방법보다 평균 success rate가 12.0% 향상되었다. 또한 다양한 real-world 작업에서 4 time steps 미만으로 physically plausible한 action을 생성해 inference speed를 크게 높인다.

## 연결
- **기반 대표 논문:** ACT / ALOHA, BC-Z, DDPM, Diffusion Policy, Gato, Octo, PaLM-E, RT-1 — [[knowledge/map|분야 지도]]

## 초록 (원문)
Robotic manipulation in high-precision tasks is essential for numerous industrial and real-world applications where accuracy and speed are required. Yet current diffusion-based policy learning methods generally suffer from low computational efficiency due to the iterative denoising process during inference. Moreover, these methods do not fully explore the potential of generative models for enhancing information exploration in 3D environments. In response, we propose FlowRAM, a novel framework that leverages generative models to achieve region-aware perception, enabling efficient multimodal information processing. Specifically, we devise a Dynamic Radius Schedule, which enables adaptive perception, facilitating transitions from global scene comprehension to fine-grained geometric details. Furthermore, we integrate state space models to integrate multimodal information, while preserving linear computational complexity. In addition, we employ conditional flow matching to learn action poses by regressing deterministic vector fields, which simplifies the learning process while maintaining performance. We verify the effectiveness of the FlowRAM in the RLBench, an established manipulation benchmark, and achieve state-of-the-art performance. The results demonstrate that FlowRAM achieves a remarkable improvement, particularly in high-precision tasks, where it outperforms previous methods by 12.0% in average success rate. Additionally, FlowRAM is able to generate physically plausible actions for a variety of real-world tasks in less than 4 time steps, significantly increasing inference speed.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
