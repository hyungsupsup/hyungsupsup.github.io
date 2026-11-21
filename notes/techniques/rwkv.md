---
title: "RWKV"
date: 2026-11-22
tags: [technique, sequence]
category: "시퀀스 대안"
status: draft
---

> Transformer처럼 병렬로 학습하고 RNN처럼 순서대로 기억을 갱신하는 경량 시퀀스 모델

**대표 논문**: RWKV: Reinventing RNNs for the Transformer Era (2023) · **분류**: 시퀀스 대안

## 해결한 문제
Transformer는 attention(모든 단어를 서로 비교하는 방식) 때문에 문장이 길어지면 계산량과 메모리가 빠르게 늘어난다. RNN은 메모리는 작지만 단어를 하나씩 처리해야 해서 학습을 병렬로 하기 어렵다.

## 핵심 아이디어
RWKV는 '읽은 문장을 매번 처음부터 다시 훑는 대신 핵심 메모를 계속 갱신하는 독서 노트'처럼 동작한다. 각 단어를 입력하면 이전 상태와 현재 단어를 섞어 새 상태를 만들고, 시간 혼합과 채널 혼합으로 정보를 이동시킨다. 학습 때는 이 순환 구조를 병렬로 계산할 수 있게 수식을 설계했고, 추론 때는 이전 상태만 유지하면 된다.

## 왜 작동하나
모든 단어 쌍을 비교하는 attention 대신 고정된 크기의 상태만 갱신하므로 긴 시퀀스에서도 메모리와 계산이 선형적으로 늘어난다. 덕분에 Transformer의 병렬 학습 장점과 RNN의 저비용 추론 장점을 동시에 노릴 수 있다.

## 트레이드오프
- 정확한 long-range retrieval(먼저 나온 특정 단어를 그대로 찾아오는 능력)은 attention보다 약할 수 있다.
- 생태계와 추론 최적화 도구가 Transformer만큼 성숙하지 않을 수 있다.
- 긴 문맥에서 정보를 압축해 저장하므로 세부 정보가 손실될 수 있다.

## 계보
**이전**
- RNN/LSTM
- [[techniques/transformer|Transformer]]
- [[techniques/linear-attention|Linear attention]]

**이후**
- RWKV-4
- RWKV-5
- RWKV-6

## 피지컬 AI에서의 쓰임
- 로봇 온보드에서 음성/명령을 낮은 메모리로 처리하는 경량 언어모델
- VLA(비전-언어-행동 모델)의 언어 인코더나 경량 policy backbone
- 월드모델/시뮬레이션에서 긴 시퀀스를 저비용으로 압축해 기억하는 모듈

## 💡 아이디어 훅
- RWKV의 상태 갱신을 diffusion의 latent 압축과 결합하면 긴 영상 생성이 가벼워질까?
- 로봇의 다중모달 시퀀스에서 attention 대신 RWKV로 메모리를 관리하면 온보드 추론이 빨라질까?
- KV cache(이전에 읽은 단어들의 핵심 정보를 다시 계산하지 않도록 저장해 두는 메모리)를 RWKV 상태로 대체하면 장기 대화의 메모리 부담이 줄까?

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
