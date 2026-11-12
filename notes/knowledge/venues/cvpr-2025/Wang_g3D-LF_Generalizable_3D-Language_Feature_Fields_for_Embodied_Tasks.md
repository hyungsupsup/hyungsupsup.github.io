---
title: "g3D-LF: Generalizable 3D-Language Feature Fields for Embodied Tasks"
tags: [cvpr2025, embodied-perception, navigation, dataset-benchmark]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** g3D-LF는 대규모 3D-language 데이터로 사전학습되어 embodied tasks에서 novel view 표현, agent 중심 BEV map, multi-granularity language query를 지원하는 generalizable 3D-language feature field 모델이다.

**CVPR 2025** · Zihan Wang, Gim Hee Lee
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_g3D-LF_Generalizable_3D-Language_Feature_Fields_for_Embodied_Tasks_CVPR_2025_paper.html)

**주제:** Embodied Perception · Navigation · Dataset & Benchmark

## 문제
Embodied agent가 unseen environment에서도 실시간으로 구축·동적 업데이트 가능한 3D 표현을 얻고, 이를 multi-granularity language와 정렬하여 target을 query하는 문제를 해결한다.

## 핵심 아이디어
Sampled ray를 따라 latent feature를 volume rendering하고 multiscale encoder로 semantic/spatial 관계를 통합하며, multi-level contrastive learning으로 feature field를 multi-granularity language와 정렬하는 것이 핵심이다.

## 방법
Agent의 posed RGB-D 이미지를 입력으로 받아 3D scene 내 임의 위치의 novel view representation과 agent 중심 BEV map을 생성한다. Volume rendering과 multiscale encoding을 통해 다양한 scale/perspective의 표현을 만들고, 대규모 3D-language dataset으로 language 정렬을 학습한다. 이를 통해 unseen environment로 generalization되고 real-time construction 및 dynamic update가 가능하다.

## 결과
Panorama 및 Monocular 설정의 Vision-and-Language Navigation, Zero-shot Object Navigation, Situated Question Answering 실험에서 g3D-LF의 우수성과 효과를 보였다.

## 초록 (원문)
We introduce Generalizable 3D-Language Feature Fields (g3D-LF), a 3D representation model pre-trained on large-scale 3D-language dataset for embodied tasks. Our g3D-LF processes posed RGB-D images from agents to encode feature fields for: 1) Novel view representation predictions from any position in the 3D scene; 2) Generations of BEV maps centered on the agent; 3) Querying targets using multi-granularity language within the above-mentioned representations. Our representation can be generalized to unseen environments, enabling real-time construction and dynamic updates. By volume rendering latent features along sampled rays and integrating semantic and spatial relationships through multiscale encoders, our g3D-LF produces representations at different scales and perspectives, aligned with multi-granularity language, via multi-level contrastive learning. Furthermore, we prepare a large-scale 3D-language dataset to align the representations of the feature fields with language. Extensive experiments on Vision-and-Language Navigation under both Panorama and Monocular settings, Zero-shot Object Navigation, and Situated Question Answering tasks highlight the significant advantages and effectiveness of our g3D-LF for embodied tasks. Our source code and dataset will be made open-source upon paper acceptance.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
