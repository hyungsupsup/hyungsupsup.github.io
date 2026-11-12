---
title: "Prior Does Matter: Visual Navigation via Denoising Diffusion Bridge Models"
tags: [cvpr2025, navigation, imitation-learning]
venue: CVPR 2025
arxiv: "2504.10041"
citations: 35
auto: true
---

> **TL;DR** NaviBridger는 Gaussian noise 대신 informative prior action에서 시작하는 denoising diffusion bridge model 기반 visual navigation 프레임워크다.

**CVPR 2025** · Hao Ren, Yiming Zeng, Zetong Bi, Zhaoliang Wan, Junlong Huang, Hui Cheng
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Ren_Prior_Does_Matter_Visual_Navigation_via_Denoising_Diffusion_Bridge_Models_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2504.10041) · 인용 35회

**주제:** Navigation · Imitation Learning

## 문제
기존 diffusion 기반 visual navigation 정책은 Gaussian noise에서 action sequence 생성을 시작해 target action distribution과의 큰 차이로 인해 불필요한 denoising step과 학습 복잡성이 발생하며, sparse한 유효 action 분포 때문에 guidance 없이 정확한 action을 생성하기 어렵다.

## 핵심 아이디어
denoising diffusion bridge models를 활용해 임의의 informative prior action에서 action 생성을 시작함으로써 denoising 과정의 guidance와 효율성을 높이는 unified visual navigation framework를 제안한다. 또한 prior action을 생성하기 위한 세 가지 source policy를 탐구한다.

## 방법
NaviBridger는 visual navigation에서 imitation learning을 diffusion bridge로 수행하며, Gaussian noise가 아닌 informative prior action을 초기값으로 사용해 target action sequence를 생성한다. prior action 생성을 위해 세 가지 source policy를 검토하고, simulated 및 real-world indoor/outdoor 환경에서 실험한다.

## 결과
Simulated 및 real-world indoor/outdoor 시나리오에서 NaviBridger는 policy inference를 가속화하고 baselines보다 target action sequence 생성에서 우수한 성능을 보인다.

## 연결
- **기반 대표 논문:** DDPM, Diffusion Policy — [[knowledge/map|분야 지도]]

## 초록 (원문)
Recent advancements in diffusion-based imitation learning, which shows impressive performance in modeling multimodal distributions and training stability, have led to substantial progress in various robot learning tasks. In visual navigation, previous diffusion-based policies typically generate action sequences by initiating from denoising Gaussian noise. However, the target action distribution often diverges significantly from Gaussian noise, leading to redundant denoising steps and increased learning complexity. Additionally, the sparsity of effective action distributions makes it challenging for the policy to generate accurate actions without guidance. To address these issues, we propose a novel, unified visual navigation framework leveraging the denoising diffusion bridge models named NaviBridger. This approach enables action generation by initiating from any informative prior actions, enhancing guidance and efficiency in the denoising process. We explore how diffusion bridges can enhance imitation learning in visual navigation tasks and further examine three source policies for generating prior actions. Extensive experiments in both simulated and real-world indoor and outdoor scenarios demonstrate that NaviBridger accelerates policy inference and outperforms the baselines in generating target action sequences. Code is available at https://github.com/hren20/NaiviBridger.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
