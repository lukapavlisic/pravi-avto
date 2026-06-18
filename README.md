# 🚗 PRAVI AVTO

Spletna aplikacija, ki pomaga uporabnikom najti primeren avtomobil glede na budget in želje.

---

## Struktura projekta

```
pravi-avto/
├── app.py              # Glavna Flask aplikacija (backend)
├── cars.py             # Podatkovna baza avtomobilov
├── requirements.txt    # Python paketi
├── static/
│   ├── css/
│   │   └── style.css   # Vsi stili (dizajn)
│   ├── js/
│   │   └── main.js     # Frontend logika (iskanje, kartice)
│   └── images/         # ← DODAJ SLIKE AVTOMOBILOV TUKAJ
└── templates/
    ├── base.html        # Osnova (header, footer)
    ├── index.html       # Začetna stran (iskanje)
    ├── avto.html        # Podstran avtomobila
    ├── vsi.html         # Stran z vsemi avtomobili
    └── 404.html         # Stran za napako
```

---

## Namestitev in zagon

### 1. Namesti Python pakete:
```bash
pip install -r requirements.txt
```

### 2. Zaženi aplikacijo:
```bash
python app.py
```

### 3. Odpri v brskalniku:
```
http://localhost:5000
```

---

## Dodajanje slik

Slike daj v mapo `/static/images/`.

Imena datotek, ki jih aplikacija pričakuje:
- `bmw420i.jpg`
- `audis5.jpg`
- `renaultlaguna.jpg`
- `golfgti.jpg`
- `mercc200coupe.jpg`
- `bmw320d.jpg`
- `audia3.jpg`
- `golf6.jpg`
- `bmw116i.jpg`
- `octavia3.jpg`
- `audia4avant.jpg`
- `bmwtouring.jpg`
- `passatb7.jpg`
- `volvov60.jpg`
- `superbcombi.jpg`

---

## Dodajanje novih avtomobilov

V datoteki `cars.py` dodaj nov slovar v seznam `AVTOMOBILI`:

```python
{
    "id": "unikaten-id",
    "znamka": "VW",
    "model": "Golf VII GTD",
    "polno_ime": "Volkswagen Golf VII GTD 2.0 TDI",
    "cena": 14000,
    "letnik": "2013–2017",
    "motor": "2.0 TDI diesel",
    "gorivo": "diesel",
    "moc": 184,
    "kategorija": "sporten",  # sporten / navaden / druzinski
    "slika": "golfgtd.jpg",
    "opis": "Kratek opis...",
    "prednosti": ["Prednost 1", "Prednost 2"],
    "slabosti": ["Slabost 1"],
    "poraba": "5.5–7 L/100km",
    "zakaj": "Zakaj je ta avto dober...",
    "slug": "vw-golf-gtd"   # URL: /avto/vw-golf-gtd
}
```

---

## Tehnologije

- **Backend:** Python + Flask
- **Frontend:** HTML5, CSS3, JavaScript (vanilla)
- **Podatkovna baza:** Python seznam (brez SQL)
- **Tipografija:** Inter + Barlow Condensed (Google Fonts)

---

*Zaključna naloga — Pravi Avto*
