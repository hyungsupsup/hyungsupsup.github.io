---
title: "Mixture of Experts"
date: 2026-11-24
tags: [technique, efficiency]
category: "효율화·적응"
status: draft
---

> MoE는 큰 병원에 전문의가 많지만, 접수대(라우터)가 환자마다 필요한 전문의 1~2명만 부르는 방식이다.

**대표 논문**: Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer (2017) · **분류**: 효율화·적응

## 해결한 문제
기존 dense 모델은 모든 입력마다 모델의 모든 파라미터를 다 계산해야 해서, 모델을 키우면 계산량과 비용이 그대로 커진다. 그래서 큰 모델의 지식을 쓰면서도 실제 추론 속도는 유지하기 어려웠다.

## 핵심 아이디어
MoE는 여러 개의 전문가(expert, 보통 FFN 같은 작은 계산 블록)를 두고, 라우터(gating network, 입력마다 어떤 전문가를 쓸지 고르는 작은 네트워크)가 가장 잘 맞는 전문가 몇 개만 고른다. 입력은 선택된 전문가들만 거치고, 각 전문가의 출력은 라우터가 준 가중치로 합쳐진다. 즉 모델 전체는 크지만, 한 번에 활성화되는 부분은 일부만이다.

## 왜 작동하나
모든 전문가를 다 쓰지 않고 필요한 전문가만 쓰면, 큰 모델의 용량을 유지하면서도 계산량은 dense 모델보다 줄일 수 있다. 또 서로 다른 전문가가 다른 패턴을 담당하면, 같은 크기의 dense 모델보다 더 다양한 지식을 효율적으로 나눌 수 있다.

## 트레이드오프
- 총 파라미터는 여전히 크므로 GPU 메모리에 모든 전문가를 올려야 할 수 있다.
- 라우터가 특정 전문가만 계속 쓰면 병목이 생기고, 안 쓰면 낭비가 되므로 load balancing이 필요하다.
- 전문가가 여러 GPU에 흩어져 있으면 통신 비용이 커져서 실제 속도가 기대만큼 안 나올 수 있다.

## 계보
**이전**
- Dense Transformer FFN
- Hierarchical Mixture of Experts
- Ensemble models

**이후**
- Switch Transformer
- GShard
- Mixtral
- DeepSeek MoE
- Mixture-of-Depths

## 피지컬 AI에서의 쓰임
- VLA(비전-언어-행동) 모델에서 물체 인식, 경로 계획, 파지 동작 같은 전문가를 나눠 상태마다 일부만 활성화한다.
- 로봇 월드모델에서 실내/야외/충돌 상황 같은 조건별 전문가를 라우팅해 계산량을 줄이되 기억 용량은 크게 만든다.
- LLM/CV 추론에서 MoE로 active parameter를 줄여 latency와 비용을 개선하되, KV cache와 메모리 관리가 중요해진다.

## 💡 아이디어 훅
- MoE 라우터를 로봇 안전 가드레일처럼 쓰면, 위험한 행동은 특정 전문가를 우회할 수 있을까?
- diffusion의 timestep마다 다른 전문가를 쓰면 생성 품질과 속도를 동시에 개선할 수 있을까?
- LLM 에이전트에서 tool use, code, reasoning을 전문가로 분리하면 hallucination이 줄까?

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
