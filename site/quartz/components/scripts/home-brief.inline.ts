// [supway custom] 로컬(내 PC)에서 홈을 열면, 로컬 전용 페이지(notes/brief/, git 제외)를 읽어
// 홈 맨 위에 카드로 끼워 넣는다. 공개 사이트에는 그 페이지가 없고, 이 스크립트도 로컬에서만 동작한다.
const LOCAL_HOSTS = ["localhost", "127.0.0.1"]

async function loadLocalCards() {
  if (!LOCAL_HOSTS.includes(location.hostname)) return
  if ((document.body.dataset.slug ?? "") !== "index") return
  const article = document.querySelector("article")
  if (!article || article.querySelector(".bf-home")) return

  let html = ""
  for (const url of ["/brief/", "/brief/index.html", "/brief.html"]) {
    try {
      const r = await fetch(url, { cache: "no-store" })
      if (r.ok) {
        html = await r.text()
        break
      }
    } catch {}
  }
  if (!html) return
  const src = new DOMParser().parseFromString(html, "text/html").querySelector(".bf")
  if (!src) return

  const box = document.createElement("div")
  box.className = "bf bf-home"
  const title = document.createElement("div")
  title.className = "mh-section"
  const date = src.getAttribute("data-day") || ""
  title.innerHTML = `<span>Today ${date}</span>`
  box.appendChild(title)
  const grid = document.createElement("div")
  grid.className = "bf-grid"
  for (const key of ["news", "housing", "jobs", "trivia"]) {
    const sec = src.querySelector(`.bf-${key}`)
    if (sec) grid.appendChild(sec)
  }
  box.appendChild(grid)
  article.prepend(box)
}

document.addEventListener("nav", () => {
  loadLocalCards()
})
loadLocalCards()
