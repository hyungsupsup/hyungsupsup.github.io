// [섭노트 custom] 상단 탭 내비게이션.
// SPA 이동 시 body가 다시 맞춰지며 삽입한 요소가 지워지므로 "nav"마다 다시 붙인다.
const TABS: [string, string][] = [
  ["홈", ""],
  ["데일리", "daily"],
  ["기법 사전", "techniques"],
  ["지식 창고", "knowledge"],
  ["실험실", "lab"],
  ["열린 질문", "open-questions"],
  ["로드맵", "roadmap"],
]

function currentSlug(): string {
  return document.body.dataset.slug ?? ""
}

function isActive(target: string, slug: string): boolean {
  if (target === "") return slug === "index" || slug === ""
  return slug === target || slug.startsWith(target + "/")
}

function renderTopnav() {
  const bar = document.querySelector<HTMLElement>('.page[data-frame="default"] .sidebar.left')
  if (!bar) return
  bar.querySelector(".sn-topnav")?.remove()
  const slug = currentSlug()
  const nav = document.createElement("nav")
  nav.className = "sn-topnav"
  nav.setAttribute("aria-label", "주요 메뉴")
  for (const [label, target] of TABS) {
    const a = document.createElement("a")
    a.href = "/" + (target && !target.includes("-") || target === "" ? target + (target ? "/" : "") : target)
    a.textContent = label
    a.className = "internal"
    if (isActive(target, slug)) {
      a.classList.add("active")
      a.setAttribute("aria-current", "page")
    }
    nav.appendChild(a)
  }
  bar.appendChild(nav)
}

document.addEventListener("nav", renderTopnav)
renderTopnav()
