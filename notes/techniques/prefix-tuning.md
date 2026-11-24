---
title: "Prefix Tuning"
date: 2026-11-25
tags: [technique, efficiency]
category: "효율화·적응"
status: draft
---

> 모델 몸통은 그대로 두고, 주의력(attention) 메모리에 붙이는 작은 '지시문 스티커'만 학습해서 새 일에 적응시키는 방법

**대표 논문**: Prefix-Tuning: Optimizing Continuous Prompts for Generation (2021) · **분류**: 효율화·적응

## 해결한 문제
기존 full fine-tuning(모델 가중치 전체를 다시 학습)은 태스크마다 큰 파라미터를 저장하고 GPU 메모리와 학습 시간이 많이 든다. 여러 작업을 순서대로 학습하면 이전 능력이 망가지는 catastrophic forgetting(기억 소실)도 걱정이다. 그래서 '모델은 그대로 두고 작은 부품만 바꿔' 빠르게 여러 작업에 적응하는 방법이 필요했다.

## 핵심 아이디어
비유하자면 로봇의 눈과 손(모델 가중치)은 그대로 두고, 작업 지시 라벨(prefix)만 바꿔 끼우는 것이다. 실제로는 transformer의 각 layer attention에서 key/value(질문과 답변을 연결하는 메모리) 앞에 학습 가능한 작은 벡터들을 붙인다. forward pass 때 이 prefix가 attention 패턴을 살짝 바꿔 모델이 새 작업에 맞게 행동하게 하고, backward pass에서는 prefix 벡터만 업데이트한다. 추론 때는 원본 모델 + task prefix만 저장하면 된다.

## 왜 작동하나
attention은 '무엇을 볼지'를 정하는 관문이라, key/value를 살짝 조작하면 전체 가중치를 바꾸지 않아도 정보 흐름을 바꿀 수 있다. 학습 파라미터가 매우 적어 메모리, 저장, 작업 전환 비용이 줄어든다. 원본 모델이 고정되어 있어 기존 지식이 덜 망가진다.

## 트레이드오프
- 복잡한 도메인 적응이나 정밀 제어에서는 full fine-tuning보다 성능이 떨어질 수 있다.
- prefix 길이, 초기화, 레이어별 설정 같은 하이퍼파라미터에 따라 결과가 민감할 수 있다.
- 태스크마다 prefix를 따로 관리해야 하고, 사람이 읽는 프롬프트처럼 해석하기 어렵다.

## 계보
**이전**
- Full fine-tuning
- Hard prompt engineering
- Adapter tuning

**이후**
- [[techniques/lora|LoRA]]
- [[techniques/qlora|QLoRA]]
- Prompt tuning
- IA^3
- Multi-task prefix tuning

## 피지컬 AI에서의 쓰임
- VLA(Vision-Language-Action) 모델에서 '접시 닦기', '물건 집기' 같은 작업별 prefix를 붙여 큰 로봇 정책 모델을 태스크마다 빠르게 전환한다.
- 로봇 world model이나 planner의 LLM을 frozen 상태로 두고, 특정 환경이나 로봇 팔 종류에 맞는 prefix만 학습해 시뮬레이션에서 실물 적응을 가볍게 한다.
- CV/VLA의 vision encoder나 attention 모듈에 task prefix를 넣어 '장애물 회피', '사람 손 추적' 같은 조건부 행동을 유도한다.

## 💡 아이디어 훅
- 로봇의 여러 관절 제어기에도 layer별 prefix를 붙이면 '보행에서 파지로' 전환을 더 빠르게 할 수 있을까?
- prefix를 사람이 읽는 자연어 프롬프트와 함께 학습하면, 모델이 '왜 이 행동을 하는지' 설명하는 데 쓸 수 있을까?
- 여러 로봇 태스크의 prefix를 평균하거나 병합하면 새로운 작업에 zero-shot으로 쓸 수 있을까?

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
