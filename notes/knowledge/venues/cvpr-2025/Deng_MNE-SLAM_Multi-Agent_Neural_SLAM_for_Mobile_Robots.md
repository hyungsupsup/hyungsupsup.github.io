---
title: "MNE-SLAM: Multi-Agent Neural SLAM for Mobile Robots"
tags: [cvpr2025, embodied-perception, dataset-benchmark]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** 모바일 로봇을 위한 최초의 분산 다중 에이전트 협업 neural SLAM 프레임워크와 단일/다중 에이전트 실내 INS 데이터셋을 제안한다.

**CVPR 2025** · Tianchen Deng, Guole Shen, Chen Xun, Shenghai Yuan, Tongxin Jin, Hongming Shen 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Deng_MNE-SLAM_Multi-Agent_Neural_SLAM_for_Mobile_Robots_CVPR_2025_paper.html)

**주제:** Embodied Perception · Dataset & Benchmark

## 문제
기존 neural implicit SLAM은 단일 에이전트에 국한되어 대규모 실내 장면과 긴 시퀀스에서 어려움을 겪고, 기존 다중 에이전트 SLAM은 통신 대역폭 제약을 충족하지 못한다. 또한 NeRF/GS 기반 SLAM용 실세계 데이터셋은 연속시간 궤적과 고정밀 3D mesh ground truth를 함께 제공하지 않는다.

## 핵심 아이디어
peer-to-peer 통신만으로 동작하는 분산 neural mapping/tracking과 intra-to-inter loop closure, multi-submap fusion을 결합해 다중 에이전트 협업과 통신 효율을 높인다. 또한 단일/다중 에이전트 실내 장면을 포함한 최초의 실세계 INS 데이터셋을 제공한다.

## 방법
각 에이전트가 분산적으로 neural map과 camera tracking을 수행하고 peer-to-peer 통신으로 joint scene representation을 공유한다. intra-to-inter loop closure로 에이전트 내부 및 에이전트 간 일관성을 확보하고 multi-submap fusion으로 전역 지도를 구성한다. 제안 데이터셋은 고정밀 3D mesh와 연속시간 camera trajectory ground truth를 제공한다.

## 결과
다양한 데이터셋 실험에서 제안 방법이 mapping, tracking, communication 측면에서 우수함을 보인다. 데이터셋과 코드는 공개될 예정이다.

## 초록 (원문)
Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulty in large indoor scenes and long sequences. Existing multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this end, we propose the first distributed multi-agent collaborative SLAM framework with distributed mapping and camera tracking, joint scene representation, intra-to-inter loop closure, and multi-submap fusion. Specifically, our proposed distributed neural mapping and tracking framework only needs peer-to-peer communication, which can greatly improve multi-agent cooperation and communication efficiency. A novel intra-to-inter loop closure method is designed to achieve local (single-agent) and global (multi-agent) consistency. Furthermore, to the best of our knowledge, there is no real-world dataset for NeRF-based/GS-based SLAM that provides both continuous-time trajectories groundtruth and high-accuracy 3D meshes groundtruth. To this end, we propose the first real-world indoor neural slam (INS) dataset covering both single-agent and multi-agent scenarios, ranging from small room to large-scale scenes, with high-accuracy ground truth for both 3D mesh and continuous-time camera trajectory. This dataset can advance the development of the community. Experiments on various datasets demonstrate the superiority of the proposed method in both mapping, tracking, and communication. The dataset and code will be open-source on https://github.com/dtc111111/MNESLAM.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
