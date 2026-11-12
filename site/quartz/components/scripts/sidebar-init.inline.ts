// [섭노트 custom] 페이지가 그려지기 전에 저장된 사이드바 상태(너비·접힘)를 적용해서 깜빡임을 막는다.
{
  try {
    const root = document.documentElement
    for (const side of ["left", "right"]) {
      const w = localStorage.getItem(`sb-${side}-w`)
      if (w && /^\d+$/.test(w)) root.style.setProperty(`--sb-${side}-w`, `${w}px`)
      if (localStorage.getItem(`sb-${side}-collapsed`) === "1") {
        root.classList.add(`sb-${side}-collapsed`)
      }
    }
  } catch {
    // localStorage를 쓸 수 없으면 기본값으로 둔다
  }
}
