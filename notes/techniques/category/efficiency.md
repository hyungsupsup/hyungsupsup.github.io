---
title: "⚡ 효율화·적응"
date: 2026-11-20
tags: [technique-category]
---

<p class="tc-lead">큰 모델을 적은 자원으로 학습·적응·배포하는 기법.</p>
<div class="mh-section"><span>Parameter-Efficient Fine-Tuning</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/lora"><h4>LoRA</h4><p>거대 모델의 몸통은 얼려두고, 옆에 얇은 '덧대기 판' 두 장만 붙여 학습하는 초경량 미세조정 기법 — 두꺼운 사전에 포스트잇만 붙이는 셈.</p><span class="tc-badge">초안</span></a><div class="tc-card tc-todo"><h4>QLoRA</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div><div class="tc-card tc-todo"><h4>Adapter</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div><div class="tc-card tc-todo"><h4>Prefix Tuning</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div></div>
<div class="mh-section"><span>압축·경량화</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/knowledge-distillation"><h4>Knowledge Distillation</h4><p>큰 '선생님' 모델이 정답을 맞히는 요령(확신의 정도까지)을 작은 '학생' 모델에게 과외로 옮겨 담는 효율화 기술</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/quantization"><h4>Quantization</h4><p>고해상도 사진을 JPEG로 저장하듯, 숫자를 굵직한 눈금으로 반올림해 모델을 4분의 1~8분의 1 크기로 눌러 담는 경량화 기법</p><span class="tc-badge">초안</span></a></div>
<div class="mh-section"><span>조건부 계산</span></div>
<div class="tc-grid"><div class="tc-card tc-todo"><h4>Mixture of Experts</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div></div>
<div class="mh-section"><span>추론 가속</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/speculative-decoding"><h4>Speculative Decoding</h4><p>작은 모델이 빠르게 '초안'을 여러 개 던지고, 큰 모델이 그걸 한 번에 채점해서 맞는 것만 채택하는 방식으로 LLM 추론을 2~3배 빠르게 만드는 기법 — 빠른 조수가 받아쓰고 선생님이 검토하는 회의록과 비슷하다.</p><span class="tc-badge">초안</span></a></div>

[[techniques/index|← 기법 사전 전체]]
