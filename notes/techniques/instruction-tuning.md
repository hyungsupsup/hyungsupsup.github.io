---
title: "Instruction Tuning"
date: 2026-11-26
tags: [technique, training]
category: "학습 기법"
status: draft
---

> LLM에게 '이런 명령을 받으면 이렇게 답해'라는 예시를 잔뜩 보여줘서, 지시를 알아듣고 수행하도록 훈련하는 방법

**대표 논문**: Finetuned Language Models Are Zero-Shot Learners (2021) · **분류**: 학습 기법

## 해결한 문제
Instruction Tuning 이전에는 LLM이 다음 단어를 잘 예측해도, 사용자가 '요약해줘', '번역해줘', '코드 짜줘'라고 시키면 맥락만 이어가거나 엉뚱한 답을 할 수 있었다. 그래서 좋은 결과를 얻으려면 프롬프트를 여러 번 고치거나 예시를 잔뜩 넣어야 해서 불편했다.

## 핵심 아이디어
비유하자면, 똑똑한 앵무새에게 '질문→답변' 카드 수만 장을 보여주며 '이런 말에는 이렇게 답하는 거야'라고 가르치는 것과 같다. 실제로는 사전학습된 LLM에 instruction(명령문)과 response(원하는 답변) 쌍을 학습 데이터로 주고, 모델이 명령을 보고 적절한 답변을 생성하도록 fine-tuning(미세조정)한다. 학습 후 모델은 처음 보는 명령에도 '무엇을 해야 하는지'를 더 잘 이해하고 답변 형식도 사용자에게 맞게 바꾼다.

## 왜 작동하나
모델이 단순히 '다음 단어'만 예측하는 습관에서 벗어나, '사용자의 의도에 맞는 답변'을 생성하도록 방향을 잡아주기 때문이다. 덕분에 few-shot 예시를 많이 넣지 않아도 되고, 같은 모델이 요약·번역·코딩·질문답변 같은 여러 작업을 더 자연스럽게 수행할 수 있다.

## 트레이드오프
- Instruction Tuning의 성능은 학습 데이터에 '어떤 명령과 답변'이 얼마나 잘 들어 있느냐에 크게 좌우된다.
- 너무 좁은 스타일의 데이터로만 훈련하면 모델이 특정 답변 형식만 고집하거나, 처음 보는 상황에서 과하게 자신 있게 틀린 답을 할 수 있다.
- Instruction Tuning만으로는 안전성·사실성·도구 사용 정확도가 완전히 해결되지 않아, 이후 RLHF나 평가·가드레일이 추가로 필요할 수 있다.

## 계보
**이전**
- [[techniques/supervised-fine-tuning|Supervised Fine-Tuning (SFT)]]
- Prompt Engineering
- Few-shot Prompting
- Task-specific Fine-Tuning

**이후**
- [[techniques/rlhf|RLHF]]
- [[techniques/dpo|DPO]]
- Self-Instruct
- Chain-of-Thought Fine-Tuning
- Preference Tuning

## 피지컬 AI에서의 쓰임
- VLA 모델에서 '빨간 컵을 들어 올려' 같은 자연어 명령을 받아 로봇 동작 토큰으로 바꾸는 지시 수행 능력을 키울 때 쓸 수 있다.
- LLM 에이전트가 '이 파일을 읽고 요약해서 이메일 초안을 작성해' 같은 다단계 작업을 이해하고, 도구 호출 순서를 더 잘 따르도록 훈련할 때 쓸 수 있다.
- CV나 멀티모달 모델에서 '이미지에서 배경만 제거해줘', '이 표를 그래프로 바꿔줘' 같은 텍스트 지시를 더 정확히 수행하도록 학습할 때 쓸 수 있다.

## 💡 아이디어 훅
- Instruction Tuning을 로봇에 쓸 때, 성공 예시뿐 아니라 '실패 후 고친 명령→동작'도 학습 데이터로 넣으면 더 강해질까?
- LLM의 KV cache를 활용해, 긴 로봇 작업 지시를 여러 단계로 나누어 Instruction Tuning하면 제어 속도와 정확도를 동시에 개선할 수 있을까?
- Instruction Tuning 데이터를 자동으로 만들 때, Self-Instruct처럼 모델이 스스로 명령을 생성하고 검증하게 하면 사람 라벨링을 얼마나 줄일 수 있을까?

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
