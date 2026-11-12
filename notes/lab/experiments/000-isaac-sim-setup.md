---
title: "000 · Isaac Sim 6.2 설치 (Windows 11, pip)"
date: 2026-11-12
tags: [lab, isaac-sim, setup]
status: 완료
---

## 목표
Windows 11 노트북(RTX 4060 8GB)에 Isaac Sim을 설치하고 GUI가 실행되는지 확인한다.

## 환경
| 항목 | 값 |
|---|---|
| OS | Windows 11 Home |
| GPU | RTX 4060 8GB (공식 최소사양 RTX 4080보다 낮음) |
| Driver | 566.36 |
| Isaac Sim | 6.2.0.0 (PyPI `isaacsim` 패키지) |
| Python | 3.12 (uv 가상환경) |

## 설치 과정
```powershell
uv venv --python 3.12 .venv
uv pip install --python .venv\Scripts\python.exe "isaacsim[all,extscache]==6.2.0.0" `
  --extra-index-url https://pypi.nvidia.com --index-strategy unsafe-best-match --prerelease=allow
.venv\Scripts\isaacsim.exe     # 첫 실행 시 EULA 동의, 셰이더 캐싱으로 수 분 걸림
```

## 결과
- ✅ 설치하고 GUI 창이 뜨는 것까지 확인

## 문제점 · 배운 것
1. **Python 버전**: Isaac Sim 6.x wheel은 `cp312`만 있음 → 시스템 Python(3.13) 대신 3.12 venv 필요
2. **pre-release 의존성**: `isaacsim-core`가 `tinyobjloader==2.0.0rc13`에 의존 → uv에서는 `--prerelease=allow` 필요 (pip에서는 `==`로 버전을 고정하면 그대로 받아짐)
3. **index 전략**: PyPI와 pypi.nvidia.com 양쪽에 있는 패키지 때문에 uv에서 `--index-strategy unsafe-best-match` 사용
4. **PowerShell 실행 정책**: `activate.ps1` 차단 → `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, 또는 `.venv\Scripts\isaacsim.exe`를 바로 실행
5. **EULA**: 비대화형 실행이라면 `OMNI_KIT_ACCEPT_EULA=YES` 필요

## 다음
- GPU 드라이버 업데이트 후 성능 확인
- 001 Franka pick & place
