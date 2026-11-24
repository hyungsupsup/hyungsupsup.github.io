---
title: "Adapter"
date: 2026-11-25
tags: [technique, efficiency]
category: "효율화·적응"
status: draft
---

> 큰 모델 안에 끼워 넣는 작은 '변환 플러그'로, 전체를 다시 학습하지 않고 특정 작업에 빠르게 적응시키는 방법

**대표 논문**: Parameter-Efficient Transfer Learning for NLP (2019) · **분류**: 효율화·적응

## 해결한 문제
거대한 모델을 새 작업에 맞게 전체 학습하면 시간, 메모리, 저장 공간이 너무 많이 든다. 작업마다 모델 사본을 만들면 관리도 어렵고, 일부 층만 얼려두는 방식은 적응력이 떨어질 수 있다.

## 핵심 아이디어
Adapter는 큰 모델 사이에 작은 병목 구조의 신경망을 끼워 넣는 방식이다. 마치 번역기가 붙은 플러그처럼, 원래 모델의 큰 가중치는 그대로 두고 작은 Adapter만 학습한다. 보통 입력을 먼저 작은 차원으로 압축했다가 다시 복원하는 구조를 쓰며, 원래 출력과 더해져서 기존 지식을 크게 망치지 않는다.

## 왜 작동하나
학습해야 할 파라미터가 훨씬 적어서 계산량과 저장 부담이 크게 줄어든다. 큰 모델은 이미 배운 일반 지식을 유지하고, Adapter만 새 작업에 맞는 작은 변환을 담당하므로 과적응이나 지식 손실을 줄이기 쉽다.

## 트레이드오프
- 작업이 매우 복잡하면 전체 학습보다 성능이 낮을 수 있다.
- Adapter를 여러 개 쓰면 모델 구조가 복잡해지고 추론 속도가 약간 느려질 수 있다.
- 작업마다 Adapter를 관리해야 해서 배포와 버전 관리가 번거로울 수 있다.

## 계보
**이전**
- Full fine-tuning
- Frozen backbone + task head
- Feature extraction

**이후**
- [[techniques/lora|LoRA]]
- [[techniques/prefix-tuning|Prefix tuning]]
- Prompt tuning
- AdapterFusion
- Mixture-of-Adapters
- IA3

## 피지컬 AI에서의 쓰임
- VLA 모델에서 로봇 팔 종류가 바뀌면 전체를 다시 학습하지 않고 Adapter만 새로 학습해 빠르게 적응시킨다.
- Diffusion policy가 새 카메라나 작업 환경에 맞게 작은 Adapter로 동작 분포를 보정한다.
- World model에서 특정 로봇의 물리 특성을 반영할 때 큰 모델은 고정하고 Adapter만 학습해 시뮬레이션과 실물 간 차이를 줄인다.

## 💡 아이디어 훅
- Adapter와 LoRA를 함께 쓰면 어떤 장단점이 생길까?
- 로봇 작업마다 Adapter를 고르는 라우터를 만들면 멀티 태스크 로봇에 도움이 될까?
- Adapter를 안전 필터처럼 써서 위험한 동작만 차단할 수 있을까?

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
