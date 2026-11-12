---
title: "Learning to Detect Objects from Multi-Agent LiDAR Scans without Manual Labels"
tags: [cvpr2025, autonomous-driving, embodied-perception]
venue: CVPR 2025
arxiv: "2503.08421"
citations: 13
auto: true
---

> **TL;DR** 다중 에이전트 LiDAR 스캔에서 수동 라벨 없이 3D 객체를 검출하는 비지도 방법 DOtA를 제안한다.

**CVPR 2025** · Qiming Xia, Wenkai Lin, Haoen Xiang, Xun Huang, Siheng Chen, Zhen Dong 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Xia_Learning_to_Detect_Objects_from__Multi-Agent_LiDAR_Scans_without_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.08421) · 인용 13회

**주제:** Autonomous Driving · Embodied Perception

## 문제
기존 비지도 3D 객체 검출은 데이터 희소성과 제한된 시점 때문에 클러스터링 기반 의사 라벨의 품질이 낮다. 다중 에이전트의 상호보완적 관측을 활용해 이 병목을 완화하는 것이 목표다.

## 핵심 아이디어
에이전트 간 공유되는 ego-pose와 ego-shape로 검출기를 초기화해 예비 라벨을 만들고, 상호보완 관측을 multi-scale encoding/decoding해 고품질·저품질 라벨을 구분해 prompt로 활용한다.

## 방법
DOtA는 협력 에이전트의 내부 공유 ego-pose와 ego-shape를 이용해 detector를 초기화하고 신경망의 일반화 성능으로 preliminary labels를 추론한다. 이후 에이전트 간 complementary observations로 preliminary labels를 multi-scale encoding한 뒤 high-quality 및 low-quality labels로 decode한다. 이 라벨들을 prompt로 삼아 올바른 feature learning을 유도해 비지도 객체 검출 성능을 높인다.

## 결과
V2V4Real과 OPV2V에서 DOtA가 state-of-the-art unsupervised 3D object detection 방법들을 능가함을 보였고, 다양한 collaborative perception 프레임워크에서 DOtA 라벨의 효과도 검증했다.

## 초록 (원문)
Unsupervised 3D object detection serves as an important solution for offline 3D object annotation. However, due to the data sparsity and limited views, the clustering-based label fitting in unsupervised object detection often generates low-quality pseudo-labels. Multi-agent collaborative dataset, which involves the sharing of complementary observations among agents, holds the potential to break through this bottleneck. In this paper, we introduce a novel unsupervised method that learns to Detect Objects from Multi-Agent LiDAR scans, termed DOtA, without using labels from external. DOtA first uses the internally shared ego-pose and ego-shape of collaborative agents to initialize the detector, leveraging the generalization performance of neural networks to infer preliminary labels. Subsequently, DOtA uses the complementary observations between agents to perform multi-scale encoding on preliminary labels, then decodes high-quality and low-quality labels. These labels are further used as prompts to guide a correct feature learning process, thereby enhancing the performance of the unsupervised object detection task. Extensive experiments on the V2V4Real and OPV2V datasets show that our DOtA outperforms state-of-the-art unsupervised 3D object detection methods. Additionally, we also validate the effectiveness of the DOtA labels under various collaborative perception frameworks. The code is available at https://github.com/xmuqimingxia/DOtA.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
