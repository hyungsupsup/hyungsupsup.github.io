---
title: "ECBench: Can Multi-modal Foundation Models Understand the Egocentric World? A Holistic Embodied Cognition Benchmark"
tags: [cvpr2025, dataset-benchmark, embodied-perception]
venue: CVPR 2025
arxiv: "2501.05031"
citations: 36
auto: true
---

> **TL;DR** ECBench는 egocentric video 기반 LVLM의 embodied cognition 능력을 30개 차원에서 체계적으로 평가하는 benchmark와 ECEval 평가 체계를 제안한다.

**CVPR 2025** · Ronghao Dang, Yuqian Yuan, Wenqi Zhang, Yifei Xin, Boqiang Zhang, Long Li 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Dang_ECBench_Can_Multi-modal_Foundation_Models_Understand_the_Egocentric_World_A_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2501.05031) · 인용 36회

**주제:** Dataset & Benchmark · Embodied Perception

## 문제
기존 embodied video question answering 데이터셋은 포괄적이고 체계적인 평가 프레임워크가 부족하며, robotic self-cognition, dynamic scene perception, hallucination 같은 핵심 embodied cognition 문제를 거의 다루지 못한다.

## 핵심 아이디어
ECBench는 다양한 scene video source와 개방형·다양한 질문 형식, 30 dimensions of embodied cognition을 갖춘 고품질 benchmark이며, class-independent meticulous human annotation과 multi-round question screening으로 품질·균형·높은 visual dependence를 확보한다. 또한 ECEval을 도입해 지표의 공정성과 합리성을 보장한다.

## 방법
ECBench는 egocentric video에 대한 question answering 형태로 LVLM의 embodied cognitive abilities를 평가하며, 30 dimensions of embodied cognition을 기준으로 구성된다. 데이터 품질 관리를 위해 human annotation과 multi-round question screening 전략을 사용하고, ECEval로 포괄적이고 공정한 평가를 수행한다. 이를 통해 proprietary, open-source, task-specific LVLMs를 광범위하게 평가한다.

## 결과
ECBench를 활용해 proprietary, open-source, task-specific LVLMs에 대한 광범위한 평가를 수행했으며, LVLM의 embodied cognitive capabilities를 발전시키고 embodied agents를 위한 신뢰할 수 있는 core models 개발의 기반을 마련하는 데 기여한다고 주장한다.

## 초록 (원문)
The enhancement of generalization in robots by large vision-language models (LVLMs) is increasingly evident. Therefore, the embodied cognitive abilities of LVLMs based on egocentric videos are of great interest. However, current datasets for embodied video question answering lack comprehensive and systematic evaluation frameworks. Critical embodied cognitive issues, such as robotic self-cognition, dynamic scene perception, and hallucination, are rarely addressed. To tackle these challenges, we propose ECBench, a high-quality benchmark designed to systematically evaluate the embodied cognitive abilities of LVLMs. ECBench features a diverse range of scene video sources, open and varied question formats, and 30 dimensions of embodied cognition. To ensure quality, balance, and high visual dependence, ECBench uses class-independent meticulous human annotation and multi-round question screening strategies. Additionally, we introduce ECEval, a comprehensive evaluation system that ensures the fairness and rationality of the indicators. Utilizing ECBench, we conduct extensive evaluations of proprietary, open-source, and task-specific LVLMs. ECBench is pivotal in advancing the embodied cognitive capabilities of LVLMs, laying a solid foundation for developing reliable core models for embodied agents. All data and code is available at https://github.com/Rh-Dang/ECBench.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
