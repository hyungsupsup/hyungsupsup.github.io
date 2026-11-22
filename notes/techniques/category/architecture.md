---
title: "🧱 아키텍처 모듈"
date: 2026-11-23
tags: [technique-category]
---

<p class="tc-lead">모델을 조립하는 기본 블록과 조건 주입 방법.</p>
<div class="mh-section"><span>백본</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/transformer"><h4>Transformer</h4><p>문장 속 모든 단어가 서로를 한 번에 훑어보며 '누가 누구랑 얼마나 관련 있나'를 점수로 매기는 방식으로, 순서대로 읽지 않고 통째로 병렬 처리하는 신경망 블록 (모든 학생이 서로 쪽지를 동시에 주고받는 교실 같은 것)</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/vit"><h4>ViT</h4><p>이미지를 16x16 퍼즐 조각으로 잘라 '단어'처럼 한 줄로 늘어놓고, 문장 읽듯이 Transformer에 넣어 이해하는 이미지 인식 아키텍처</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/dit"><h4>DiT</h4><p>이미지 생성 diffusion 모델의 뼈대인 U-Net을 ViT처럼 transformer로 갈아 끼운 것 — 이미지를 작은 퍼즐 조각(패치)으로 잘라 '단어'처럼 서로 대화시키는 방식</p><span class="tc-badge">초안</span></a><div class="tc-card tc-todo"><h4>U-Net</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div><div class="tc-card tc-todo"><h4>ResNet</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div></div>
<div class="mh-section"><span>조건 주입·연결</span></div>
<div class="tc-grid"><div class="tc-card tc-todo"><h4>FiLM</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div><div class="tc-card tc-todo"><h4>Perceiver</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div><div class="tc-card tc-todo"><h4>Q-Former</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div></div>
<div class="mh-section"><span>정규화</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/layer-normalization"><h4>Layer Normalization</h4><p>한 샘플(또는 한 토큰) 안의 특징 값들을 평균 0, 표준편차 1로 고르게 맞춰 주는 '자동 볼륨 노멀라이저'</p><span class="tc-badge">초안</span></a></div>
<div class="mh-section"><span>Convolution</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/causal-convolution"><h4>Causal Convolution</h4><p>미래를 몰래 보지 않고 과거와 현재만 참고하는 1D 컨볼루션(입력 시퀀스에 작은 필터를 밀어 붙여 가중합을 계산하는 연산)입니다.</p><span class="tc-badge">초안</span></a></div>

[[techniques/index|← 기법 사전 전체]]
