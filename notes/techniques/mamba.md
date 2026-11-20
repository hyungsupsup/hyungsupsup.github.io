---
title: "Mamba"
date: 2026-11-21
tags: [technique, sequence]
category: "시퀀스 대안"
status: draft
---

> Transformer처럼 모든 단어를 서로 비교하지 않고, 컨베이어 벨트처럼 흐름을 따라가며 중요한 정보만 골라 기억하는 고속 시퀀스 모델

**대표 논문**: Mamba: Linear-Time Sequence Modeling with Selective State Spaces (2023) · **분류**: 시퀀스 대안

## 해결한 문제
Transformer는 attention(모든 토큰끼리 관계를 계산하는 방식) 때문에 시퀀스가 길어지면 계산량과 메모리가 급격히 늘어난다. 기존 RNN/LSTM은 순서대로 계산해야 해서 학습이 느리고, 긴 문맥을 오래 기억하기 어려웠다.

## 핵심 아이디어
비유하자면, 컨베이어 벨트 위 물품(토큰)을 지나가게 하면서 중요한 물건만 상자에 담고 나머지는 빠르게 흘려보내는 스마트 창고다. Mamba는 state space model(시간에 따라 내부 상태가 갱신되는 수학적 틀)을 쓰되, 입력마다 어떤 정보를 기억하고 무시할지 조절하는 selective scan(선택적 상태 갱신)을 적용한다. 각 토큰에서 이전 상태와 현재 입력을 합쳐 새 상태를 만들고, 하드웨어에 맞게 병렬로 계산하는 scan kernel을 사용해 속도를 확보한다.

## 왜 작동하나
모든 과거 토큰을 전부 비교하지 않고 선형으로 처리하기 때문에 긴 시퀀스에서 계산량과 메모리가 크게 줄어든다. 입력에 따라 기억 규칙을 바꿀 수 있어 단순 RNN보다 중요한 정보를 더 오래 유지하기 쉽다.

## 트레이드오프
- attention처럼 모든 과거를 즉시 조회하는 방식은 아니라, 특정 위치를 정확히 다시 꺼내는 능력은 모델이 학습으로 만들어야 한다.
- selective scan과 커스텀 커널 구현이 복잡하고, Transformer만큼 다양한 하드웨어·프레임워크 지원이 성숙하지 않을 수 있다.
- 짧은 문맥이나 일부 벤치마크에서는 Transformer가 여전히 더 강할 수 있다.

## 계보
**이전**
- [[techniques/transformer|Transformer]]
- RNN/LSTM
- S4 (Structured State Space Sequence Model)

**이후**
- Mamba-2
- Jamba
- Samba
- MambaVision

## 피지컬 AI에서의 쓰임
- 로봇의 카메라·LiDAR·관절 각도 같은 긴 센서 스트림을 실시간으로 요약해 다음 행동을 예측하는 VLA(비전-언어-행동) 모델의 백본
- 드론이나 자율주행에서 수십 초~수 분의 과거 궤적과 주변 객체 변화를 기억해 충돌 위험을 판단하는 시퀀스 예측
- 영상 생성이나 3D 스캔 시퀀스에서 프레임 간 일관성을 유지하면서 메모리를 줄이는 diffusion/transformer 대안

## 💡 아이디어 훅
- 로봇이 '중요한 순간만 기억'하는 Mamba식 selective state를 이벤트 기반 센서와 결합하면 배터리와 연산을 얼마나 줄일 수 있을까?
- Transformer의 attention과 Mamba의 state를 하이브리드로 쓰면 긴 영상에서 빠른 검색과 장기 기억을 동시에 잡을 수 있을까?
- Mamba의 선형 상태를 월드모델의 latent dynamics로 쓰면 시뮬레이션 속도와 예측 정확도 사이 균형이 어떻게 변할까?

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
