# =============================================================================
# PRAVI AVTO - Glavna Flask aplikacija
# =============================================================================
# Backend za spletno aplikacijo "Pravi Avto".
# Uporablja Flask framework in podatke iz cars.py
# =============================================================================
import os
from flask import Flask, render_template, request, jsonify
from cars import AVTOMOBILI, poisci_avtomobile, poisci_avto_po_slugu

# Inicializacija Flask aplikacije
app = Flask(__name__)


# =============================================================================
# ROUTES (Poti do strani)
# =============================================================================

@app.route("/")
def domov():
    """
    Začetna stran aplikacije.
    Prikaže iskalni obrazec.
    """
    return render_template("index.html")


@app.route("/iskanje", methods=["POST"])
def iskanje():
    """
    Obdelava iskalne zahteve.
    Sprejme JSON z iskralnimi kriteriji in vrne rezultate.
    """
    
    # Pridobimo podatke iz zahteve
    podatki = request.get_json()
    
    # Budget je neobvezen - 0 ali None pomeni prikaži vse
    raw_budget = podatki.get("budget", 0)
    budget = int(raw_budget) if raw_budget else 0
    tip = podatki.get("tip", "vseeno")
    gorivo = podatki.get("gorivo", "vseeno")
    
    # Poiščemo ustrezne avtomobile
    rezultati = poisci_avtomobile(budget, tip, gorivo)
    
    # Pripravimo odgovor za JSON
    odgovor = []
    for r in rezultati:
        avto = r["avto"]
        odgovor.append({
            "id": avto["id"],
            "slug": avto["slug"],
            "polno_ime": avto["polno_ime"],
            "znamka": avto["znamka"],
            "model": avto["model"],
            "cena": avto["cena"],
            "letnik": avto["letnik"],
            "motor": avto["motor"],
            "gorivo": avto["gorivo"],
            "moc": avto["moc"],
            "kategorija": avto["kategorija"],
            "slika": avto["slika"],
            "opis": avto["opis"],
            "cas_0_100": avto.get("cas_0_100"),
            "masa": avto.get("masa"),
            "prtljaznik": avto.get("prtljaznik"),
            "ocena": r["ocena"],
            "nad_budgetom": r["nad_budgetom"],
            "razlika_cene": r["razlika_cene"]
        })
    
    return jsonify({
        "rezultati": odgovor,
        "skupaj": len(odgovor),
        "budget": budget,
        "tip": tip,
        "gorivo": gorivo
    })


@app.route("/avto/<slug>")
def avto_podrobnosti(slug):
    """
    Podstran posameznega avtomobila.
    Prikaže vse podrobnosti in prednosti/slabosti.
    
    Args:
        slug (str): URL slug avtomobila (npr. 'bmw-420i-f32')
    """
    
    avto = poisci_avto_po_slugu(slug)
    
    # Če avtomobil ne obstaja, prikaže 404
    if avto is None:
        return render_template("404.html"), 404
    
    return render_template("avto.html", avto=avto)


@app.route("/vsi-avtomobili")
def vsi_avtomobili():
    """
    Stran z vsemi avtomobili v bazi (za pregled).
    """
    return render_template("vsi.html", avtomobili=AVTOMOBILI)


# =============================================================================
# ZAGON APLIKACIJE
# =============================================================================

if __name__ == "__main__":
    # Debug mode za razvoj - izklopi pri produkciji!
    print("🚗 Pravi Avto aplikacija se zaganja...")
    print("📍 Dostopno na: http://localhost:5000")
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
