---
title: "AffordDP: Generalizable Diffusion Policy with Transferable Affordance"
tags: [cvpr2025, manipulation, imitation-learning, embodied-perception]
venue: CVPR 2025
arxiv: "2412.03142"
citations: 57
auto: true
---

> **TL;DR** AffordDP는 transferable affordance를 활용해 새로운 객체와 카테고리로 일반화되는 diffusion policy를 제안한다.

**CVPR 2025** · Shijie Wu, Yihang Zhu, Yunao Huang, Kaizhen Zhu, Jiayuan Gu, Jingyi Yu 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_AffordDP_Generalizable_Diffusion_Policy_with_Transferable_Affordance_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2412.03142) · 인용 57회

**주제:** Manipulation · Imitation Learning · Embodied Perception

## 문제
Diffusion-based policy는 robotic manipulation에서 성능이 좋지만 out-of-domain 분포와 unseen object/category에 대한 일반화에 어려움을 겪는다. 기존의 visual feature encoding 개선은 주로 같은 카테고리나 유사한 외형에 국한된 일반화를 제공한다.

## 핵심 아이디어
Affordance를 '어디서' '어떻게' 상호작용하는지에 대한 manipulation prior로 보고, 이를 3D contact points와 post-contact trajectories로 모델링해 완전히 새로운 객체 인스턴스와 카테고리로 전이한다. In-domain affordance를 foundational vision models와 point cloud registration 기반 6D transformation matrix로 unseen objects에 transfer한다.

## 방법
AffordDP는 affordance를 3D contact points와 post-contact trajectories로 표현해 복잡한 task의 static/dynamic 정보를 포착한다. Transferable affordance는 foundational vision models와 point cloud registration을 이용해 6D transformation matrix를 추정함으로써 in-domain data에서 unseen objects로 전이된다. 또한 diffusion sampling 중 affordance guidance를 적용해 생성된 action sequence가 action space의 manifold를 유지하면서 원하는 manipulation으로 점진적으로 이동하도록 refine한다.

## 결과
Simulated 및 real-world 환경 실험에서 AffordDP는 이전 diffusion-based 방법들을 일관되게 능가하며, 다른 방법들이 실패하는 unseen instances와 categories로 성공적으로 일반화한다.

## 연결
- **기반 대표 논문:** Diffusion Policy, RT-1 — [[knowledge/map|분야 지도]]
- 인용함 → [[knowledge/venues/cvpr-2025/Wu_MoManipVLA_Transferring_Vision-language-action_Models_for_General_Mobile_Manipulation|MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation]]
- 인용함 → [[knowledge/venues/cvpr-2025/Yu_SeqAfford_Sequential_3D_Affordance_Reasoning_via_Multimodal_Large_Language_Model|SeqAfford: Sequential 3D Affordance Reasoning via Multimodal Large Language Model]]
- 인용함 → [[knowledge/venues/cvpr-2025/Chen_G3Flow_Generative_3D_Semantic_Flow_for_Pose-aware_and_Generalizable_Object|G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizable Object Manipulation]]
- 인용됨 ← [[knowledge/venues/cvpr-2025/Yu_SeqAfford_Sequential_3D_Affordance_Reasoning_via_Multimodal_Large_Language_Model|SeqAfford: Sequential 3D Affordance Reasoning via Multimodal Large Language Model]]

## 초록 (원문)
Diffusion-based policies have shown impressive performance in robotic manipulation tasks while struggling with out-of-domain distributions. Recent efforts attempted to enhance generalization by improving the visual feature encoding for diffusion policy. However, their generalization is typically limited to the same category with similar appearances. Our key insight is that leveraging affordances--manipulation priors that define "where" and "how" an agent interacts with an object--can substantially enhance generalization to entirely unseen object instances and categories. We introduce the Diffusion Policy with transferable Affordance (AffordDP), designed for generalizable manipulation across novel categories. AffordDP models affordances through 3D contact points and post-contact trajectories, capturing the essential static and dynamic information for complex tasks. The transferable affordance from in-domain data to unseen objects is achieved by estimating a 6D transformation matrix using foundational vision models and point cloud registration techniques. More importantly, we incorporate affordance guidance during diffusion sampling that can refine action sequence generation. This guidance directs the generated action to gradually move towards the desired manipulation for unseen objects while keeping the generated action within the manifold of action space. Experimental results from both simulated and real-world environments demonstrate that AffordDP consistently outperforms previous diffusion-based methods, successfully generalizing to unseen instances and categories where others fail.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
