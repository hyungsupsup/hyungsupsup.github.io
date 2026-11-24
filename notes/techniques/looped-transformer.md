---
title: "Looped Transformer"
date: 2026-11-25
tags: [technique, architecture]
category: "아키텍처 모듈"
status: draft
---

> 서로 다른 층을 깊게 쌓는 대신, 가중치를 공유하는 블록 하나를 여러 번 반복 통과시켜 파라미터는 그대로 두고 '생각하는 깊이'만 늘리는 transformer (같은 문제집을 여러 번 다시 풀며 답을 다듬는 것)

**대표 논문**: Universal Transformers (Dehghani et al., 2018) · Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach (Geiping et al., 2025) · **분류**: 아키텍처 모듈

## 해결한 문제
일반 transformer는 층 수가 고정되어 있어서, 쉬운 입력이든 어려운 입력이든 같은 깊이의 계산만 한다. 더 깊게 생각하게 하려면 층을 더 쌓아야 하는데, 그러면 파라미터와 메모리가 같이 늘어난다. Chain-of-Thought처럼 토큰을 더 생성해서 계산을 늘리는 방법도 있지만, 생각을 매번 언어 토큰으로 꺼내야 해서 느리고 표현이 제한된다.

## 핵심 아이디어
보통 세 부분으로 나눈다.
1. **Prelude**: 입력 토큰을 latent 공간으로 임베딩한다 (`e`).
2. **Recurrent core**: 가중치를 공유하는 블록(또는 블록 묶음)이 상태를 R번 갱신한다. `s_t = Core(s_{t-1}, e)`. 매 스텝 입력 임베딩 `e`를 다시 주입해서, 반복이 길어져도 원래 입력을 잊지 않게 한다.
3. **Coda**: 마지막 상태 `s_R`을 출력으로 디코딩한다.

학습할 때 반복 횟수 R을 랜덤하게 샘플링하면(Geiping et al.), 추론할 때 R을 학습 때보다 늘려 '더 오래 생각'하게 할 수 있다. 토큰별로 반복 횟수를 다르게 주는 adaptive depth(early exit, Universal Transformer의 ACT)도 가능하다.

## 왜 작동하나
- 같은 함수를 반복 적용하는 구조는 반복 알고리즘(탐색, 산술, 반복 정제)을 표현하기에 자연스럽다. 그래서 학습 때보다 더 어려운 문제로 일반화하는 데 유리하다는 연구 결과들이 있다.
- 추론이 토큰이 아니라 연속적인 latent 상태 안에서 일어나므로, CoT보다 표현 대역폭이 넓고 출력 토큰을 쓰지 않는다 ("hidden/latent reasoning").
- 파라미터 수와 계산량(깊이)을 분리하므로, 메모리가 제약일 때 작은 모델로 깊은 계산을 할 수 있다.

## 트레이드오프
- 파라미터는 아끼지만 FLOPs와 지연 시간은 반복 횟수만큼 그대로 늘어난다.
- 반복이 깊어지면 상태가 발산하거나 붕괴해서 학습이 불안정해질 수 있다. 정규화, 입력 재주입, truncated backprop 같은 처리가 필요하다.
- 추론 과정이 latent에 숨어 있어서 CoT보다 해석하고 모니터링하기 어렵다. 안전성 논의에서 쟁점이 된다.
- 같은 파라미터 수의 일반 모델보다 낫더라도, 같은 FLOPs의 일반 모델과 비교하면 이점이 줄어들 수 있다 (비교 기준에 주의).

## 계보
**이전**
- [[techniques/transformer|Transformer]]
- Universal Transformer (가중치 공유 + Adaptive Computation Time)
- ALBERT (층 간 파라미터 공유)

**이후**
- Recurrent-depth LM (Huginn, Geiping et al., 2025)
- Looped MoE, latent multi-token prediction을 결합한 변형 (예: LoopMTP, arXiv 2608.03624)
- Looped GPT-BERT 등 소형 LM에서 파라미터 대신 계산을 늘리는 연구 (arXiv 2609.09691)
- GPT-6 Astra: *The Information*이 recurrent depth를 쓴다고 보도함. OpenAI는 아키텍처를 공개하지 않음 (확인 필요)

## 피지컬 AI에서의 쓰임
- VLA는 제어 주기 때문에 추론 예산이 빠듯하다. 상황 난이도에 따라 반복 횟수를 조절하는 adaptive compute가 잘 맞을 수 있다 (가능성, 확인 필요).
- 온보드 GPU처럼 메모리가 작은 환경에서, 파라미터는 작게 유지하면서 계산 깊이를 늘리는 백본으로 쓸 수 있다.
- 상태를 반복해서 정제한다는 점에서 [[techniques/diffusion-policy|Diffusion Policy]]나 [[techniques/flow-matching|Flow Matching]] action head의 반복 denoising과 개념적으로 닮았다 (개인 해석).

## 💡 아이디어 훅
- Looped core의 반복 횟수를 로봇 정책의 불확실성(예: [[techniques/conformal-prediction|Conformal Prediction]] 구간 폭)에 맞춰 조절하면, 쉬운 구간은 빠르게, 어려운 접촉 구간은 깊게 생각하게 할 수 있을까?
- Diffusion의 denoising step과 looped transformer의 반복을 하나로 합치면(반복 하나 = denoising 한 스텝), 파라미터를 공유하는 action generator가 될까?
- 월드모델에서 '한 번 반복 = 한 타임스텝 앞을 상상'으로 해석할 수 있을까?

## 참고
- [GPT-6 Astra, Looped Transformers, and Hidden Reasoning — Sebastian Raschka](https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and)
- [LoopMTP (arXiv 2608.03624)](https://arxiv.org/pdf/2608.03624)
- [Looped GPT-BERT (arXiv 2609.09691)](https://arxiv.org/pdf/2609.09691)

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
