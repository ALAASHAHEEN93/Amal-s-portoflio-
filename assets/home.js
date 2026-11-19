// Home page: advent calendar doors + English/Arabic switch
// ---- settings: fill in CV to show the "Download CV" button
const CV_FILE = ""; // e.g. "assets/Amal-Ahmed-CV.pdf"

// door number n -> projects[n-1]; each opens its own case study page in work/
const projects = [
  {page:"homely",           img:"thumb-homely.jpg",          en:["Homely","Mobile app","A seamless home shopping app for furniture, décor, plants and candles."],           ar:["Homely","تطبيق جوال","تطبيق تسوّق منزلي سلس للأثاث والديكور والنباتات والشموع."]},
  {page:"house-basket",     img:"thumb-basket.jpg",          en:["House Basket","Mobile app","سلة البيت — an online grocery app that makes weekly shopping fast."],         ar:["سلة البيت","تطبيق جوال","تطبيق بقالة أونلاين يجعل تسوّق الأسبوع سريعًا."]},
  {page:"flexora",          img:"thumb-flexora.jpg",         en:["Flexora","AI fitness","An AI coach that adapts workouts and meals to your energy and goals."],          ar:["Flexora","لياقة بالذكاء الاصطناعي","مدرّب ذكي يكيّف التمارين والوجبات حسب طاقتك وأهدافك."]},
  {page:"book-hub-landing", img:"thumb-bookhub-landing.jpg", en:["Book Hub Landing","Landing page","The marketing website for the Book Hub reading app."],                ar:["صفحة Book Hub","صفحة هبوط","الموقع التسويقي لتطبيق Book Hub للقراءة."]},
  {page:"book-hub-app",     img:"thumb-bookhub-app.jpg",     en:["Book Hub","Mobile app","Fast delivery, Arabic library, flexible payments and book borrowing."],          ar:["Book Hub","تطبيق جوال","توصيل سريع ومكتبة عربية ودفع مرن واستعارة الكتب."]},
  {page:"fashion-app",      img:"thumb-fashion.jpg",         en:["Fashion App","Mobile app","Style inspiration plus a size guide that recommends the right fit."],         ar:["تطبيق أزياء","تطبيق جوال","إلهام في الستايل ودليل مقاسات يقترح المقاس المناسب."]},
  {page:"magnolia-market",  img:"thumb-magnolia.jpg",        en:["Magnolia Market","E-commerce","A concept home-goods app with AR placement and reviews."],               ar:["Magnolia Market","تجارة إلكترونية","تطبيق تصوّري لمنتجات المنزل بالواقع المعزز والتقييمات."]},
  {page:"weather-app",      img:"thumb-weather.jpg",         en:["Weather App","Mobile UI","Hourly and 7-day forecasts, air quality and UV at a glance."],                ar:["تطبيق الطقس","واجهة جوال","توقعات كل ساعة ولسبعة أيام وجودة الهواء بنظرة."]},
  {page:"power-energy",     img:"thumb-electrical.jpg",      en:["Power Energy","E-commerce","An electronics store website with categories and filters."],                ar:["Power Energy","تجارة إلكترونية","موقع متجر أجهزة إلكترونية بالفئات والفلاتر."]},
  {page:"coffee-app",       img:"thumb-coffee.jpg",          en:["Coffee App","Mobile app","Order coffee, pay in a few taps and track it live."],                         ar:["تطبيق قهوة","تطبيق جوال","اطلب قهوتك وادفع بضغطات قليلة وتابعها مباشرة."]},
  {page:"dashboard",        img:"thumb-dashboard.jpg",       en:["Dashboard","Web","An analytics dashboard for traffic, users and status."],                              ar:["لوحة التحكم","ويب","لوحة تحليلات للزيارات والمستخدمين والحالة."]},
  {page:"shopping-app",     img:"thumb-shopping.jpg",        en:["Shopping App","Mobile app","Gift shopping for watches and accessories, with swipe-to-pay."],            ar:["تطبيق تسوق","تطبيق جوال","تسوّق هدايا الساعات والإكسسوارات مع الدفع بالسحب."]},
];
const order = [7,1,11,4,9,3,12,6,2,10,5,8];

const AR = {
  logo:"أمل", nWork:"الأعمال", nAbout:"عني", nProcess:"طريقتي", nContact:"تواصل", talk:"تواصلي معي ↗", talk2:"لنتحدث ↗",
  eyebrow:"12 بابًا · ملف أعمال واحد",
  h1:"أهلًا، أنا <em>أمل،</em> مصممة UI/UX بعقلٍ فضولي.",
  lede:"كل باب في تقويمي يخفي دراسة حالة من أعمالي. مرّر المؤشر على الباب لتلقي نظرة — واضغط لتقرأ القصة كاملة.",
  openAll:"افتح كل الأبواب", name:"أمل أحمد", role:"مصممة UI/UX", city:"القاهرة، مصر", avail:"متاحة للعمل الحر والدوام الكامل",
  aboutEy:"عني", aboutH:"أصمّم <em>بعناية،</em> وأسلّم بهدف.",
  about1:"أنا مصممة UI/UX من القاهرة، مصر. أصمّم تطبيقات الجوال وصفحات الهبوط ولوحات التحكم لتكون سهلة الاستخدام وجميلة.",
  about2:"أتطلع دائمًا لعلاقات طويلة مع عملائي، وأن أقدّم لهم أعمالًا حديثة وراقية يفخرون بها. راسلني في أي وقت لنتحدث عن مشروعك.",
  s1:"مشاهدة للمشاريع", s2:"إعجاب", s3:"متابع", s4:"على Behance منذ",
  procH:"كيف <em>أعمل</em>", procEy:"التفكير التصميمي في كل مشروع",
  st1:"التعاطف", st1p:"أسئلة أصحاب المصلحة ومقابلات المستخدمين والاستبيانات وتحليل المنافسين.",
  st2:"التحديد", st2p:"خرائط التعاطف والشخصيات وعبارات المشكلة وأسئلة «كيف يمكننا» والقصص المصورة.",
  st3:"توليد الأفكار", st3p:"فرز البطاقات ومصفوفة الأولويات وهيكلة المعلومات ورحلات المستخدم.",
  st4:"النموذج الأولي", st4p:"نظام التصميم والرسومات والإطارات السلكية والنماذج عالية الدقة.",
  toolkit:"الأدوات", uxr:"بحث تجربة المستخدم",
  door13:"الباب 13 · تواصل", helloH:"قل <em>مرحبًا.</em>", helloP:"متاحة لمشاريع العمل الحر والوظائف بدوام كامل. لنصنع معًا شيئًا يحب الناس استخدامه.",
  cLinked:"تواصل على LinkedIn ↗", cBehance:"وظّفني على Behance ↗", cCv:"حمّل السيرة الذاتية ↓",
  foot:"© 2026 أمل أحمد · القاهرة، مصر",
};
const UI = {
  en:{caseStudy:"Case study", read:"Read case study →", opened:n=>`${n} of 12 doors opened`, all:`All 12 open. <a href="#contact">Let's work together ↗</a>`, door:"Door", switchTo:"العربية", title:"Amal Ahmed — UI/UX Designer"},
  ar:{caseStudy:"دراسة حالة", read:"اقرأ دراسة الحالة ←", opened:n=>`فُتح ${n} من 12 بابًا`, all:`فُتحت الأبواب الـ12. <a href="#contact">لنعمل معًا ↗</a>`, door:"الباب", switchTo:"English", title:"أمل أحمد — مصممة UI/UX"},
};

// remember original English text
const EN = {};
document.querySelectorAll("[data-i]").forEach(el => { EN[el.dataset.i] = el.hasAttribute("data-html") ? el.innerHTML : el.textContent; });

let lang = "en";
try { lang = localStorage.getItem("lang") === "ar" ? "ar" : "en"; } catch (e) {}
const qs = new URLSearchParams(location.search).get("lang");
if (qs === "ar" || qs === "en") lang = qs; // share index.html?lang=ar for the Arabic version

const cal = document.getElementById("calendar");
const dots = document.getElementById("dots");
const progText = document.getElementById("progText");
const visited = new Set();
const canHover = matchMedia("(hover:hover)").matches;
const cells = [];

order.forEach(n => {
  const p = projects[n-1];
  const cell = document.createElement("div");
  cell.className = "cell";
  cell.innerHTML = `
    <a class="inside" tabindex="-1">
      <img src="assets/${p.img}" alt="" loading="lazy">
      <span class="n">${n}</span>
      <span class="eyebrow"></span>
      <h3></h3>
      <p></p>
      <span class="go"></span>
    </a>
    <div class="door" role="button" tabindex="0" aria-expanded="false">
      <span class="front"><span class="big">${n}</span><span class="lab"></span><span class="knob"></span></span>
      <span class="back"><span>amal</span></span>
    </div>`;
  const door = cell.querySelector(".door");
  const link = cell.querySelector(".inside");
  let pinned = false;
  const setOpen = o => {
    cell.classList.toggle("open", o);
    door.setAttribute("aria-expanded", o);
    link.tabIndex = o ? 0 : -1;
    if (o) { visited.add(n); updateProgress(); }
  };
  cell._open = () => { pinned = true; setOpen(true); };
  cell._render = () => {
    const [t, cat, d] = p[lang], u = UI[lang];
    link.href = `work/${p.page}${lang === "ar" ? "-ar" : ""}.html`;
    link.querySelector("img").alt = t;
    link.querySelector(".eyebrow").textContent = `${u.caseStudy} · ${cat}`;
    link.querySelector("h3").textContent = t;
    link.querySelector("p").textContent = d;
    link.querySelector(".go").textContent = u.read;
    cell.querySelector(".lab").textContent = cat;
    door.setAttribute("aria-label", `${u.door} ${n}: ${t}`);
  };
  if (canHover) {
    cell.addEventListener("mouseenter", () => setOpen(true));
    cell.addEventListener("mouseleave", () => { if (!pinned) setOpen(false); });
    door.addEventListener("click", () => { location.href = link.href; });
  } else {
    door.addEventListener("click", () => { pinned = true; setOpen(true); });
  }
  door.addEventListener("keydown", ev => {
    if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); pinned = true; setOpen(true); link.focus({preventScroll:true}); }
  });
  cells.push(cell);
  cal.appendChild(cell);
});

for (let i = 0; i < 12; i++) dots.appendChild(document.createElement("i"));
function updateProgress(){
  const c = visited.size, u = UI[lang];
  [...dots.children].forEach((d,i) => d.classList.toggle("on", i < c));
  progText.innerHTML = c === 12 ? u.all : u.opened(c);
}

function applyLang(){
  const html = document.documentElement;
  html.lang = lang; html.dir = lang === "ar" ? "rtl" : "ltr";
  document.title = UI[lang].title;
  document.querySelectorAll("[data-i]").forEach(el => {
    const k = el.dataset.i, v = lang === "ar" ? (AR[k] ?? EN[k]) : EN[k];
    if (el.hasAttribute("data-html")) el.innerHTML = v; else el.textContent = v;
  });
  document.getElementById("langBtn").textContent = UI[lang].switchTo;
  document.getElementById("langBtn").setAttribute("lang", lang === "ar" ? "en" : "ar");
  cells.forEach(c => c._render());
  updateProgress();
}
document.getElementById("langBtn").addEventListener("click", () => {
  lang = lang === "ar" ? "en" : "ar";
  try { localStorage.setItem("lang", lang); } catch (e) {}
  applyLang();
});

const cv = document.getElementById("cvBtn");
if (CV_FILE) { cv.href = CV_FILE; cv.hidden = false; }

applyLang();

document.getElementById("openAll").addEventListener("click", () => {
  cells.forEach((cell,i) => setTimeout(() => cell._open(), i*90));
});
setTimeout(() => {
  cells.forEach((c,i) => setTimeout(() => { c.classList.add("peek"); setTimeout(() => c.classList.remove("peek"), 260); }, 600 + i*60));
}, 200);

const io = new IntersectionObserver(es => es.forEach(e => {
  if (!e.isIntersecting) return;
  e.target.classList.add("in");
  e.target.querySelectorAll("[data-count]").forEach(el => {
    const to = +el.dataset.count, t0 = performance.now();
    const tick = t => { const k = Math.min(1,(t-t0)/1400); el.textContent = Math.round(to*(1-Math.pow(1-k,3))).toLocaleString(lang === "ar" ? "ar-EG" : "en"); if (k<1) requestAnimationFrame(tick); };
    requestAnimationFrame(tick);
  });
  io.unobserve(e.target);
}), {threshold:.15});
document.querySelectorAll(".rv").forEach(el => io.observe(el));
