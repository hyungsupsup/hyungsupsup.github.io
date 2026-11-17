---
title: "Chain-of-Thought"
date: 2026-11-17
tags: [technique, training]
category: "학습 기법"
status: draft
---

> LLM이 최종 답을 바로 내지 않고 중간 추론 단계(reasoning steps)를 명시적으로 생성하도록 유도해 복잡한 다단계 추론 성능을 끌어올리는 프롬프팅/학습 기법.

**대표 논문**: Chain-of-Thought Prompting Elicits Reasoning in Large Language Models (2022) · **분류**: 학습 기법

## 해결한 문제
기존 few-shot prompting은 입력→출력 매핑만 보여주므로 산술·상식·기호적 다단계 추론에서 모델이 중간 계산을 생략하고 그럴듯한 오답으로 점프했다. 또한 scratchpad류 접근은 태스크별로 특화된 학습 데이터가 필요해 범용성이 낮았다. CoT는 별도 파인튜닝 없이 소수의 추론 예시만으로 다단계 문제를 분해하게 만든다.

## 핵심 아이디어
프롬프트의 few-shot 예시를 $(x_i, r_i, y_i)$ 형태로 구성한다. 여기서 $r_i$는 자연어 추론 사슬(중간 계산, 근거, 하위 질문 분해)이다. 모델은 테스트 입력 $x$에 대해 $p(y \mid x) = \sum_{r} p(r \mid x)\, p(y \mid x, r)$ 를 근사하듯 먼저 $r$을 생성하고 그 조건부로 $y$를 생성한다. 추론 사슬은 토큰 시퀀스이므로 각 단계가 자기회귀 컨텍스트로 누적되어 후속 단계의 조건이 되고, 이는 고정 깊이 Transformer가 외부 메모리(컨텍스트)를 이용해 계산 깊이를 늘리는 효과를 낸다. 학습 기법으로 확장하면 교사 모델이 생성한 CoT를 소형 모델에 distillation하거나, CoT 포함 데이터로 SFT/RL을 수행한다.

## 왜 작동하나
추론 단계를 토큰으로 '말하게' 하면 중간 결과가 컨텍스트에 명시적으로 저장되어, 모델이 한 번의 forward pass로 감당해야 했던 계산 부담을 여러 스텝으로 분산시킬 수 있다. 또 사전학습 코퍼스에 이미 존재하는 풀이 과정의 분포를 활용하므로, 소수 예시만으로도 해당 태스크의 절차적 지식을 끌어낸다.

## 트레이드오프
- 추론 토큰만큼 inference 비용·지연이 선형 이상으로 증가한다
- 충분히 큰 모델에서만 창발적으로 효과가 나타나 소형 모델에서는 이득이 미미하거나 역효과(그럴듯한 오류 사슬)가 날 수 있다
- 생성된 추론 사슬이 실제 계산 과정과 불일치(unfaithful)할 수 있어 해석·검증이 어렵다
- 프롬프트 예시의 형식·문체에 민감하고 태스크별 예시 설계 비용이 든다
- 단일 사슬은 초기 실수에 오류가 전파되며, self-consistency 같은 다중 샘플링은 비용을 배가한다

## 계보
**이전**
- Few-shot in-context learning (Brown et al., GPT-3)
- Scratchpad / show-your-work prompting (Nye et al., 2021)
- Natural language rationale / explain-then-predict fine-tuning
- Prompt-based arithmetic decomposition (e.g., least-to-most의 전신)

**이후**
- Zero-shot CoT ("Let's think step by step")
- Self-Consistency (majority voting over CoT samples)
- Tree-of-Thoughts / Graph-of-Thoughts
- Least-to-Most Prompting
- Program-of-Thoughts / PAL (코드 실행 기반 추론)
- ReAct (reasoning + acting interleaving)
- CoT distillation (Ho et al.) 및 reasoning distillation
- RL로 긴 CoT를 학습하는 reasoning model 계열 (OpenAI o1, DeepSeek-R1 등)

## 피지컬 AI에서의 쓰임
- RT-2의 chain-of-thought 변형: 로봇 명령을 'Plan → Answer'로 분해해 다단계 조작 지시를 처리
- SayCan / Inner Monologue: LLM이 자연어 CoT로 하위 태스크를 계획하고 affordance/value function으로 필터링
- Embodied Chain-of-Thought (ECoT): VLA 정책이 계획·하위태스크·시각적 grounding·gripper 위치를 텍스트로 먼저 추론한 뒤 action을 출력
- PaLM-E / Code as Policies: 장면 관찰에 대한 추론 사슬을 거쳐 로봇 코드 또는 waypoint 생성
- 월드모델·VLA에서 action token 예측 전에 latent/텍스트 reasoning step을 두는 하이브리드 정책

## 💡 아이디어 훅
- VLA에서 텍스트 CoT 대신 연속 latent reasoning token(예: 소수의 learned reasoning slot)으로 추론하고 action head와 공동 학습하면 지연·비용을 줄이면서 이득을 유지할 수 있는가?
- CoT 사슬을 월드모델 rollout과 결합해 '상상한 미래 상태'를 추론 단계로 삼고 그 위에서 action을 선택하는 model-based CoT는 단순 언어 CoT보다 조작 태스크에서 우수한가?
- 로봇 실행 성공/실패 신호를 verifier로 학습해 CoT 사슬을 사후 필터링하거나 process reward로 RL하면 unfaithful reasoning과 오류 전파를 얼마나 줄일 수 있는가?
- 대형 VLA의 CoT를 소형 실시간 정책으로 distillation할 때, 추론 토큰을 컴파일해 추론 없는(student) 정책으로 증류하는 'CoT-free 컴파일'이 가능한가?
- 실패 복구(recovery) 상황에서 CoT가 실제 로봇 상태와 어긋나는 hallucinated reasoning을 탐지하는 grounding 검증기를 어떻게 설계할 것인가?
- 다중 로봇/다중 에이전트에서 CoT 사슬을 공유 컨텍스트로 교환하는 협업 추론 프로토콜이 단일 에이전트 CoT 대비 통신 비용 대비 이득이 있는가?

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
