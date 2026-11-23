---
title: "🎓 학습 기법"
date: 2026-11-24
tags: [technique-category]
---

<p class="tc-lead">모방학습, 강화학습, 선호 학습. 정책을 어떻게 가르치는가.</p>
<div class="mh-section"><span>모방학습</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/behavior-cloning"><h4>Behavior Cloning</h4><p>전문가가 운전하는 모습을 옆에서 지켜보고 '이 상황에선 이렇게 움직이더라'를 통째로 외워서 따라 하는 학습법 — 즉 로봇판 '보고 배우기(모방 학습)'의 가장 기본형.</p><span class="tc-badge">초안</span></a><div class="tc-card tc-todo"><h4>DAgger</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div></div>
<div class="mh-section"><span>강화학습</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/ppo"><h4>PPO</h4><p>정책(policy, 상황을 보고 행동을 고르는 규칙)을 업데이트하되 '한 번에 너무 멀리 가지 않도록 목줄을 채우는' 강화학습 기법 — 새 정책이 옛 정책에서 크게 벗어나면 이득을 잘라버린다.</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/offline-rl"><h4>Offline RL</h4><p>로봇이 직접 부딪히며 배우지 않고, 과거에 쌓인 로그 데이터만으로 '어떤 행동이 좋은지'를 배우는 학습법</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/group-relative-policy-optimization"><h4>Group Relative Policy Optimization</h4><p>같은 문제에 대한 여러 답을 한꺼번에 뽑아 서로 비교해 '이 답이 평균보다 얼마나 좋은가'로만 학습하는 PPO의 가벼운 변형.</p><span class="tc-badge">초안</span></a></div>
<div class="mh-section"><span>선호 정렬</span></div>
<div class="tc-grid"><div class="tc-card tc-todo"><h4>RLHF</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div><a class="tc-card internal" href="/techniques/dpo"><h4>DPO</h4><p>DPO는 사람 선호 쌍을 보고 보상 모델 없이 바로 '더 좋은 답' 쪽으로 확률을 조정하는 학습법이다.</p><span class="tc-badge">초안</span></a></div>
<div class="mh-section"><span>학습 전략</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/curriculum-learning"><h4>Curriculum Learning</h4><p>처음부터 어려운 문제를 풀게 하지 않고, 쉬운 예제부터 차근차근 난이도를 올려가며 학습하는 '단계별 숙제' 방식</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/chain-of-thought"><h4>Chain-of-Thought</h4><p>LLM이 최종 답을 바로 내지 않고 중간 추론 단계(reasoning steps)를 명시적으로 생성하도록 유도해 복잡한 다단계 추론 성능을 끌어올리는 프롬프팅/학습 기법.</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/teacher-forcing"><h4>Teacher Forcing</h4><p>Autoregressive 모델 학습 시 이전 시점의 모델 예측 대신 ground-truth 이전 토큰(또는 상태)을 입력으로 넣어주는 학습 기법.</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/k-fac"><h4>K-FAC</h4><p>K-FAC(크로네커 분해 근사 곡률)은 모든 파라미터 쌍의 관계까지 계산하는 대신, 각 층의 입력과 출력 신호 두 개의 작은 행렬로 손실 곡면을 근사해 더 똑똑한 경사 하강을 하는 학습법이다.</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/genetic-algorithm"><h4>Genetic Algorithm</h4><p>여러 후보 해답을 '번식·선택·변이' 시키면서 점점 더 좋은 답을 찾아가는 진화형 탐색 방법</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/supervised-fine-tuning"><h4>Supervised Fine-Tuning</h4><p>이미 세상의 언어/이미지를 많이 배운 모델에게 '질문-정답' 숙제를 다시 시켜서 특정 일을 잘하게 만드는 맞춤 훈련</p><span class="tc-badge">초안</span></a></div>
<div class="mh-section"><span>불확실성 추정</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/conformal-prediction"><h4>Conformal Prediction</h4><p>모델 출력에 대해 분포 가정 없이 유한 표본(finite-sample) 보장된 예측 집합/구간을 만들어주는 사후 보정(post-hoc calibration) 프레임워크.</p><span class="tc-badge">초안</span></a></div>

[[techniques/index|← 기법 사전 전체]]
