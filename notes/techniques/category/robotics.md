---
title: "🦾 로봇 특화"
date: 2026-11-19
tags: [technique-category]
---

<p class="tc-lead">로봇 정책·데이터·시뮬레이션에서 자주 쓰이는 기법.</p>
<div class="mh-section"><span>Action 표현</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/action-chunking"><h4>Action Chunking</h4><p>로봇에게 '한 걸음씩' 명령하는 대신 '앞으로 몇 초치 동작 묶음(청크)'을 한 번에 내려주는 기법 — 계단을 한 칸씩 오르지 않고 여러 칸을 미리 내다보며 오르는 것.</p><span class="tc-badge">초안</span></a><div class="tc-card tc-todo"><h4>Diffusion Policy</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div><a class="tc-card internal" href="/techniques/action-tokenization"><h4>Action Tokenization (FAST)</h4><p>로봇의 길고 자잘한 행동 궤적을 'MP3 압축하듯' 주파수로 눌러 담아, 몇 개의 토큰으로 줄여버리는 행동 토크나이저</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/motion-retargeting"><h4>Motion Retargeting</h4><p>체형이 다른 배우의 춤을 내 몸에 맞춰 다시 안무하는 것 — 사람(또는 다른 로봇)의 움직임을 타깃 로봇의 몸에 맞게 '번역'해 옮기는 기법</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/tool-center-point"><h4>Tool Center Point</h4><p>로봇 팔 끝에 붙은 공구가 '실제로 일하는 지점'을 기준점으로 삼는 약속 — 드라이버 손잡이가 아니라 드라이버 날 끝을 기준으로 움직이는 것.</p><span class="tc-badge">초안</span></a></div>
<div class="mh-section"><span>데이터</span></div>
<div class="tc-grid"><div class="tc-card tc-todo"><h4>Teleoperation Data Collection</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div><div class="tc-card tc-todo"><h4>Co-training</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div><a class="tc-card internal" href="/techniques/cross-embodiment-augmentation"><h4>Cross-Embodiment Augmentation</h4><p>여러 로봇의 경험을 한 로봇의 학습 데이터에 보태는 '로봇판 전학생 노트 빌려쓰기' — 팔 길이·센서·행동 공간이 달라도 공통점을 뽑아 학습을 도와주는 기법.</p><span class="tc-badge">초안</span></a></div>
<div class="mh-section"><span>Sim2Real·월드모델</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/domain-randomization"><h4>Domain Randomization</h4><p>시뮬레이터를 일부러 마구잡이로 흔들어 놓고 학습시켜서, 진짜 세상이 와도 '또 하나의 변형판'처럼 느껴지게 만드는 sim-to-real(시뮬레이션→실제 전이) 요령</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/world-model"><h4>World Model (Dreamer)</h4><p>로봇이 머릿속에 '세상의 축소판 시뮬레이터'를 만들어 두고, 그 안에서 상상으로 수없이 연습한 뒤 실제 행동을 결정하는 기법 (체스 두기 전에 머릿속으로 몇 수 앞을 그려보는 것)</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/gpu-native-rendering"><h4>GPU-native Rendering</h4><p>그림 그리는 일을 CPU가 GPU에 부탁하지 않고 GPU 안에서 처음부터 끝까지 처리해서, 수천 개 로봇 환경의 카메라 영상을 한꺼번에 뽑아내는 방식</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/batched-physics"><h4>Batched Physics</h4><p>수많은 로봇 시뮬레이션을 한 줄로 세워 동시에 계산하는 '물리 계산 분반 수업' — 한 번의 스텝으로 N개 환경의 다음 상태를 뽑는 기법</p><span class="tc-badge">초안</span></a></div>

[[techniques/index|← 기법 사전 전체]]
