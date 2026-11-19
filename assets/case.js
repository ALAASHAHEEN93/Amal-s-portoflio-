// Shared behaviour for case study pages
(function () {
  // remember the chosen language so the home page opens in it too
  try { localStorage.setItem("lang", document.documentElement.lang); } catch (e) {}
  document.querySelectorAll("a.lang").forEach(a => a.addEventListener("click", () => {
    try { localStorage.setItem("lang", a.dataset.lang); } catch (e) {}
  }));

  // lightbox
  const lb = document.getElementById("lb"), lbi = lb.querySelector("img");
  document.querySelectorAll(".cover img,.screens img,.boards img").forEach(i => i.addEventListener("click", () => {
    lbi.src = i.src; lb.classList.add("open"); lb.scrollTop = 0; document.body.style.overflow = "hidden";
  }));
  const close = () => { lb.classList.remove("open"); document.body.style.overflow = ""; };
  lb.addEventListener("click", close);
  addEventListener("keydown", ev => { if (ev.key === "Escape") close(); });

  // full boards toggle
  const bt = document.getElementById("bt"), bd = document.getElementById("boards");
  if (bt) bt.addEventListener("click", () => {
    const o = bd.classList.toggle("open");
    bt.setAttribute("aria-expanded", o);
    bt.textContent = o ? bt.dataset.close : bt.dataset.open;
    if (!o) bt.scrollIntoView({ block: "center" });
  });

  // reading progress
  const pb = document.getElementById("pb");
  addEventListener("scroll", () => {
    const h = document.documentElement;
    pb.style.width = (h.scrollTop / (h.scrollHeight - h.clientHeight) * 100) + "%";
  }, { passive: true });

  // reveal on scroll
  const io = new IntersectionObserver(es => es.forEach(x => {
    if (x.isIntersecting) { x.target.classList.add("in"); io.unobserve(x.target); }
  }), { threshold: .08 });
  document.querySelectorAll(".rv").forEach(x => io.observe(x));
})();
