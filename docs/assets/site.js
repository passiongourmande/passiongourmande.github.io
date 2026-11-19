// Passion Gourmande: navigation, language switch, order-request form
(function () {
  const header = document.querySelector(".site-header");
  const root = header ? header.dataset.root : "";
  const file = (location.pathname.split("/").pop() || "index.html").replace(/#.*$/, "");
  const page = file.endsWith(".html") ? file : "index.html";

  // current page in nav
  document.querySelectorAll(".site-nav a[data-page]").forEach(a => {
    if (a.dataset.page + ".html" === page) a.setAttribute("aria-current", "page");
  });

  // language switch -> same page in the other language (English at the root)
  document.querySelectorAll(".lang-switch a[data-lang]").forEach(a => {
    const l = a.dataset.lang;
    a.href = root + (l === "en" ? "" : l + "/") + page + location.hash;
  });

  // mobile menu
  const toggle = document.querySelector(".nav-toggle");
  const nav = document.getElementById("site-nav");
  if (toggle && nav) toggle.addEventListener("click", () => {
    const open = nav.classList.toggle("open");
    toggle.setAttribute("aria-expanded", open);
  });

  // order form (2 steps -> email / WhatsApp / Instagram DM; nothing is stored or sent by the site)
  document.querySelectorAll(".quote form").forEach(form => {
    const box = form.closest(".quote");
    const stepNo = box.querySelector(".stepno");
    const bar = box.querySelector(".progress i");
    const steps = [...form.querySelectorAll(".step")];
    const summary = box.querySelector(".summary");
    const show = n => {
      steps.forEach(s => (s.hidden = s.dataset.step !== String(n)));
      stepNo.textContent = n === 1 ? stepNo.dataset.s1 : n === 2 ? stepNo.dataset.s2 : "✓";
      bar.style.width = n === 1 ? "50%" : "100%";
      form.querySelectorAll(".error").forEach(e => (e.style.display = "none"));
      if (n > 1) box.scrollIntoView({ behavior: "smooth", block: "start" });
    };
    const checked = name => [...form.querySelectorAll(`[name="${name}"]:checked`)].map(i => i.value);
    const val = name => (form.elements[name] ? form.elements[name].value.trim() : "");
    const err = n => (steps[n - 1].querySelector(".error").style.display = "block");

    // no past dates
    const d = form.elements["date"];
    if (d) d.min = new Date().toISOString().slice(0, 10);

    form.querySelector("[data-next]").addEventListener("click", () => {
      if (!checked("occasion").length || !checked("items").length || !val("date")) return err(1);
      show(2);
    });
    form.querySelectorAll("[data-back]").forEach(b =>
      b.addEventListener("click", () => show(b.closest(".step").dataset.step === "3" ? 2 : 1)));

    form.addEventListener("submit", e => {
      e.preventDefault();
      const phoneOk = val("tel").replace(/\D/g, "").length >= 7;
      const mailOk = /\S+@\S+\.\S+/.test(val("email"));
      if (!val("nom") || !(phoneOk || mailOk)) return err(2);
      // plain-text summary built from the visible labels (follows the page language)
      const lines = [form.dataset.intro, ""];
      const label = el => el.textContent.replace("*", "").trim();
      form.querySelectorAll(".step[data-step='1'] > *, .step[data-step='2'] > *").forEach(block => {
        const parts = block.matches(".row2") ? [...block.children] : [block];
        parts.forEach(p => {
          if (p.matches("fieldset")) {
            const v = [...p.querySelectorAll("input:checked")].map(i => i.value);
            if (v.length) lines.push(`${label(p.querySelector("legend"))} : ${v.join(", ")}`);
          } else if (p.matches(".field")) {
            const input = p.querySelector("input, textarea");
            if (input && input.value.trim()) lines.push(`${label(p.querySelector("label"))} : ${input.value.trim()}`);
          }
        });
      });
      const body = lines.join("\n");
      summary.value = body;
      const subject = `${form.dataset.subject} – ${val("nom")}`;
      const mail = box.querySelector("[data-send='mail']");
      if (mail) mail.href = `mailto:${form.dataset.email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
      const wa = box.querySelector("[data-send='wa']");
      if (wa) wa.href = `https://wa.me/${form.dataset.wa}?text=${encodeURIComponent(body)}`;
      show(3);
    });

    // Instagram can't be pre-filled: copy the text, then the link opens the DM
    const ig = box.querySelector("[data-send='ig']");
    if (ig) ig.addEventListener("click", () => {
      const done = () => (box.querySelector(".copied").hidden = false);
      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(summary.value).then(done, () => { summary.select(); document.execCommand("copy"); done(); });
      } else { summary.select(); try { document.execCommand("copy"); } catch (_) {} done(); }
    });
  });
})();
