# daily

매일 인사이트 생성 + 기법 사전 자동 확장. LLM 설정은 루트 `.env` (paper-db와 공유).

```powershell
python tools/daily/daily.py run                          # 오늘 것 1회 생성
python tools/daily/daily.py serve --at 07:30 --push      # 상주: 매일 07:30 생성 후 push
python tools/daily/daily.py serve --at 07:30 --push --cards 3   # 기법 카드 하루 3장
python tools/daily/daily.py card "Mamba" --category "시퀀스 대안" # 카드 1장 수동 생성
```

- 기법 목록: `techniques.json` (분류별). 카드가 없는 기법부터 순서대로 생성.
- 출력: `notes/techniques/<slug>.md`, `notes/daily/YYYY-MM-DD.md`
- `serve`: 1분마다 확인, 지정 시각 이후 오늘 노트가 없으면 생성 (PC를 늦게 켜도 그날 것 생성). 실패 시 10분 후 재시도.
