/* Grace Dental Suite — small, dependency-free site script */
(function () {
  "use strict";
  var cfg = window.GDS || {};
  var host = location.hostname;
  // In the Claude preview, external embeds are blocked, so show tidy link cards instead.
  var PREVIEW = /claude\.(ai|site)|claudeusercontent|^$/.test(host) || location.protocol === "file:";

  // Mobile menu
  var toggle = document.querySelector(".menu-toggle");
  var menu = document.getElementById("menu");
  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      var open = menu.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && menu.classList.contains("open")) {
        menu.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
      }
    });
  }

  // Footer year
  var yr = document.getElementById("yr");
  if (yr) yr.textContent = new Date().getFullYear();

  // Load third-party embeds only when they scroll near the screen (faster pages, fewer cookies).
  function whenNear(el, fn) {
    if (!("IntersectionObserver" in window)) return fn();
    var io = new IntersectionObserver(function (entries) {
      if (entries[0].isIntersecting) { io.disconnect(); fn(); }
    }, { rootMargin: "400px" });
    io.observe(el);
  }
  function addScript(src) {
    if (document.querySelector('script[src="' + src + '"]')) {
      if (src.indexOf("instagram") > -1 && window.instgrm) window.instgrm.Embeds.process();
      return;
    }
    var s = document.createElement("script");
    s.src = src; s.async = true;
    document.body.appendChild(s);
  }

  document.querySelectorAll("[data-instagram]").forEach(function (el) {
    if (PREVIEW) return; // fallback card is already in the HTML
    whenNear(el, function () {
      // Keep the fallback card inside the embed: if Instagram's script is blocked, the card still shows.
      el.innerHTML = '<blockquote class="instagram-media" data-instgrm-permalink="' + el.dataset.instagram +
        '" data-instgrm-version="14" data-instgrm-captioned>' + el.innerHTML + '</blockquote>';
      addScript("https://www.instagram.com/embed.js");
    });
  });

  document.querySelectorAll("[data-tiktok]").forEach(function (el) {
    if (PREVIEW) return;
    var url = el.dataset.tiktok;
    var id = (url.match(/video\/(\d+)/) || [])[1];
    if (!id) return;
    whenNear(el, function () {
      el.innerHTML = '<blockquote class="tiktok-embed" cite="' + url + '" data-video-id="' + id +
        '" style="max-width:605px;min-width:0"><section>' + el.innerHTML + '</section></blockquote>';
      addScript("https://www.tiktok.com/embed.js");
    });
  });

  // Gallery TikToks: load the player only when tapped (one at a time keeps TikTok happy and pages light)
  document.querySelectorAll("[data-tiktok-click]").forEach(function (el) {
    if (PREVIEW) return;
    var id = (el.dataset.tiktokClick.match(/video\/(\d+)/) || [])[1];
    var card = el.querySelector("a");
    if (!id || !card) return;
    card.addEventListener("click", function (e) {
      e.preventDefault();
      var title = card.querySelector("b") ? card.querySelector("b").textContent : "TikTok video";
      el.innerHTML = '<iframe class="tt-player" src="https://www.tiktok.com/player/v1/' + id +
        '?autoplay=1&rel=0" title="' + title.replace(/"/g, "&quot;") + '" allow="autoplay; fullscreen; encrypted-media" allowfullscreen loading="lazy"></iframe>';
    });
  });

  document.querySelectorAll("[data-map]").forEach(function (el) {
    if (PREVIEW) return;
    whenNear(el, function () {
      el.innerHTML = '<iframe title="Map showing Grace Dental Suite in Parow" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=' +
        encodeURIComponent(el.dataset.map) + '&output=embed"></iframe>';
    });
  });

  // Before/after sliders
  document.querySelectorAll(".ba-frame").forEach(function (frame) {
    var range = frame.querySelector(".ba-range");
    if (!range) return;
    range.addEventListener("input", function () { frame.style.setProperty("--pos", range.value + "%"); });
  });

  // Booking form → opens WhatsApp with the request already written. No server needed.
  var form = document.getElementById("book-form");
  if (form) {
    var err = form.querySelector(".form-error");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = form.elements;
      var missing = [];
      if (!f.name.value.trim()) missing.push(f.name);
      if (!f.phone.value.trim()) missing.push(f.phone);
      if (!f.consent.checked) missing.push(f.consent);
      if (missing.length) {
        err.textContent = "Please add your name and phone number, and tick the consent box.";
        err.style.display = "block";
        missing[0].focus();
        return;
      }
      err.style.display = "none";
      var lines = [
        "Hi Grace Dental Suite, I'd like to book an appointment.",
        "",
        "Name: " + f.name.value.trim(),
        "Phone: " + f.phone.value.trim(),
        "Treatment: " + f.treatment.value,
        "Medical aid: " + f.aid.value,
        f.when.value.trim() ? "Preferred time: " + f.when.value.trim() : "",
        f.message.value.trim() ? "Note: " + f.message.value.trim() : ""
      ].filter(function (l, i) { return l !== "" || i === 1; });
      var url = "https://wa.me/" + (cfg.whatsapp || "") + "?text=" + encodeURIComponent(lines.join("\n"));
      window.open(url, "_blank", "noopener");
    });
  }
})();
