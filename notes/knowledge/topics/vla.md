---
title: VLA (Vision-Language-Action)
date: 2026-11-12
tags: [topic, vla]
status: 작성 중
---

## 한 줄 정의
이미지와 언어 명령을 입력으로 받아 로봇 동작을 직접 출력하는 모델. 보통 사전학습된 VLM에 동작 출력부를 붙여 만든다.

## 계보 (채워 나갈 것)
- RT-1 → RT-2 (VLM에 동작을 토큰으로 학습) → OpenVLA (오픈소스 7B) → π0 (flow matching 동작 헤드) → π0.5 / GR00T N1 / SmolVLA

## 핵심 설계 축
| 축 | 선택지 | 대표 |
|---|---|---|
| 동작 표현 | 이산 토큰 / 연속값 (diffusion·flow) / action chunk | RT-2, OpenVLA / π0 / ACT |
| 백본 | 대형 VLM / 경량 VLM | OpenVLA (Llama 2 기반) / SmolVLA |
| 데이터 | 교차 로봇(cross-embodiment) / 단일 로봇 | Open X-Embodiment |

## 열린 문제 (내 생각)
- 시뮬레이션과 실제 영상 사이의 시각적 차이에 대한 강건성 → [[open-questions]]

## 관련 노트
- 실험: (아직 없음)
