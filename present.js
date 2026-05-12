/* Presentation Mode · per-page deck where each <section> becomes a slide.
   - Hotkey: P toggles. ESC exits.
   - Navigate: ArrowRight/Down/Space/PageDown = next; ArrowLeft/Up/PageUp = prev.
   - Home / End jump to first / last slide.
   - Slide title derived from the section's .section-label or heading. */
(function () {
  'use strict';

  var SLIDE_SELECTOR = 'body > section';
  var STATE = { active: false, idx: 0, slides: [] };

  function enter() {
    if (STATE.active) return;
    STATE.slides = Array.prototype.slice.call(document.querySelectorAll(SLIDE_SELECTOR));
    if (!STATE.slides.length) return;
    STATE.active = true;
    document.body.classList.add('present-mode');
    buildChrome();
    show(0);
  }

  function exit() {
    if (!STATE.active) return;
    STATE.active = false;
    document.body.classList.remove('present-mode');
    STATE.slides.forEach(function (s) { s.classList.remove('present-slide-active'); });
    var chrome = document.getElementById('present-chrome');
    if (chrome) chrome.remove();
  }

  function show(n) {
    if (n < 0) n = 0;
    if (n >= STATE.slides.length) n = STATE.slides.length - 1;
    STATE.idx = n;
    STATE.slides.forEach(function (s, i) {
      s.classList.toggle('present-slide-active', i === n);
    });
    var active = STATE.slides[n];
    if (active) active.scrollTop = 0;
    updateChrome();
  }

  function next() { show(STATE.idx + 1); }
  function prev() { show(STATE.idx - 1); }

  function slideTitle(slide) {
    var label = slide.querySelector('.section-label');
    if (label) return label.textContent.trim();
    var h = slide.querySelector('h1, h2');
    if (h) return h.textContent.trim();
    return '';
  }

  function buildChrome() {
    var chrome = document.createElement('div');
    chrome.id = 'present-chrome';
    chrome.innerHTML =
      '<div id="present-progress"><div id="present-progress-fill"></div></div>' +
      '<div id="present-counter"><span id="present-idx">1</span> / <span id="present-total">' + STATE.slides.length + '</span></div>' +
      '<div id="present-title"></div>' +
      '<div id="present-nav">' +
        '<button id="present-prev" aria-label="Previous slide" title="Previous (←)">' +
          '<svg width="11" height="11" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polyline points="7.5 2.5 4 6 7.5 9.5"/></svg>' +
        '</button>' +
        '<button id="present-next" aria-label="Next slide" title="Next (→)">' +
          '<svg width="11" height="11" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polyline points="4.5 2.5 8 6 4.5 9.5"/></svg>' +
        '</button>' +
        '<span class="hint">ESC to exit</span>' +
      '</div>';
    document.body.appendChild(chrome);
    document.getElementById('present-prev').addEventListener('click', prev);
    document.getElementById('present-next').addEventListener('click', next);
  }

  function updateChrome() {
    var idxEl = document.getElementById('present-idx');
    var fill = document.getElementById('present-progress-fill');
    var title = document.getElementById('present-title');
    var prevBtn = document.getElementById('present-prev');
    var nextBtn = document.getElementById('present-next');
    if (idxEl) idxEl.textContent = String(STATE.idx + 1);
    if (fill) fill.style.width = ((STATE.idx + 1) / STATE.slides.length * 100) + '%';
    if (title) title.textContent = slideTitle(STATE.slides[STATE.idx]) || '';
    if (prevBtn) prevBtn.disabled = STATE.idx === 0;
    if (nextBtn) nextBtn.disabled = STATE.idx === STATE.slides.length - 1;
  }

  function inField(t) {
    return t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.isContentEditable);
  }

  document.addEventListener('keydown', function (e) {
    if (inField(e.target)) return;
    if (!STATE.active) {
      if (e.key === 'p' || e.key === 'P') { enter(); e.preventDefault(); }
      return;
    }
    switch (e.key) {
      case 'Escape':
      case 'p':
      case 'P':
        exit(); e.preventDefault(); break;
      case 'ArrowRight':
      case 'ArrowDown':
      case 'PageDown':
      case ' ':
        next(); e.preventDefault(); break;
      case 'ArrowLeft':
      case 'ArrowUp':
      case 'PageUp':
        prev(); e.preventDefault(); break;
      case 'Home':
        show(0); e.preventDefault(); break;
      case 'End':
        show(STATE.slides.length - 1); e.preventDefault(); break;
    }
  });

  function addToggle() {
    if (document.getElementById('present-toggle')) return;
    var btn = document.createElement('button');
    btn.id = 'present-toggle';
    btn.type = 'button';
    btn.title = 'Presentation mode (P)';
    btn.setAttribute('aria-label', 'Enter presentation mode');
    btn.innerHTML =
      '<svg width="13" height="13" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">' +
        '<rect x="1.5" y="2.5" width="13" height="9" rx="1"/><path d="M5 14h6M8 11.5V14"/>' +
      '</svg><span>Present</span>';
    btn.addEventListener('click', enter);
    document.body.appendChild(btn);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', addToggle);
  } else {
    addToggle();
  }
})();
