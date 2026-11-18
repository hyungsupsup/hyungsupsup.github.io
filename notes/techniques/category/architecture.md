---
title: "🧱 아키텍처 모듈"
date: 2026-11-19
tags: [technique-category]
---

<p class="tc-lead">모델을 조립하는 기본 블록과 조건 주입 방법.</p>
<div class="mh-section"><span>백본</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/transformer"><h4>Transformer</h4><p>문장 속 모든 단어가 서로를 한 번에 훑어보며 '누가 누구랑 얼마나 관련 있나'를 점수로 매기는 방식으로, 순서대로 읽지 않고 통째로 병렬 처리하는 신경망 블록 (모든 학생이 서로 쪽지를 동시에 주고받는 교실 같은 것)</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/vit"><h4>ViT</h4><p>이미지를 16x16 퍼즐 조각으로 잘라 '단어'처럼 한 줄로 늘어놓고, 문장 읽듯이 Transformer에 넣어 이해하는 이미지 인식 아키텍처</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/dit"><h4>DiT</h4><p>이미지 생성 diffusion 모델의 뼈대인 U-Net을 ViT처럼 transformer로 갈아 끼운 것 — 이미지를 작은 퍼즐 조각(패치)으로 잘라 '단어'처럼 서로 대화시키는 방식</p><span class="tc-badge">초안</span></a><div class="tc-card tc-todo"><h4>U-Net</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div><div class="tc-card tc-todo"><h4>ResNet</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div><a class="tc-card internal" href="/techniques/streaming-video-llm"><h4>Streaming Video LLM</h4><p>녹화본을 다 보고 나서 답하는 게 아니라, 라이브 중계를 보면서 실시간으로 말하는 비디오 LLM.</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/tabular-foundation-model"><h4>Tabular Foundation Model</h4><p>표(엑셀) 데이터를 위한 '학습 없는 예측기' — 수많은 가상의 표 문제를 미리 풀어본 사전학습 모델에게 예시 몇 줄만 보여주면, 따로 학습 없이 바로 답을 내주는 표 전문 파운데이션 모델</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/table-encoder"><h4>Table Encoder</h4><p>표를 '셀 하나하나에 행·열 주소를 붙인 스프레드시트 지도'처럼 읽어서, 표의 구조와 내용을 한꺼번에 이해하는 인코더 모듈</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/feature-encoding"><h4>Feature Encoding</h4><p>센서가 준 날것의 데이터(픽셀·좌표·토큰)를 신경망이 먹을 수 있는 '숫자 카드'로 잘라서 번역해 주는 입력 담당 모듈</p><span class="tc-badge">초안</span></a></div>
<div class="mh-section"><span>조건 주입·연결</span></div>
<div class="tc-grid"><div class="tc-card tc-todo"><h4>FiLM</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div><div class="tc-card tc-todo"><h4>Perceiver</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div><div class="tc-card tc-todo"><h4>Q-Former</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div><a class="tc-card internal" href="/techniques/tool-calling"><h4>Tool Calling</h4><p>말만 하던 LLM에게 계산기·검색·로봇 팔 같은 '손발'을 달아주는 장치 — 필요할 때 정해진 형식으로 도구를 불러 쓰게 한다.</p><span class="tc-badge">초안</span></a></div>
<div class="mh-section"><span>정규화</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/layer-normalization"><h4>Layer Normalization</h4><p>한 샘플(또는 한 토큰) 안의 특징 값들을 평균 0, 표준편차 1로 고르게 맞춰 주는 '자동 볼륨 노멀라이저'</p><span class="tc-badge">초안</span></a></div>
<div class="mh-section"><span>메모리</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/self-improvement-memory"><h4>Self-Improvement Memory</h4><p>일을 겪은 뒤 메모장을 스스로 고쳐 쓰는 에이전트용 기억 장치 — 경험을 저장만 하는 게 아니라 '교훈'으로 다듬어 다음 행동을 바꾸는 모듈</p><span class="tc-badge">초안</span></a></div>

[[techniques/index|← 기법 사전 전체]]
