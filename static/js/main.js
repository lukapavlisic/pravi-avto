// =============================================================================
// PRAVI AVTO - Glavna JavaScript logika
// =============================================================================

// --- DOM ELEMENTI ---
const searchForm    = document.getElementById('search-form');
const budgetInput   = document.getElementById('budget');
const resultsSection = document.getElementById('results-section');
const resultsGrid   = document.getElementById('results-grid');
const resultsCount  = document.getElementById('results-count');
const loadingOverlay = document.getElementById('loading-overlay');
const noResults     = document.getElementById('no-results');
const sortSelect    = document.getElementById('sort-select');

// Trenutni rezultati (za razvrščanje brez ponovnega iskanja)
let trenutniRezultati = [];
let trenutniBudget    = 0;

// =============================================================================
// KATEGORIJE
// =============================================================================
const KATEGORIJE = {
  sporten:   { label: 'Športen',   cls: 'chip-sport' },
  navaden:   { label: 'Navaden',   cls: '' },
  druzinski: { label: 'Družinski', cls: 'chip-druzinski' }
};

const GORIVO_LABELS = { bencin: 'Bencin', diesel: 'Diesel' };

// =============================================================================
// SHRANJEVANJE ISKANJA (sessionStorage)
// =============================================================================

function shraniIskanje(budget, tip, gorivo) {
  try {
    sessionStorage.setItem('pa_budget', budget);
    sessionStorage.setItem('pa_tip', tip);
    sessionStorage.setItem('pa_gorivo', gorivo);
  } catch(e) {}
}

function naložiIskanje() {
  try {
    const budget = sessionStorage.getItem('pa_budget');
    const tip    = sessionStorage.getItem('pa_tip');
    const gorivo = sessionStorage.getItem('pa_gorivo');
    if (!budget && !tip) return;

    if (budget && budgetInput) budgetInput.value = budget || '';

    if (tip) {
      const tipEl = document.querySelector(`input[name="tip"][value="${tip}"]`);
      if (tipEl) tipEl.checked = true;
    }
    if (gorivo) {
      const gorivoEl = document.querySelector(`input[name="gorivo"][value="${gorivo}"]`);
      if (gorivoEl) gorivoEl.checked = true;
    }
  } catch(e) {}
}

// =============================================================================
// ISKANJE
// =============================================================================

if (searchForm) {
  searchForm.addEventListener('submit', async function(e) {
    e.preventDefault();
    await izvejiIskanje();
  });
}

async function izvejiIskanje() {
  const budget = budgetInput.value.trim() ? parseInt(budgetInput.value) : 0;
  const tip    = document.querySelector('input[name="tip"]:checked')?.value || 'vseeno';
  const gorivo = document.querySelector('input[name="gorivo"]:checked')?.value || 'vseeno';

  if (budget && budget < 500) {
    prikaziNapako('Budget mora biti vsaj 500 €');
    return;
  }

  shraniIskanje(budget, tip, gorivo);
  prikaziLoading(true);
  resultsSection.classList.add('visible');

  setTimeout(() => {
    resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }, 100);

  try {
    const odgovor = await fetch('/iskanje', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ budget, tip, gorivo })
    });

    if (!odgovor.ok) throw new Error('Napaka pri iskanju');

    const podatki = await odgovor.json();
    trenutniRezultati = podatki.rezultati;
    trenutniBudget    = podatki.budget;

    prikaziLoading(false);
    prikaziRezultate(podatki.rezultati, podatki.budget);

  } catch(e) {
    console.error(e);
    prikaziLoading(false);
    prikaziNapako('Prišlo je do napake. Prosim poskusi znova.');
  }
}

// =============================================================================
// RAZVRŠČANJE
// =============================================================================

function razvrsti(rezultati, nacin) {
  const kopija = [...rezultati];
  switch(nacin) {
    case 'ujemanje':
      return kopija.sort((a, b) => b.ocena - a.ocena);
    case 'cena-asc':
      return kopija.sort((a, b) => a.cena - b.cena);
    case 'cena-desc':
      return kopija.sort((a, b) => b.cena - a.cena);
    case 'moc-desc':
      return kopija.sort((a, b) => b.moc - a.moc);
    case 'cas-asc':
      return kopija.sort((a, b) => (a.cas_0_100 || 99) - (b.cas_0_100 || 99));
    case 'letnik-desc':
      // Primerjamo začetni letnik (vzamemo prvo številko)
      return kopija.sort((a, b) => {
        const la = parseInt((a.letnik || '0').split('-')[0]);
        const lb = parseInt((b.letnik || '0').split('-')[0]);
        return lb - la;
      });
    default:
      return kopija;
  }
}

if (sortSelect) {
  sortSelect.addEventListener('change', function() {
    if (!trenutniRezultati.length) return;
    const razvrsceni = razvrsti(trenutniRezultati, this.value);
    izrisiKartice(razvrsceni, trenutniBudget);
  });
}

// =============================================================================
// PRIKAZ REZULTATOV
// =============================================================================

function prikaziRezultate(rezultati, budget) {
  resultsGrid.innerHTML = '';
  noResults.style.display = 'none';

  if (!rezultati.length) {
    noResults.style.display = 'block';
    resultsCount.textContent = '';
    // Skrijemo sort bar
    const sortBar = document.getElementById('sort-bar');
    if (sortBar) sortBar.style.display = 'none';
    return;
  }

  const budgetBesedilo = budget > 0 ? ` za budget do ${formatiraiCeno(budget)}` : '';
  resultsCount.textContent = `${rezultati.length} avtomobil${rezultati.length === 1 ? '' : rezultati.length < 5 ? 'i' : 'ov'} najdenih${budgetBesedilo}`;

  // Pokažemo sort bar
  const sortBar = document.getElementById('sort-bar');
  if (sortBar) sortBar.style.display = 'flex';

  // Resetiramo sort na ujemanje
  if (sortSelect) sortSelect.value = 'ujemanje';

  izrisiKartice(rezultati, budget);
}

function izrisiKartice(rezultati, budget) {
  resultsGrid.innerHTML = '';
  rezultati.forEach((avto, index) => {
    const kartica = ustvariKartico(avto, index + 1, budget);
    resultsGrid.appendChild(kartica);
  });
}

// =============================================================================
// KARTICA AVTOMOBILA
// =============================================================================

function ustvariKartico(avto, rang, budget) {
  const kat = KATEGORIJE[avto.kategorija] || { label: avto.kategorija, cls: '' };
  const card = document.createElement('div');
  card.className = 'car-card';
  card.style.animationDelay = `${Math.min(rang - 1, 5) * 0.07}s`;

  const cenaFormatirana = formatiraiCeno(avto.cena);

  const nadBudgetomHtml = avto.nad_budgetom
    ? `<div class="over-budget-tag">+${formatiraiCeno(avto.razlika_cene)} nad budgetom</div>`
    : '';

  // Slika — poskusi naložiti pravo, ob napaki pokaže placeholder
  const slikaHtml = `
    <img
      src="/static/images/${avto.slika}"
      alt="${avto.polno_ime}"
      class="car-image"
      onerror="this.outerHTML='<div class=\'car-image-placeholder\'><div class=\'placeholder-name\'>${avto.znamka}</div><div class=\'placeholder-model\'>${avto.model}</div></div>'"
    >`;

  // 0-100 badge samo za sportne
  const casBadge = avto.cas_0_100
    ? `<span class="meta-chip chip-perf">${avto.cas_0_100}s 0–100</span>`
    : '';

  // Letnik — vzamemo začetni letnik
  const letnikStart = avto.letnik ? avto.letnik.split('-')[0] : '';

  card.innerHTML = `
    <div class="car-rank ${rang === 1 ? 'rank-1' : ''}">${rang}</div>
    ${slikaHtml}
    <div class="car-body">
      <div class="car-header">
        <div>
          <div class="car-brand">${avto.znamka}</div>
          <div class="car-name">${avto.model}</div>
          <div class="car-letnik">${letnikStart ? 'od ' + letnikStart : ''}</div>
        </div>
        <div class="car-price">
          <div class="price-amount">${cenaFormatirana}</div>
          <div class="price-label">okvirna cena</div>
          ${nadBudgetomHtml}
        </div>
      </div>

      <div class="car-meta">
        <span class="meta-chip ${kat.cls}">${kat.label}</span>
        <span class="meta-chip">${GORIVO_LABELS[avto.gorivo] || avto.gorivo}</span>
        <span class="meta-chip">${avto.moc} KM</span>
        ${casBadge}
      </div>

      <p class="car-desc">${avto.opis}</p>

      <a href="/avto/${avto.slug}" class="btn-details">
        Več informacij
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <path d="M5 12h14M12 5l7 7-7 7"/>
        </svg>
      </a>
    </div>
  `;

  return card;
}

// =============================================================================
// POMOŽNE FUNKCIJE
// =============================================================================

function prikaziLoading(aktivno) {
  if (aktivno) {
    loadingOverlay.classList.add('active');
    resultsGrid.innerHTML = '';
    noResults.style.display = 'none';
    resultsCount.textContent = 'Iščem...';
    const sortBar = document.getElementById('sort-bar');
    if (sortBar) sortBar.style.display = 'none';
  } else {
    loadingOverlay.classList.remove('active');
  }
}

function formatiraiCeno(cena) {
  return new Intl.NumberFormat('sl-SI', {
    style: 'currency',
    currency: 'EUR',
    maximumFractionDigits: 0
  }).format(cena);
}

function prikaziNapako(sporocilo) {
  let errorEl = document.getElementById('form-error');
  if (!errorEl) {
    errorEl = document.createElement('div');
    errorEl.id = 'form-error';
    errorEl.style.cssText = `
      color: #b03030;
      background: rgba(176,48,48,0.07);
      border: 1px solid rgba(176,48,48,0.18);
      border-radius: 8px;
      padding: 10px 14px;
      font-size: 13px;
      margin-bottom: 16px;
    `;
    searchForm.insertBefore(errorEl, searchForm.firstChild);
  }
  errorEl.textContent = sporocilo;
  setTimeout(() => { if (errorEl) errorEl.remove(); }, 4000);
}

// =============================================================================
// FILTER NA STRANI "VSI AVTOMOBILI"
// =============================================================================

function filtrirajKategorijo(kategorija) {
  const kartice = document.querySelectorAll('.car-card[data-kategorija]');
  document.querySelectorAll('.cat-btn').forEach(g => {
    g.classList.toggle('active', g.dataset.kategorija === kategorija);
  });
  kartice.forEach(k => {
    const ujema = kategorija === 'vsi' || k.dataset.kategorija === kategorija;
    k.style.display = ujema ? '' : 'none';
    if (ujema) { k.style.animation = 'none'; k.offsetHeight; k.style.animation = ''; }
  });
}

// =============================================================================
// INICIALIZACIJA
// =============================================================================

document.addEventListener('DOMContentLoaded', () => {
  // Naložimo shranjeno iskanje
  naložiIskanje();

  // Filtri na strani vseh avtomobilov
  document.querySelectorAll('.cat-btn').forEach(btn => {
    btn.addEventListener('click', () => filtrirajKategorijo(btn.dataset.kategorija));
  });
});
