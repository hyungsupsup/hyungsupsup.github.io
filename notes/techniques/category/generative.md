---
title: "🌫️ 생성모델"
date: 2026-11-26
tags: [technique-category]
---

<p class="tc-lead">Diffusion, Flow Matching, 자기회귀. 로봇 정책과 월드모델의 생성 엔진.</p>
<div class="mh-section"><span>Diffusion</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/ddpm"><h4>DDPM</h4><p>사진을 아주 작은 소음으로 천천히 망가뜨리는 과정을 배우고, 그 역순으로 노이즈 덩어리에서 그림을 복원하는 생성모델</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/ddim"><h4>DDIM</h4><p>DDIM은 학습된 diffusion 모델을 '한 번에 더 크게 걷는' 방식으로 샘플링해, 이미지·행동 생성을 훨씬 적은 단계로 끝내는 빠른 샘플링 기법이다.</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/score-matching"><h4>Score Matching</h4><p>데이터가 밀집한 방향으로 가리키는 화살표(스코어)를 학습해, 무작위 잡음에서 시작해 그 화살표를 따라가며 샘플을 만드는 생성 모델</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/latent-diffusion"><h4>Latent Diffusion</h4><p>거대한 벽화를 바로 칠하지 않고, 먼저 작은 밑그림(잠재 스케치)을 잡은 뒤 그 위에서 그림을 완성하고 마지막에 크게 확대하는 생성모델 — '압축된 공간에서 노이즈를 걷어내는 diffusion'</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/classifier-free-guidance"><h4>Classifier-Free Guidance</h4><p>조건(프롬프트·목표)을 따르는 쪽으로 결과를 한 번 더 '밀어주는' 생성모델 샘플링 요령 — 힌트 있는 답과 힌트 없는 답의 차이를 과장해서 더한다.</p><span class="tc-badge">초안</span></a></div>
<div class="mh-section"><span>Flow·Few-step</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/flow-matching"><h4>Flow Matching</h4><p>Flow Matching은 소음에서 데이터로 가는 '바람길(속도장)'을 학습해, 이미지를 마치 물줄기를 따라 흐르듯 만들어내는 생성모델이다.</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/rectified-flow"><h4>Rectified Flow</h4><p>Rectified Flow는 노이즈에서 이미지를 만드는 구불구불한 경로를 여러 번 고쳐 거의 직선으로 만들어, 몇 걸음 만에 결과물을 뽑을 수 있게 해주는 생성 모델이다.</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/consistency-model"><h4>Consistency Model</h4><p>노이즈에서 깨끗한 결과로 가는 여러 중간 지점을 '어디서 출발해도 같은 목적지로 바로 점프'하게 학습시킨 빠른 생성모델.</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/distribution-matching-distillation"><h4>Distribution Matching Distillation</h4><p>사전학습된 diffusion/flow 교사의 score 차이를 이용해, 학생 생성기를 단일 스텝(또는 소수 스텝)으로 데이터 분포 자체에 매칭시키는 증류 기법.</p><span class="tc-badge">초안</span></a></div>
<div class="mh-section"><span>Discrete·Autoregressive</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/vq-vae"><h4>VQ-VAE</h4><p>사진을 무한한 색 대신 정해진 팔레트 색으로만 그리는 생성모델: 연속값을 코드북(정해진 벡터 목록)의 이산 코드로 바꿔 압축·생성한다.</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/autoregressive-transformer"><h4>Autoregressive Transformer</h4><p>문장을 한 단어씩 '다음 단어 맞히기'로 이어 붙여 글을 만들어내는 신경망 — 도미노를 앞에서부터 차례로 넘어뜨리듯, 방금 만든 단어를 다시 입력으로 넣어 다음 단어를 예측한다.</p><span class="tc-badge">초안</span></a></div>

[[techniques/index|← 기법 사전 전체]]
