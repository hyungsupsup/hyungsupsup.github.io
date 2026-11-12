# 프로젝트 전체(비공개 파일 포함)를 private 저장소 supnote에 백업한다.
# 공개 저장소(.git)와 별개인 git 디렉터리 .git-supnote 를 사용한다.
param([string]$Message = "sync $(Get-Date -Format 'yyyy-MM-dd HH:mm')")
Set-Location $PSScriptRoot
git config core.safecrlf false
$env:GIT_CONFIG_PARAMETERS = "'core.safecrlf=false'"
$g = @("--git-dir=.git-supnote", "--work-tree=.")

if (-not (Test-Path .git-supnote)) {
    git init -q --bare .git-supnote
    git @g config core.bare false
    git @g remote add origin https://github.com/hyungsupsup/supnote.git
    git @g checkout -q -b main 2>$null
}

git @g add -A
# 공개 .gitignore가 제외하는 비공개 파일은 강제로 포함 (.env 비밀키는 제외)
git @g add -f private CLAUDE.local.md
git @g reset -q -- .env 2>$null
git @g commit -q -m $Message 2>$null
git @g push -u origin main
