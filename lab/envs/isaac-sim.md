# Isaac Sim 6.2.0.0 환경

- 위치: `robot/.venv` (Python 3.12.7, uv)
- 설치 상세와 문제 해결: `notes/lab/experiments/000-isaac-sim-setup.md`

```powershell
# 재설치
uv venv --python 3.12 .venv
uv pip install --python .venv\Scripts\python.exe "isaacsim[all,extscache]==6.2.0.0" `
  --extra-index-url https://pypi.nvidia.com --index-strategy unsafe-best-match --prerelease=allow

# GUI 실행
.venv\Scripts\isaacsim.exe

# standalone 스크립트 실행 (EULA 비대화형 동의)
$env:OMNI_KIT_ACCEPT_EULA="YES"; .venv\Scripts\python.exe lab\experiments\NNN-이름\src\main.py
```
