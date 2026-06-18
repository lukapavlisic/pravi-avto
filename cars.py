# =============================================================================
# PRAVI AVTO - Podatkovna baza avtomobilov
# =============================================================================

AVTOMOBILI = [

    # =========================================================================
    # SPORTNI AVTOMOBILI
    # =========================================================================

    {
        "id": "bmw-420i-f32",
        "znamka": "BMW",
        "model": "420i Coupe F32 LCI",
        "polno_ime": "BMW F32 420i Coupe LCI",
        "cena": 15500,
        "letnik": "2015-2017",
        "motor": "2.0 turbo bencin (B48)",
        "gorivo": "bencin",
        "moc": 184,
        "kategorija": "sporten",
        "slika": "bmw420i.png",
        "slika_tuning": "bmw420i_tuning.png",
        "opis": "BMW 420i Coupe LCI je elegantni kupejski avto z odlično vozno dinamiko in premium notranjostjo. LCI osvežitev je prinesla modernejše žaromete LED in posodobljeno notranjost.",
        "prednosti": [
            "Izjemno lep kupejski dizajn",
            "Premium BMW notranjost",
            "Odlična vožna dinamika",
            "Zanesljiv motor B48",
            "Dobra vrednost za denar"
        ],
        "slabosti": [
            "Višji stroški vzdrževanja",
            "Majhen prtljažnik",
            "Omejen prostor zadaj",
            "Višja poraba v mestu"
        ],
        "poraba": "6.5-8.5 L/100km",
        "zakaj": "BMW 420i Coupe je avto za tiste, ki hočejo izstopati. Kupejska oblika, premium obcutek in odlična voznja ga naredijo za eno privlačnejsih vozil v tem cenovnem razredu.",
        "tuning": {
            "stage1_moc": 230,
            "stage1_opis": "S stage 1 remap na motorju B48 pridemo do približno 230 KM in 350 Nm navora. Sprememba je močno občutna pri pospešvanju od 2000 vrtljajev navzgor.",
            "stage1_cena": "250-400 EUR",
            "zvok_stock": "bmw420i_stock_sound.mp3",
            "zvok_tuning": "bmw420i_tuning_sound.mp3",
            "zvok_opis": "Z dodanim sport exhaust ali downpipe brez katalizatorja dobi B48 precej globlji in bolj agresiven ton, še posebej pri pospesvanju."
        },
                "cas_0_100": 7.4,
        "masa": 1520,
        "prtljaznik": 445,
        "slug": "bmw-420i-f32"
    },

    {
        "id": "audi-s5-b8",
        "znamka": "Audi",
        "model": "S5 Coupe B8",
        "polno_ime": "Audi S5 B8 Coupe 4.2 FSI",
        "cena": 13500,
        "letnik": "2007-2011",
        "motor": "4.2 V8 FSI bencin",
        "gorivo": "bencin",
        "moc": 354,
        "kategorija": "sporten",
        "slika": "audis5.png",
        "slika_tuning": "audis5_tuning.png",
        "opis": "Audi S5 B8 z V8 motorjem je eden redkih modernih avtomobilov z atmosferskim V8 zvokom in pravim sportskim karakterjem. Quattro pogon poskrbi za odlicno oprijemanje.",
        "prednosti": [
            "Legendarni 4.2 V8 zvok",
            "Quattro 4x4 pogon",
            "Prestizen Audi dizajn",
            "Odlicna zmogljivost (0-100 v 5.1s)",
            "Prostornejsa notranjost kot pri konkurenci"
        ],
        "slabosti": [
            "Visoka poraba goriva (12-15 L/100km)",
            "Visoki stroski vzdrzevanja V8",
            "Starejsi letnik",
            "Verizni gonilnik zahteva redno vzdrzevanje"
        ],
        "poraba": "12-15 L/100km",
        "zakaj": "Za ljubitelje avtomobilov, ki iscejo pravega sportnika z V8 motorjem in slogom. Audi S5 B8 je avto, ki ne pusti nikogar ravnodusnega.",
        "tuning": {
            "stage1_moc": 354,
            "stage1_opis": "Atmosferski V8 ne reagira na remap tako kot turbomotorji. Stage 1 prinese minimalno spremembo (priblizno +10-15 KM). Pravi tuning je pri izpuhu.",
            "stage1_cena": "150-250 EUR",
            "zvok_stock": "audis5_stock_sound.mp3",
            "zvok_tuning": "audis5_tuning_sound.mp3",
            "zvok_opis": "S sportnim izpuhom (npr. Milltek ali Akrapovic) dobi V8 popolnoma drug karakter. Zvok pri pospesvanju je eden najboljsih v razredu."
        },
                "cas_0_100": 5.1,
        "masa": 1735,
        "prtljaznik": 455,
        "slug": "audi-s5-b8"
    },

    {
        "id": "renault-laguna-coupe",
        "znamka": "Renault",
        "model": "Laguna Coupe 2.0T",
        "polno_ime": "Renault Laguna III Coupe 2.0 T",
        "cena": 5500,
        "letnik": "2008-2013",
        "motor": "2.0 turbo bencin",
        "gorivo": "bencin",
        "moc": 170,
        "kategorija": "sporten",
        "slika": "renaultlaguna.png",
        "slika_tuning": "renaultlaguna_tuning.png",
        "opis": "Renault Laguna Coupe je eleganten in pogosto spregledan avto, ki ponuja pravo kupejsko izkusnjo po dostopni ceni. Dizajn mu daje edinstven, casoven videz.",
        "prednosti": [
            "Edinstvena kupejska oblika",
            "Dostopna cena",
            "Udobna notranjost",
            "Dobra standardna oprema",
            "Presenetljivo dober pogon"
        ],
        "slabosti": [
            "Nizja prepoznavnost znamke",
            "Rezervni deli redkejsi",
            "Elektronske napake na starejsih",
            "Slabse vrednotenje pri prodaji"
        ],
        "poraba": "8-10 L/100km",
        "zakaj": "Laguna Coupe je idealna za tiste, ki hocejo kupejski avto z znacajem, ne da bi porabili ves denar za premium znamke.",
        "tuning": {
            "stage1_moc": 215,
            "stage1_opis": "2.0 turbo motor dobro reagira na remap. Stage 1 prinese do 215 KM in bistveno boljso odzivnost motorja po celem obratnem obmocju.",
            "stage1_cena": "200-350 EUR",
            "zvok_stock": "laguna_stock_sound.mp3",
            "zvok_tuning": "laguna_tuning_sound.mp3",
            "zvok_opis": "Z menjavo srednje glusnika ali cevi dobi 2.0T precej bolj sportski ton brez prevelikega hrupa."
        },
                "cas_0_100": 8.2,
        "masa": 1530,
        "prtljaznik": 383,
        "slug": "renault-laguna-coupe"
    },

    {
        "id": "vw-golf-gti-mk6",
        "znamka": "Volkswagen",
        "model": "Golf GTI Mk6",
        "polno_ime": "Volkswagen Golf VI GTI 2.0 TSI",
        "cena": 10500,
        "letnik": "2009-2013",
        "motor": "2.0 TSI turbo bencin",
        "gorivo": "bencin",
        "moc": 211,
        "kategorija": "sporten",
        "slika": "golfgti.png",
        "slika_tuning": "golfgti_tuning.png",
        "opis": "Golf GTI Mk6 je pravi hot-hatch klasik. Perfektna kombinacija prakticnosti in sportskih zmogljivosti. Eden najboljsih avtomobilov za vsakdanjo voznju z zabavnim pridihom.",
        "prednosti": [
            "Odlicno ravnanje",
            "Prakticen hatchback format",
            "Zanesljiv motor TSI",
            "Premium notranjost",
            "Odlicna vrednost za denar"
        ],
        "slabosti": [
            "Pogost med vozniki",
            "DSG menjalnik zahteva vzdrzevanje",
            "Trse vzmetenje v sport nastavitvi",
            "Visji zavarovalni razredi"
        ],
        "poraba": "7-9 L/100km",
        "zakaj": "Golf GTI je benchmark hot-hatcha. Ni treba izbirati med prakticnostjo in zabavo - GTI ponuja oboje.",
        "tuning": {
            "stage1_moc": 260,
            "stage1_opis": "EA888 motor je eden najboljsih za tuning. Stage 1 remap na originalni strojni opremi prinese 260-270 KM in do 380 Nm. Sprememba je mocno obcutna.",
            "stage1_cena": "250-400 EUR",
            "zvok_stock": "golfgti_stock_sound.mp3",
            "zvok_tuning": "golfgti_tuning_sound.mp3",
            "zvok_opis": "Z downpipe in sport izpuhom (Milltek, Remus) dobi GTI precej agresivnejsi zvok z izstreljevalnimi poki pri odpu plina."
        },
                "cas_0_100": 6.9,
        "masa": 1381,
        "prtljaznik": 350,
        "slug": "vw-golf-gti-mk6"
    },

    {
        "id": "mercedes-c200-w204-coupe",
        "znamka": "Mercedes-Benz",
        "model": "C200 Coupe W204",
        "polno_ime": "Mercedes-Benz C200 CGI Coupe W204",
        "cena": 11000,
        "letnik": "2011-2014",
        "motor": "1.8 turbo bencin CGI",
        "gorivo": "bencin",
        "moc": 184,
        "kategorija": "sporten",
        "slika": "mercc200coupe.png",
        "slika_tuning": "mercc200coupe_tuning.png",
        "opis": "Mercedes C200 Coupe W204 zdruzuje eleganco Mercedes-Benz z elegantno kupejsko obliko. Udobna, a se vedno dinamicna voznja ga postavlja med vodilne v svoji klasi.",
        "prednosti": [
            "Prestizen Mercedes dizajn",
            "Udobna in elegantna notranjost",
            "Zanesljiv bencinski motor",
            "Dobra standardna oprema",
            "Zraven premium znamke"
        ],
        "slabosti": [
            "Visji stroski vzdrzevanja",
            "Manjsi prtljaznik",
            "Zadnja klop tesna",
            "Rezervni deli dragi"
        ],
        "poraba": "7-9 L/100km",
        "zakaj": "Za tiste, ki cenijo Mercedes prestiz in hocejo elegantno kupejsko izkusnjo z zvezdico na pokrovu.",
        "tuning": {
            "stage1_moc": 220,
            "stage1_opis": "1.8 CGI motor dobro reagira na remap in stage 1 prinese priblizno 220-225 KM ter izboljsano odzivnost po celotnem obmocju.",
            "stage1_cena": "250-380 EUR",
            "zvok_stock": "mercc200_stock_sound.mp3",
            "zvok_tuning": "mercc200_tuning_sound.mp3",
            "zvok_opis": "Z zamenjavo izpusnega sistema dobi C200 precej globlji ton. Brabus ali sport izpuh sta popularni opciji."
        },
                "cas_0_100": 7.8,
        "masa": 1500,
        "prtljaznik": 390,
        "slug": "mercedes-c200-w204-coupe"
    },

    {
        "id": "bmw-135i-e82",
        "znamka": "BMW",
        "model": "135i Coupe E82",
        "polno_ime": "BMW E82 135i Coupe",
        "cena": 14000,
        "letnik": "2007-2012",
        "motor": "3.0 turbo bencin N54/N55",
        "gorivo": "bencin",
        "moc": 306,
        "kategorija": "sporten",
        "slika": "bmw135i.png",
        "slika_tuning": "bmw135i_tuning.png",
        "opis": "BMW 135i E82 je eden najbolj podcenjenih BMW-jev vseh casov. S 306 KM in zadnjim pogonom v kompaktnem kupejskem telesu je pravi sportnik za tiste, ki vedo kaj iscejo.",
        "prednosti": [
            "Mocen N54/N55 motor idealen za tuning",
            "Zadnji pogon - pravo BMW ravnanje",
            "Kompakten in lahek",
            "Odlicno razmerje moci in teze",
            "Cenejsi od vecjih BMW-jev"
        ],
        "slabosti": [
            "Visji stroski vzdrzevanja",
            "N54 ima znane tezave z turbinama",
            "Malce star dizajn",
            "Rezervni deli dragi"
        ],
        "poraba": "9-12 L/100km",
        "zakaj": "135i E82 je skrivnost med poznavalci. Za ceno manjsega BMW dobis mocnejsi motor kot v M3 E90 in neskoncen potential za tuning.",
        "tuning": {
            "stage1_moc": 370,
            "stage1_opis": "N54 in N55 sta narojena za tuning. Stage 1 remap prinese 360-380 KM in do 560 Nm navora brez nobenih strojnih sprememb. Izjemna sprememba.",
            "stage1_cena": "300-500 EUR",
            "zvok_stock": "bmw135i_stock_sound.mp3",
            "zvok_tuning": "bmw135i_tuning_sound.mp3",
            "zvok_opis": "N54 je znan po lepem zvoku sest valjnika. Z downpipe in sport izpuhom postane zvok eden najboljsih v razredu - globok, melodicen, s poki pri dvignjeni nogi."
        },
                "cas_0_100": 5.3,
        "masa": 1495,
        "prtljaznik": 260,
        "slug": "bmw-135i-e82"
    },

    {
        "id": "honda-civic-fn2",
        "znamka": "Honda",
        "model": "Civic Type R FN2",
        "polno_ime": "Honda Civic Type R FN2",
        "cena": 11000,
        "letnik": "2007-2011",
        "motor": "2.0 VTEC bencin",
        "gorivo": "bencin",
        "moc": 201,
        "kategorija": "sporten",
        "slika": "civictyperfn2.png",
        "slika_tuning": "civictyperfn2_tuning.png",
        "opis": "Honda Civic Type R FN2 je zadnji pravi Honda hot-hatch z atmosferskim VTEC motorjem. 201 KM brez turba, visoki vrtljaji in odlicno ravnanje ga naredijo za kultni avto.",
        "prednosti": [
            "Kultni VTEC zvok pri visokih vrtljajih",
            "Odlicno ravnanje brez turboja",
            "Zanesljiv Honda motor",
            "Lahek in agililen",
            "Kultni status med ljubitelji"
        ],
        "slabosti": [
            "Trdo vzmetenje za vsakdan",
            "Agresiven dizajn ni za vsakogar",
            "Visoka poraba pri visokih vrtljajih",
            "Manjsa zadnja sedeza"
        ],
        "poraba": "8-11 L/100km",
        "zakaj": "FN2 Type R je eden zadnjih cistokrvnih hot-hatchev z atmosferskim motorjem. Za tiste, ki cenijo cisto vozno izkusnjo brez turboja.",
        "tuning": {
            "stage1_moc": 220,
            "stage1_opis": "VTEC atmosferski motor nima turba za remap. Stage 1 (intake + exhaust + remap) prinese priblizno 215-220 KM. Pravi gain je v zvoku in odzivnosti.",
            "stage1_cena": "300-500 EUR",
            "zvok_stock": "civictyper_stock_sound.mp3",
            "zvok_tuning": "civictyper_tuning_sound.mp3",
            "zvok_opis": "VTEC zvok je legendarni. Z izpuhom (Mugen, Akrapovic) dobi motor se bolj znacilen krik pri visokih vrtljajih - povsem edinstven zvok."
        },
                "cas_0_100": 6.6,
        "masa": 1285,
        "prtljaznik": 280,
        "slug": "honda-civic-fn2"
    },

    {
        "id": "ford-focus-st-mk2",
        "znamka": "Ford",
        "model": "Focus ST Mk2",
        "polno_ime": "Ford Focus ST Mk2 2.5 turbo",
        "cena": 7500,
        "letnik": "2005-2011",
        "motor": "2.5 turbo bencin (Volvo motor)",
        "gorivo": "bencin",
        "moc": 225,
        "kategorija": "sporten",
        "slika": "focusst.png",
        "slika_tuning": "focusst_tuning.png",
        "opis": "Ford Focus ST Mk2 z 2.5 litrskim turbo motorjem je eden najbolj zabavnih hot-hatchev svoje dobe. 225 KM, odlicno ravnanje in dostopna cena ga naredijo za izvrstno izbiro.",
        "prednosti": [
            "225 KM za razumno ceno",
            "Izjemno ravnanje in agilnost",
            "Sportski videz",
            "Zanesljiv pri vzdrzevanju",
            "Dober zvok 5-valjnika"
        ],
        "slabosti": [
            "5-valjnik redkejsi za servis",
            "Visja poraba goriva",
            "Starejsi modeli kaze leta",
            "Nadomestni deli tezje dostopni"
        ],
        "poraba": "9-12 L/100km",
        "zakaj": "Focus ST Mk2 je eden redkih 5-valjnih hot-hatchev in ima edinstven zvok. Za ceno rabljeneaga Golf GTI dobis vec moci in vec karakterja.",
        "tuning": {
            "stage1_moc": 280,
            "stage1_opis": "2.5 turbo motor odlicno reagira na remap. Stage 1 prinese 275-285 KM in do 420 Nm navora. Spememba je mocno obcutna.",
            "stage1_cena": "250-400 EUR",
            "zvok_stock": "focusst_stock_sound.mp3",
            "zvok_tuning": "focusst_tuning_sound.mp3",
            "zvok_opis": "5-valjni motor ima povsem edinstven zvok - burble pri nizkih vrtljajih in agresiven krik pri visokih. Z izpuhom postane se bolj izrazit."
        },
                "cas_0_100": 6.8,
        "masa": 1367,
        "prtljaznik": 385,
        "slug": "ford-focus-st-mk2"
    },

    {
        "id": "seat-leon-cupra-mk2",
        "znamka": "SEAT",
        "model": "Leon Cupra Mk2",
        "polno_ime": "SEAT Leon II Cupra 2.0 TFSI",
        "cena": 7000,
        "letnik": "2006-2012",
        "motor": "2.0 TFSI turbo bencin",
        "gorivo": "bencin",
        "moc": 241,
        "kategorija": "sporten",
        "slika": "seatleon.png",
        "slika_tuning": "seatleon_tuning.png",
        "opis": "SEAT Leon Cupra Mk2 je sportski hatchback z Audi/VW tehnologijo po manjsi ceni. 241 KM, trden podvozju in agresiven videz ga naredijo za odlicno alternativo Golfu GTI.",
        "prednosti": [
            "241 KM za dostopno ceno",
            "Audi/VW motor in tehnologija",
            "Agresiven dizajn",
            "Odlicno ravnanje",
            "Dober zvok 2.0 TFSI"
        ],
        "slabosti": [
            "Manjsa prepoznavnost znamke",
            "Vzdrzevanje enako drago kot VW",
            "Manjse vrednotenje pri prodaji",
            "Manj luksuzna notranjost"
        ],
        "poraba": "8-11 L/100km",
        "zakaj": "Cupra je SEAT-ov odgovor na Golf GTI. Enaka mehanika, moc moci, agresivnejsi videz - za manjso ceno. Odlicna vrednost.",
        "tuning": {
            "stage1_moc": 300,
            "stage1_opis": "2.0 TFSI motor (isti kot v GTI) je izvrsten za tuning. Stage 1 prinese 295-310 KM in do 430 Nm. Sprememba je dramaticna.",
            "stage1_cena": "250-400 EUR",
            "zvok_stock": "seatleon_stock_sound.mp3",
            "zvok_tuning": "seatleon_tuning_sound.mp3",
            "zvok_opis": "Z downpipe in sport izpuhom dobi 2.0 TFSI globok, agresiven ton z znacilnimi turbopoki pri odpu plina."
        },
                "cas_0_100": 6.1,
        "masa": 1360,
        "prtljaznik": 341,
        "slug": "seat-leon-cupra-mk2"
    },

    {
        "id": "bmw-m135i-f20",
        "znamka": "BMW",
        "model": "M135i F20",
        "polno_ime": "BMW F20 M135i 3.0 turbo",
        "cena": 17000,
        "letnik": "2012-2015",
        "motor": "3.0 turbo bencin N55",
        "gorivo": "bencin",
        "moc": 320,
        "kategorija": "sporten",
        "slika": "bmwm135i.png",
        "slika_tuning": "bmwm135i_tuning.png",
        "opis": "BMW M135i F20 je eden najboljsih sportnih hatchbackov kar je bilo ustvarjenih. 320 KM, 6-valjni motor in zadnji pogon v kompaktnem BMW hatchbacku - kombinacija brez konkurenta.",
        "prednosti": [
            "320 KM 6-valjni motor",
            "Zadnji pogon - pravo BMW ravnanje",
            "Prakticen 5-vrata hatchback",
            "N55 motor idealen za tuning",
            "Premium BMW notranjost"
        ],
        "slabosti": [
            "Visja cena v razredu",
            "Visoka poraba goriva",
            "Visji stroski vzdrzevanja",
            "Zavarovanje drazje"
        ],
        "poraba": "9-13 L/100km",
        "zakaj": "M135i F20 je ultimativni dnevni sportnik. 320 KM, zadnji pogon, 5 vrat - nihce drug ne ponuja te kombinacije v tem segmentu.",
        "tuning": {
            "stage1_moc": 380,
            "stage1_opis": "N55 je eden najboljsih motorjev za tuning. Stage 1 remap prinese 375-385 KM in do 580 Nm navora - vse brez strojnih sprememb.",
            "stage1_cena": "300-500 EUR",
            "zvok_stock": "bmwm135i_stock_sound.mp3",
            "zvok_tuning": "bmwm135i_tuning_sound.mp3",
            "zvok_opis": "6-valjni N55 ze v originalnem stanju zveni odlicno. Z downpipe in Milltek izpuhom postane zvok res izjemen - globok, melodicen, s poki pri sproscanju plina."
        },
                "cas_0_100": 4.9,
        "masa": 1545,
        "prtljaznik": 360,
        "slug": "bmw-m135i-f20"
    },

    {
        "id": "opel-astra-opc",
        "znamka": "Opel",
        "model": "Astra OPC J",
        "polno_ime": "Opel Astra J OPC 2.0 turbo",
        "cena": 10000,
        "letnik": "2011-2015",
        "motor": "2.0 turbo bencin",
        "gorivo": "bencin",
        "moc": 280,
        "kategorija": "sporten",
        "slika": "astraopc.png",
        "slika_tuning": "astraopc_tuning.png",
        "opis": "Opel Astra OPC je agresiven hot-hatch z 280 KM, ki prihaja po bistveno nizji ceni kot Golf GTI ali Focus ST. Brembo zavore, Recarovo sedisc in trd podvozje potrjujejo sportski karakter.",
        "prednosti": [
            "280 KM za razumno ceno",
            "Brembo zavore serije",
            "Agresiven videz",
            "Odlicno ravnanje",
            "Dober zvok 2.0 turbo"
        ],
        "slabosti": [
            "Trdo vzmetenje za vsak dan",
            "Visoka poraba goriva",
            "Opel vzdrzevanje ni poceni",
            "Manj prestizna znamka"
        ],
        "poraba": "9-12 L/100km",
        "zakaj": "Astra OPC ponuja resno zmogljivost za manjsi denar kot nemska konkurenca. 280 KM in Brembo zavore za ceno normalnega Golfa.",
        "tuning": {
            "stage1_moc": 330,
            "stage1_opis": "2.0 turbo motor v OPC dobro reagira na remap. Stage 1 prinese 325-335 KM in do 460 Nm navora.",
            "stage1_cena": "250-400 EUR",
            "zvok_stock": "astraopc_stock_sound.mp3",
            "zvok_tuning": "astraopc_tuning_sound.mp3",
            "zvok_opis": "Z zamenjavo izpusnega sistema (npr. Milltek ali MSD) dobi Astra OPC precej globlji in sportski ton."
        },
                "cas_0_100": 6.0,
        "masa": 1415,
        "prtljaznik": 370,
        "slug": "opel-astra-opc"
    },

    {
        "id": "vw-scirocco-r",
        "znamka": "Volkswagen",
        "model": "Scirocco R",
        "polno_ime": "Volkswagen Scirocco R 2.0 TSI",
        "cena": 14000,
        "letnik": "2009-2014",
        "motor": "2.0 TSI turbo bencin",
        "gorivo": "bencin",
        "moc": 265,
        "kategorija": "sporten",
        "slika": "scirocco.png",
        "slika_tuning": "scirocco_tuning.png",
        "opis": "VW Scirocco R je sportni kupejski avto zgrajen na podlagi GTI-ja, a z bolj izrazitim dizajnom in vecjo moco. 265 KM in nizak kupejski profil ga naredijo za vizualno izstopajoc avto.",
        "prednosti": [
            "265 KM v kupejski obliki",
            "Edinstven dizajn za VW skupino",
            "Odlicna vozna dinamika",
            "Zanesljiv EA888 motor",
            "Redek na cestah"
        ],
        "slabosti": [
            "Majhen zadnji prostor",
            "Visja cena kot GTI",
            "Manjsi prtljaznik",
            "Servis enak kot pri VW"
        ],
        "poraba": "7-10 L/100km",
        "zakaj": "Scirocco R je za tiste, ki hocejo GTI zmogljivosti v bolj izrazitem dizajnu. Redek avto, ki pritegne poglede.",
        "tuning": {
            "stage1_moc": 320,
            "stage1_opis": "EA888 je odlicen za tuning. Stage 1 prinese 315-325 KM in do 450 Nm navora. Sprememba je mocno obcutna po celem obratnem obmocju.",
            "stage1_cena": "250-400 EUR",
            "zvok_stock": "scirocco_stock_sound.mp3",
            "zvok_tuning": "scirocco_tuning_sound.mp3",
            "zvok_opis": "Z Milltek ali Remus izpuhom dobi Scirocco R agresiven, globok ton z izstreljevalnimi poki ki mu prilegajo kupejskemu videzu."
        },
                "cas_0_100": 6.2,
        "masa": 1401,
        "prtljaznik": 312,
        "slug": "vw-scirocco-r"
    },

    # =========================================================================
    # NAVADNI AVTOMOBILI
    # =========================================================================

    {
        "id": "bmw-320d-e90-prelci",
        "znamka": "BMW",
        "model": "320d ED E90 pre-LCI",
        "polno_ime": "BMW E90 320d EfficientDynamics",
        "cena": 7500,
        "letnik": "2005-2008",
        "motor": "2.0 diesel (M47/N47)",
        "gorivo": "diesel",
        "moc": 163,
        "kategorija": "navaden",
        "slika": "bmw320d.png",
        "slika_tuning": "bmw320d_tuning.png",
        "opis": "BMW 320d ED iz serije E90 je legenda med dieselskimi sedani. Zdruzuje nizko porabo goriva z odlicno vozno dinamiko in BMW premium obcutkom za razumno ceno.",
        "prednosti": [
            "Nizka poraba goriva (5-6 L/100km)",
            "Odlicna voznja in ravnanje",
            "BMW premium obcutek",
            "Zanesljiv pri rednem vzdrzevanju",
            "Dobra vrednost za ceno"
        ],
        "slabosti": [
            "Pre-LCI zarometi manj moderni",
            "Verizni gonilnik N47 zahteva pozornost",
            "Stroski vzdrzevanja visji kot pri VW",
            "Rezervni deli drazji"
        ],
        "poraba": "5-6.5 L/100km",
        "zakaj": "BMW 320d ED je odlicna izbira za tiste, ki hocejo premium BMW izkusnjo z razumnimi stroski goriva. Idealen vsakodnevni avtomobil.",
        "tuning": {
            "stage1_moc": 200,
            "stage1_opis": "2.0 diesel motor se odlicno odziva na remap. Stage 1 prinese do 200 KM in 420 Nm navora. Poraba ostane podobna, odzivnost pa se mocno izboljsa.",
            "stage1_cena": "200-350 EUR",
            "zvok_stock": "bmw320d_stock_sound.mp3",
            "zvok_tuning": "bmw320d_tuning_sound.mp3",
            "zvok_opis": "Diesel zvok se s sportnim izpuhom spremeni v globlji, prijetnejsi ton. Ni dramaticno, ampak razlika je opazna."
        },
                "cas_0_100": 8.1,
        "masa": 1490,
        "prtljaznik": 460,
        "slug": "bmw-320d-e90-prelci"
    },

    {
        "id": "audi-a3-8p",
        "znamka": "Audi",
        "model": "A3 8P Sportback TDI",
        "polno_ime": "Audi A3 8P 1.6 TDI Sportback",
        "cena": 6500,
        "letnik": "2008-2012",
        "motor": "1.6 TDI diesel",
        "gorivo": "diesel",
        "moc": 105,
        "kategorija": "navaden",
        "slika": "audia3.png",
        "slika_tuning": "audia3_tuning.png",
        "opis": "Audi A3 8P Sportback je kompakten premium hatchback, ki ponuja Audi kakovost v manjsem paketu. Sportback oblika doda prakticnost brez zrtvovanja stila.",
        "prednosti": [
            "Premium Audi kakovost",
            "Majhna poraba TDI",
            "Prakticen Sportback format",
            "Cenovno dostopen vstop v Audi",
            "Dobro vzdrzevanje po vsej Evropi"
        ],
        "slabosti": [
            "1.6 TDI je zmogljivo omejen",
            "Notranjost na starejsih pokaze starost",
            "Manj prostora kot vecji avtomobili",
            "Manj zabaven od sportnih razlicic"
        ],
        "poraba": "4.5-6 L/100km",
        "zakaj": "Audi A3 je perfectna izbira za tiste, ki hocejo Audi prestiznost brez velikega avta in velikih stroskov.",
        "tuning": {
            "stage1_moc": 130,
            "stage1_opis": "1.6 TDI ima omejen potential za tuning. Stage 1 prinese priblizno 125-130 KM in do 280 Nm. Ni dramaticno, ampak odzivnost se izboljsa.",
            "stage1_cena": "180-300 EUR",
            "zvok_stock": "audia3_stock_sound.mp3",
            "zvok_tuning": "audia3_tuning_sound.mp3",
            "zvok_opis": "Z zamenjavo izpuha dobi diesel A3 nekoliko prijetnejsi ton, a sprememba ni dramaticna kot pri bencinarjih."
        },
                "cas_0_100": 12.3,
        "masa": 1315,
        "prtljaznik": 350,
        "slug": "audi-a3-8p"
    },

    {
        "id": "vw-golf-6-tdi",
        "znamka": "Volkswagen",
        "model": "Golf VI 1.6 TDI",
        "polno_ime": "Volkswagen Golf VI 1.6 TDI Comfortline",
        "cena": 5500,
        "letnik": "2009-2012",
        "motor": "1.6 TDI diesel",
        "gorivo": "diesel",
        "moc": 105,
        "kategorija": "navaden",
        "slika": "golf6.png",
        "slika_tuning": "golf6_tuning.png",
        "opis": "Volkswagen Golf VI je eden najbolj zanesljivih in priljubljenih avtomobilov v Evropi. Solidna gradnja, dobra oprema in nizka poraba ga naredijo za odlicno dnevno vozilo.",
        "prednosti": [
            "Izjemna zanesljivost",
            "Nizka poraba (4.5-6 L/100km)",
            "Enostavno vzdrzevanje",
            "Rezervni deli poceni in dostopni",
            "Dobra vrednost pri nadaljnji prodaji"
        ],
        "slabosti": [
            "Ne izstopa v mnozici",
            "Notranjost preprosta",
            "1.6 TDI ni vznemirljiv",
            "Malo premalo opreme v bazi"
        ],
        "poraba": "4.5-6 L/100km",
        "zakaj": "Golf VI je avtomobil za tiste, ki hocejo zanesljiv, prakticen in cenovno ugoden avto brez presenecenj.",
        "tuning": {
            "stage1_moc": 130,
            "stage1_opis": "1.6 TDI stage 1 prinese 130 KM in 300 Nm. Izboljsanje je obcutno pri voznji na avtocesti in pripospesvanju.",
            "stage1_cena": "180-300 EUR",
            "zvok_stock": "golf6_stock_sound.mp3",
            "zvok_tuning": "golf6_tuning_sound.mp3",
            "zvok_opis": "Golf 6 z izpuhom dobi rahlo bolj sportski diesel ton, ki je precej prijetnejsi od originalnega."
        },
                "cas_0_100": 12.1,
        "masa": 1337,
        "prtljaznik": 350,
        "slug": "vw-golf-6-tdi"
    },

    {
        "id": "bmw-116i-f20",
        "znamka": "BMW",
        "model": "116i Serija 1 F20",
        "polno_ime": "BMW F20 116i 5-vrat",
        "cena": 9000,
        "letnik": "2012-2015",
        "motor": "1.6 turbo bencin (N13)",
        "gorivo": "bencin",
        "moc": 136,
        "kategorija": "navaden",
        "slika": "bmw116i.png",
        "slika_tuning": "bmw116i_tuning.png",
        "opis": "BMW 116i F20 je vstopni model serije 1 z zadnjim pogonom. Premium BMW izkusnja v kompaktnem hatchbacku - zadnji pogon doda dinamiki vsakdanje voznje.",
        "prednosti": [
            "Zadnji pogon - pravo BMW ravnanje",
            "Premium BMW notranjost",
            "Kompakten za mesto",
            "Odlicno ravnanje",
            "Dostopna cena za BMW"
        ],
        "slabosti": [
            "Motor 1.6 turbo ni najmocnejsi",
            "Manjsi prtljaznik",
            "Zadnji sedez tesnejs",
            "Visji stroski vzdrzevanja"
        ],
        "poraba": "6-8 L/100km",
        "zakaj": "BMW serija 1 F20 je ena redkih premium compact hatchbackov z zadnjim pogonom. Za tiste, ki hocejo prava BMW vozna lastnosti v mestnem paketu.",
        "tuning": {
            "stage1_moc": 175,
            "stage1_opis": "1.6 turbo N13 motor dobro reagira na remap. Stage 1 prinese do 175 KM in boljso odzivnost skozi celotno obmocje vrtljajev.",
            "stage1_cena": "220-380 EUR",
            "zvok_stock": "bmw116i_stock_sound.mp3",
            "zvok_tuning": "bmw116i_tuning_sound.mp3",
            "zvok_opis": "Z zamenjavo izpuha dobi 1.6 motor precej prijetnejsi sportski ton, ki nadomesti manjkajoce valje."
        },
                "cas_0_100": 9.1,
        "masa": 1390,
        "prtljaznik": 360,
        "slug": "bmw-116i-f20"
    },

    {
        "id": "skoda-octavia-a7",
        "znamka": "Skoda",
        "model": "Octavia III 2.0 TDI",
        "polno_ime": "Skoda Octavia III 2.0 TDI 150 KM",
        "cena": 11500,
        "letnik": "2013-2017",
        "motor": "2.0 TDI diesel",
        "gorivo": "diesel",
        "moc": 150,
        "kategorija": "navaden",
        "slika": "octavia3.png",
        "slika_tuning": "octavia3_tuning.png",
        "opis": "Skoda Octavia III 2.0 TDI je eno najboljsih razmerij med ceno in vrednostjo v segmentu. Ogromno prostora, zanesljiv motor in nizka poraba jo naredijo za skoraj popolno vozilo.",
        "prednosti": [
            "Ogromno prostora znotraj",
            "Nizka poraba goriva",
            "Zanesljiv in dolgotrajen",
            "Poceni vzdrzevanje",
            "Odlicna vrednost za denar"
        ],
        "slabosti": [
            "Manj prestizna znamka",
            "Notranjost malce plasticna",
            "Manj vznemirljiv za voznju",
            "Dizajn nevtralen"
        ],
        "poraba": "4.5-5.5 L/100km",
        "zakaj": "Octavia III je odlicna izbira za tiste, ki hocejo prakticen, zanesljiv avto z nizkimi stroski brez premium pribitka.",
        "tuning": {
            "stage1_moc": 190,
            "stage1_opis": "2.0 TDI je eden najboljsih diesel motorjev za remap. Stage 1 prinese 185-195 KM in do 420 Nm. Poraba se ne poslabsa, odzivnost se dramaticno izboljsa.",
            "stage1_cena": "200-350 EUR",
            "zvok_stock": "octavia_stock_sound.mp3",
            "zvok_tuning": "octavia_tuning_sound.mp3",
            "zvok_opis": "Z zamenjavo izpuha dobi Octavia prijetnejsi, globlji diesel ton ki ni prevec hrupen za vsakodnevno voznju."
        },
                "cas_0_100": 9.2,
        "masa": 1350,
        "prtljaznik": 590,
        "slug": "skoda-octavia-a7"
    },

    {
        "id": "vw-golf-7-tdi",
        "znamka": "Volkswagen",
        "model": "Golf VII 2.0 TDI",
        "polno_ime": "Volkswagen Golf VII 2.0 TDI 150 KM",
        "cena": 13000,
        "letnik": "2013-2019",
        "motor": "2.0 TDI diesel (EA288)",
        "gorivo": "diesel",
        "moc": 150,
        "kategorija": "navaden",
        "slika": "golf7.png",
        "slika_tuning": "golf7_tuning.png",
        "opis": "Volkswagen Golf VII je nadgradnja legendarnega Golf VI. Modernejsi dizajn, boljsa notranjost in ucinkovitejsi motor ga delajo za enega najboljsih kompaktov na trgu.",
        "prednosti": [
            "Moderna notranjost",
            "Ucinkovit EA288 TDI motor",
            "Odlicna vrednost pri prodaji",
            "Siroka servisna mreza",
            "Solidna gradnja"
        ],
        "slabosti": [
            "Visja cena kot Golf 6",
            "DSG zahteva vzdrzevanje",
            "Manj karakterja kot starejsi Golfi",
            "Popularnost pomeni visje zavarovanje"
        ],
        "poraba": "4.5-6 L/100km",
        "zakaj": "Golf 7 TDI je priblizno optimalen dnevni avto - zanesljiv, ucinkovit, udoben in dobro vzdrzuje vrednost.",
        "tuning": {
            "stage1_moc": 190,
            "stage1_opis": "EA288 motor dobro reagira na stage 1 remap. Rezultat je 185-195 KM in do 420 Nm - priblizno GTD specifikacija za ceno remapa.",
            "stage1_cena": "200-350 EUR",
            "zvok_stock": "golf7_stock_sound.mp3",
            "zvok_tuning": "golf7_tuning_sound.mp3",
            "zvok_opis": "Golf 7 TDI z izpuhom dobi precej prijetnejsi diesel zvok. Popularna sta Milltek in Remus."
        },
                "cas_0_100": 9.2,
        "masa": 1367,
        "prtljaznik": 380,
        "slug": "vw-golf-7-tdi"
    },

    {
        "id": "mercedes-c220d-w205",
        "znamka": "Mercedes-Benz",
        "model": "C220d W205",
        "polno_ime": "Mercedes-Benz C220d W205",
        "cena": 15000,
        "letnik": "2014-2018",
        "motor": "2.1 diesel OM651",
        "gorivo": "diesel",
        "moc": 170,
        "kategorija": "navaden",
        "slika": "mercc220d.png",
        "slika_tuning": "mercc220d_tuning.png",
        "opis": "Mercedes C220d W205 je eden najboljsih premium sedanov v razredu. Modernejsi dizajn, luksuzna notranjost in ucinkovit diesel motor ga naredijo za odlicno kombinacijo udobja in ekonomicnosti.",
        "prednosti": [
            "Luksuzna W205 notranjost",
            "Ucinkovit diesel (5-6 L/100km)",
            "Odlicna gradnja",
            "Sportski videz",
            "Visoka vrednost pri prodaji"
        ],
        "slabosti": [
            "Vzdrzevanje drago",
            "OM651 znan po nekaterih tezavah",
            "Rezervni deli dragi",
            "Visji zavarovalni razred"
        ],
        "poraba": "5-6.5 L/100km",
        "zakaj": "C220d W205 je za tiste, ki hocejo pravi Mercedes luksuz z razumno porabo goriva. Odlicen avto za dolge razdalje.",
        "tuning": {
            "stage1_moc": 210,
            "stage1_opis": "OM651 diesel motor dobro reagira na remap. Stage 1 prinese 205-215 KM in do 480 Nm navora.",
            "stage1_cena": "250-400 EUR",
            "zvok_stock": "mercc220d_stock_sound.mp3",
            "zvok_tuning": "mercc220d_tuning_sound.mp3",
            "zvok_opis": "Mercedes diesel z sport izpuhom dobi globok, nizkofrekuencen ton ki pristoji premium znamki."
        },
                "cas_0_100": 7.3,
        "masa": 1455,
        "prtljaznik": 480,
        "slug": "mercedes-c220d-w205"
    },

    {
        "id": "bmw-318d-e90",
        "znamka": "BMW",
        "model": "318d E90 LCI",
        "polno_ime": "BMW E90 318d LCI",
        "cena": 6500,
        "letnik": "2008-2011",
        "motor": "2.0 diesel (N47)",
        "gorivo": "diesel",
        "moc": 143,
        "kategorija": "navaden",
        "slika": "bmw318d.png",
        "slika_tuning": "bmw318d_tuning.png",
        "opis": "BMW 318d E90 LCI je vstopni diesel v seriji 3. Kombinacija BMW vozne dinamike, udobne notranjosti in razumne porabe goriva ga naredi za odlicno dnevno vozilo.",
        "prednosti": [
            "BMW vozna dinamika",
            "Nizka poraba diesla",
            "Prostoren sedan",
            "LCI osvezitveni paket",
            "Dobra vrednost za denar"
        ],
        "slabosti": [
            "N47 verizni gonilnik - preglej pred nakupom",
            "Vzdrzevanje visje kot VW/Skoda",
            "143 KM ni dramaticno",
            "Starejsi letnik"
        ],
        "poraba": "5-6.5 L/100km",
        "zakaj": "BMW 318d LCI je odlicen vstop v BMW svet brez prevelikih stroskov. Za ceno Skode Octavie dobiS BMW dinamiko.",
        "tuning": {
            "stage1_moc": 180,
            "stage1_opis": "N47 diesel motor se dobro odziva na remap. Stage 1 prinese 175-185 KM in do 380 Nm. Avto postane precej bolj odziven.",
            "stage1_cena": "200-350 EUR",
            "zvok_stock": "bmw318d_stock_sound.mp3",
            "zvok_tuning": "bmw318d_tuning_sound.mp3",
            "zvok_opis": "Z sport izpuhom dobi BMW diesel precej prijetnejsi, globlji ton. Razlika je obcutna."
        },
                "cas_0_100": 9.5,
        "masa": 1510,
        "prtljaznik": 460,
        "slug": "bmw-318d-e90"
    },

    {
        "id": "audi-a4-b8-tdi",
        "znamka": "Audi",
        "model": "A4 B8 2.0 TDI",
        "polno_ime": "Audi A4 B8 2.0 TDI 143 KM",
        "cena": 9000,
        "letnik": "2008-2012",
        "motor": "2.0 TDI diesel",
        "gorivo": "diesel",
        "moc": 143,
        "kategorija": "navaden",
        "slika": "audia4b8.png",
        "slika_tuning": "audia4b8_tuning.png",
        "opis": "Audi A4 B8 je eleganten in prostorien sedan z odlicno gradnjo in ucinkovitim TDI motorjem. Audi kakovost po dostopni ceni na trgu rabljenih avtomobilov.",
        "prednosti": [
            "Eleganten Audi sedan",
            "Ucinkovit 2.0 TDI",
            "Prostorna notranjost",
            "Solidna Audi gradnja",
            "Dobra vrednost za denar"
        ],
        "slabosti": [
            "Vzdrzevanje drazje kot Skoda/VW",
            "Nekateri B8 imeli tezave z DSG",
            "Rezervni deli drazji",
            "Manj dinamicen kot BMW"
        ],
        "poraba": "5-6.5 L/100km",
        "zakaj": "Audi A4 B8 je odlicna izbira za tiste, ki hocejo Audi eleganco in gradnjo v vecjem sedan formatu.",
        "tuning": {
            "stage1_moc": 185,
            "stage1_opis": "2.0 TDI je eden najboljsih diesel motorjev za tuning. Stage 1 prinese 180-190 KM in do 400 Nm. Poraba se ne poveca, odzivnost pa dramaticno.",
            "stage1_cena": "200-350 EUR",
            "zvok_stock": "audia4_stock_sound.mp3",
            "zvok_tuning": "audia4_tuning_sound.mp3",
            "zvok_opis": "Z Milltek ali sport izpuhom dobi A4 TDI precej prijetnejsi, globlji diesel ton ki dobro pristoji elegantni obliki."
        },
                "cas_0_100": 10.1,
        "masa": 1515,
        "prtljaznik": 480,
        "slug": "audi-a4-b8-tdi"
    },

    {
        "id": "peugeot-308-gti",
        "znamka": "Peugeot",
        "model": "308 GTi 270",
        "polno_ime": "Peugeot 308 GTi 270 KM",
        "cena": 13000,
        "letnik": "2015-2019",
        "motor": "1.6 turbo bencin THP",
        "gorivo": "bencin",
        "moc": 270,
        "kategorija": "navaden",
        "slika": "peugeot308gti.png",
        "slika_tuning": "peugeot308gti_tuning.png",
        "opis": "Peugeot 308 GTi 270 je francoski odgovor na Golf GTI in je v mnogih pogledih boljsi. 270 KM, izjemno ravnanje in unikatni interieur ga delajo za podcenjen zaklad.",
        "prednosti": [
            "270 KM za razumno ceno",
            "Izjemno ravnanje - boljse od GTI",
            "Unikatna Peugeot notranjost",
            "Sportski videz",
            "Redek na cestah"
        ],
        "slabosti": [
            "Peugeot vzdrzevanje ni poceni",
            "Manjsa servisna mreza",
            "Rezervni deli tezje dostopni",
            "Slabsa vrednost pri prodaji"
        ],
        "poraba": "7-10 L/100km",
        "zakaj": "308 GTi 270 je eden najbolj podcenjenih hot-hatchev. Franc si je zasluzil vecjo pozornost - voznja je izjemna.",
        "tuning": {
            "stage1_moc": 320,
            "stage1_opis": "THP 1.6 turbo motor je izjemen za tuning. Stage 1 prinese 315-325 KM in do 450 Nm navora. Absolutno eden najboljsih bang-for-buck remapov.",
            "stage1_cena": "250-400 EUR",
            "zvok_stock": "308gti_stock_sound.mp3",
            "zvok_tuning": "308gti_tuning_sound.mp3",
            "zvok_opis": "Z sport izpuhom dobi THP motor agresiven, sportski ton z znacilnimi turbopoki. Zvok je presenetljivo dober za francoski avto."
        },
                "cas_0_100": 6.0,
        "masa": 1290,
        "prtljaznik": 380,
        "slug": "peugeot-308-gti"
    },

    # =========================================================================
    # DRUZINSKI AVTOMOBILI
    # =========================================================================

    {
        "id": "audi-a4-avant-b7",
        "znamka": "Audi",
        "model": "A4 Avant B7 2.0 TDI",
        "polno_ime": "Audi A4 B7 Avant 2.0 TDI",
        "cena": 5500,
        "letnik": "2005-2008",
        "motor": "2.0 TDI diesel",
        "gorivo": "diesel",
        "moc": 140,
        "kategorija": "druzinski",
        "slika": "audia4avant.png",
        "slika_tuning": "audia4avant_tuning.png",
        "opis": "Audi A4 Avant B7 je elegantni karavan, ki zdruzuje Audi premium kakovost z ogromnim prtljaznikomin zanesljivim TDI motorjem. Idealen za mlade druzine z okusom.",
        "prednosti": [
            "Ogromni prtljaznik (485L)",
            "Premium Audi notranjost",
            "Nizka poraba TDI motorja",
            "Quattro opcija za zimo",
            "Eleganten karavan dizajn"
        ],
        "slabosti": [
            "Starejsi letnik (2005-2008)",
            "Stroski vzdrzevanja visji",
            "Rezervni deli drazji",
            "Nekateri B7 imeli tezave z DSG"
        ],
        "poraba": "5.5-7 L/100km",
        "zakaj": "Audi A4 Avant B7 je pravi odgovor za tiste, ki hocejo karavan z razredom. Premium kakovost brez preplac.",
        "tuning": {
            "stage1_moc": 175,
            "stage1_opis": "2.0 TDI v B7 Avantu dobro reagira na remap. Stage 1 prinese 170-180 KM in do 380 Nm. Idealno za avtocestno voznju z druzino.",
            "stage1_cena": "200-350 EUR",
            "zvok_stock": "audia4avant_stock_sound.mp3",
            "zvok_tuning": "audia4avant_tuning_sound.mp3",
            "zvok_opis": "Z sport izpuhom dobi A4 Avant TDI globlji, prijetnejsi zvok ki je precej boljsi od originalnega diesel turna."
        },
                "cas_0_100": 10.5,
        "masa": 1585,
        "prtljaznik": 485,
        "slug": "audi-a4-avant-b7"
    },

    {
        "id": "bmw-touring-e91",
        "znamka": "BMW",
        "model": "320d Touring E91",
        "polno_ime": "BMW E91 320d Touring",
        "cena": 7000,
        "letnik": "2006-2012",
        "motor": "2.0 diesel (N47)",
        "gorivo": "diesel",
        "moc": 163,
        "kategorija": "druzinski",
        "slika": "bmwtouring.png",
        "slika_tuning": "bmwtouring_tuning.png",
        "opis": "BMW 320d Touring E91 je premium karavan, ki zdruzuje BMW vozno dinamiko z ogromnim prtljaznikomin. Idealen za aktivne druzine, ki ne zelijo zrtvovati voznih lastnosti.",
        "prednosti": [
            "BMW vozna dinamika v karavanu",
            "Velik prtljaznik (495L)",
            "Nizka poraba diesla",
            "Premium BMW notranjost",
            "Zanesljiv pri rednem vzdrzevanju"
        ],
        "slabosti": [
            "N47 verizni gonilnik zahteva pozornost",
            "Visji stroski vzdrzevanja",
            "Rezervni deli drazji",
            "Starejsi modeli zahtevajo pregled"
        ],
        "poraba": "5.5-7 L/100km",
        "zakaj": "BMW 320d Touring E91 je karavan za tiste, ki ne marajo kompromisov. Prostoren, dinamicen in premium - vse v enem paketu.",
        "tuning": {
            "stage1_moc": 200,
            "stage1_opis": "N47 diesel motor se dobro odziva na remap. Stage 1 prinese 195-205 KM in do 420 Nm. Za touring je to idealno - moc za prehitevanje na avtocesti brez vecje porabe.",
            "stage1_cena": "200-350 EUR",
            "zvok_stock": "bmwtouring_stock_sound.mp3",
            "zvok_tuning": "bmwtouring_tuning_sound.mp3",
            "zvok_opis": "BMW diesel touring z sport izpuhom dobi precej globlji, karakternejsi zvok. Razlika je opazna in prijetna."
        },
                "cas_0_100": 8.1,
        "masa": 1590,
        "prtljaznik": 495,
        "slug": "bmw-touring-e91"
    },

    {
        "id": "vw-passat-b7-variant",
        "znamka": "Volkswagen",
        "model": "Passat B7 Variant 2.0 TDI",
        "polno_ime": "Volkswagen Passat B7 Variant 2.0 TDI",
        "cena": 9000,
        "letnik": "2011-2014",
        "motor": "2.0 TDI diesel",
        "gorivo": "diesel",
        "moc": 140,
        "kategorija": "druzinski",
        "slika": "passatb7.png",
        "slika_tuning": "passatb7_tuning.png",
        "opis": "VW Passat B7 Variant je zanesljivi karavan, ki ponuja ogromno prostora in nizke stroske vzdrzevanja. Solidna nemska gradnja ga naredi za idealnega druzinskega spremljevalca.",
        "prednosti": [
            "Ogromno prostora (603L prtljaznik)",
            "Zanesljiv TDI motor",
            "Nizji stroski kot BMW/Audi",
            "Dobra servisna mreza",
            "Odlicna vrednost za denar"
        ],
        "slabosti": [
            "Dizajn bolj konservativen",
            "Notranjost manj premium kot BMW/Audi",
            "Manj dinamicen",
            "Premori kazejo starost"
        ],
        "poraba": "5-6.5 L/100km",
        "zakaj": "Passat B7 Variant je prakticen, zanesljiv in prostoren - idealen za tiste, ki cenijo funkcionalnost.",
        "tuning": {
            "stage1_moc": 180,
            "stage1_opis": "2.0 TDI v Passatu odlicno reagira na remap. Stage 1 prinese 175-185 KM in do 400 Nm. Idealno za druzinsko voznju.",
            "stage1_cena": "200-350 EUR",
            "zvok_stock": "passatb7_stock_sound.mp3",
            "zvok_tuning": "passatb7_tuning_sound.mp3",
            "zvok_opis": "Passat z sport izpuhom dobi prijetnejsi diesel ton brez prevelikih sprememb - primerno za druzinski karavan."
        },
                "cas_0_100": 10.8,
        "masa": 1579,
        "prtljaznik": 603,
        "slug": "vw-passat-b7-variant"
    },

    {
        "id": "volvo-v60-d3",
        "znamka": "Volvo",
        "model": "V60 D3",
        "polno_ime": "Volvo V60 D3 2.0 Diesel",
        "cena": 10000,
        "letnik": "2011-2015",
        "motor": "2.0 diesel D3",
        "gorivo": "diesel",
        "moc": 150,
        "kategorija": "druzinski",
        "slika": "volvov60.png",
        "slika_tuning": "volvov60_tuning.png",
        "opis": "Volvo V60 D3 je elegantni skandinavski karavan z izjemno varnostjo in komfortom. Minimalisticna Volvo notranjost in solidni diesel motor ga naredijo za odlicen druzinski avto.",
        "prednosti": [
            "Skandinavska eleganca",
            "Vrhunska varnost",
            "Udobna notranjost",
            "Solidni diesel motor",
            "Edinstven videz"
        ],
        "slabosti": [
            "Manjsi prtljaznik kot konkurenca",
            "Elektronika zahteva servis",
            "Rezervni deli drazji",
            "Manj sportski kot BMW/Audi"
        ],
        "poraba": "5.5-7 L/100km",
        "zakaj": "Volvo V60 je za tiste, ki cenijo varen, eleganten in udoben karavan s skandinavskim dizajnom.",
        "tuning": {
            "stage1_moc": 190,
            "stage1_opis": "D3 diesel motor dobro reagira na remap. Stage 1 prinese 185-195 KM in do 430 Nm. Avto postane bistveno bolj odziven.",
            "stage1_cena": "220-380 EUR",
            "zvok_stock": "volvov60_stock_sound.mp3",
            "zvok_tuning": "volvov60_tuning_sound.mp3",
            "zvok_opis": "Z sport izpuhom dobi Volvo diesel karakternejsi zvok, ki ga ne bi pricel za skandinavski avto."
        },
                "cas_0_100": 9.5,
        "masa": 1680,
        "prtljaznik": 430,
        "slug": "volvo-v60-d3"
    },

    {
        "id": "skoda-superb-combi",
        "znamka": "Skoda",
        "model": "Superb II Combi 2.0 TDI",
        "polno_ime": "Skoda Superb II Combi 2.0 TDI 170 KM",
        "cena": 8000,
        "letnik": "2009-2013",
        "motor": "2.0 TDI diesel",
        "gorivo": "diesel",
        "moc": 170,
        "kategorija": "druzinski",
        "slika": "superbcombi.png",
        "slika_tuning": "superbcombi_tuning.png",
        "opis": "Skoda Superb II Combi je avto za tiste, ki cenijo prostor nad vsem. Z ogromno notranjostjo in zanesljivim TDI motorjem je eden najboljsih karavan nakupov za denar.",
        "prednosti": [
            "Eden najvecjih prtljaznikov (633L)",
            "Ogromno prostora za potnike",
            "Zanesljiv in nizkih stroskov",
            "Dobro opremljen za ceno",
            "Izjemna vrednost"
        ],
        "slabosti": [
            "Velik in tezko za parkiranje",
            "Manj prestizna znamka",
            "Notranjost manj luksuzna",
            "Dizajn konservativen"
        ],
        "poraba": "5.5-7 L/100km",
        "zakaj": "Superb Combi odgovori na vprasanje: koliko avtomobila dobim za denar? Ogromno prostora, zanesljivost in nizki stroski.",
        "tuning": {
            "stage1_moc": 210,
            "stage1_opis": "2.0 TDI 170 KM v Superbu se dobro odziva na remap. Stage 1 prinese 205-215 KM in do 440 Nm. Idealno za avtocestno voznju s polno druzino.",
            "stage1_cena": "200-350 EUR",
            "zvok_stock": "superb_stock_sound.mp3",
            "zvok_tuning": "superb_tuning_sound.mp3",
            "zvok_opis": "Z sport izpuhom dobi Superb Combi prijetnejsi diesel ton ki ne moti potnikov zadaj."
        },
                "cas_0_100": 8.5,
        "masa": 1600,
        "prtljaznik": 633,
        "slug": "skoda-superb-combi"
    },

    {
        "id": "audi-a6-avant-c6",
        "znamka": "Audi",
        "model": "A6 Avant C6 3.0 TDI",
        "polno_ime": "Audi A6 C6 Avant 3.0 TDI Quattro",
        "cena": 9500,
        "letnik": "2005-2011",
        "motor": "3.0 V6 TDI diesel",
        "gorivo": "diesel",
        "moc": 225,
        "kategorija": "druzinski",
        "slika": "audia6avant.png",
        "slika_tuning": "audia6avant_tuning.png",
        "opis": "Audi A6 Avant C6 z 3.0 V6 TDI in Quattro pogonom je ena redkih prave luksuznih karavan po dostopni ceni. 225 KM V6 diesla, ogromno prostora in Quattro.",
        "prednosti": [
            "225 KM V6 diesel - odlicen za dolge razdalje",
            "Quattro 4x4 pogon",
            "Ogromno prostora",
            "Luksuzna Audi notranjost",
            "Odlicna gradnja"
        ],
        "slabosti": [
            "V6 diesel drag za vzdrzevanje",
            "Rezervni deli dragi",
            "Starejsi letnik",
            "Visji stroski servisa"
        ],
        "poraba": "7-9 L/100km",
        "zakaj": "A6 Avant C6 3.0 TDI je luksuzni karavan po ceni navadnega. Za druzino, ki hoce vse - prostor, luksuz in zmogljivost.",
        "tuning": {
            "stage1_moc": 270,
            "stage1_opis": "3.0 V6 TDI je odlicen za remap. Stage 1 prinese 265-275 KM in do 600 Nm navora. Avto postane resno hiter.",
            "stage1_cena": "250-400 EUR",
            "zvok_stock": "audia6_stock_sound.mp3",
            "zvok_tuning": "audia6_tuning_sound.mp3",
            "zvok_opis": "V6 diesel z sport izpuhom ima globok, karakteren zvok ki je povsem drugacen od 4-valjnih dieslov."
        },
                "cas_0_100": 6.7,
        "masa": 1810,
        "prtljaznik": 565,
        "slug": "audi-a6-avant-c6"
    },

    {
        "id": "bmw-520d-f11",
        "znamka": "BMW",
        "model": "520d Touring F11",
        "polno_ime": "BMW F11 520d Touring",
        "cena": 13500,
        "letnik": "2010-2016",
        "motor": "2.0 diesel N47/B47",
        "gorivo": "diesel",
        "moc": 184,
        "kategorija": "druzinski",
        "slika": "bmw520dtouring.png",
        "slika_tuning": "bmw520dtouring_tuning.png",
        "opis": "BMW 520d Touring F11 je serija 5 v karavan obliki. Vec luksuza, vec prostora in ohranjena vozna dinamika BMW-ja. Eden najprestiznejsih karavan po dostopni ceni.",
        "prednosti": [
            "Serija 5 luksuz v karavanu",
            "184 KM ucinkovit diesel",
            "Velik prostoren prtljaznik",
            "Odlicna gradnja in materiali",
            "BMW vozna dinamika"
        ],
        "slabosti": [
            "Vzdrzevanje drago",
            "Servis drag",
            "Rezervni deli dragi",
            "Zavarovanje visje"
        ],
        "poraba": "5.5-7 L/100km",
        "zakaj": "520d Touring F11 je ultimativni druzinski BMW. Vec prostora kot E91, bolj luksuzna notranjost in enaka dinamika.",
        "tuning": {
            "stage1_moc": 225,
            "stage1_opis": "B47/N47 diesel v 520d se dobro odziva na remap. Stage 1 prinese 220-230 KM in do 480 Nm. Touring postane resno zmogljiv.",
            "stage1_cena": "250-400 EUR",
            "zvok_stock": "bmw520d_stock_sound.mp3",
            "zvok_tuning": "bmw520d_tuning_sound.mp3",
            "zvok_opis": "BMW serija 5 diesel z sport izpuhom dobi precej globlji, bolj karakteren zvok ki pristoji luksuzni znamki."
        },
                "cas_0_100": 7.4,
        "masa": 1770,
        "prtljaznik": 560,
        "slug": "bmw-520d-f11"
    },

    {
        "id": "mercedes-e220d-w212",
        "znamka": "Mercedes-Benz",
        "model": "E220d Estate W212",
        "polno_ime": "Mercedes-Benz E220d Estate W212",
        "cena": 11500,
        "letnik": "2009-2016",
        "motor": "2.1 diesel OM651",
        "gorivo": "diesel",
        "moc": 170,
        "kategorija": "druzinski",
        "slika": "merce220estate.png",
        "slika_tuning": "merce220estate_tuning.png",
        "opis": "Mercedes E220d Estate W212 je luksuzni karavan za tiste, ki hocejo Mercedes zvezdico v druzinskem avtu. Prostorna notranjost, solidna gradnja in ucinkovit diesel ga naredijo za odlicno dolgorocno nalatbo.",
        "prednosti": [
            "Mercedes luksuz v karavanu",
            "Prostoren prtljaznik",
            "Ucinkovit diesel (5.5-7L)",
            "Solidna gradnja",
            "Odlicno udobje za potovanje"
        ],
        "slabosti": [
            "OM651 znan po nekaterih tezavah",
            "Vzdrzevanje drago",
            "Rezervni deli dragi",
            "Starejsi letniki kazejo leta"
        ],
        "poraba": "5.5-7 L/100km",
        "zakaj": "E220d Estate je za tiste, ki hocejo Mercedes udobje in prostor za druzino brez preplac.",
        "tuning": {
            "stage1_moc": 210,
            "stage1_opis": "OM651 diesel motor dobro reagira na remap. Stage 1 prinese 205-215 KM in do 470 Nm navora.",
            "stage1_cena": "250-400 EUR",
            "zvok_stock": "merce220_stock_sound.mp3",
            "zvok_tuning": "merce220_tuning_sound.mp3",
            "zvok_opis": "Mercedes diesel estate z sport izpuhom dobi globok, prizemljen zvok ki je prezentabilen in sportski hkrati."
        },
                "cas_0_100": 8.2,
        "masa": 1770,
        "prtljaznik": 695,
        "slug": "mercedes-e220d-w212"
    },

    {
        "id": "skoda-octavia-combi-rs",
        "znamka": "Skoda",
        "model": "Octavia III RS Combi",
        "polno_ime": "Skoda Octavia III RS Combi 2.0 TDI",
        "cena": 14500,
        "letnik": "2013-2017",
        "motor": "2.0 TDI diesel 184 KM",
        "gorivo": "diesel",
        "moc": 184,
        "kategorija": "druzinski",
        "slika": "octaviars.png",
        "slika_tuning": "octaviars_tuning.png",
        "opis": "Skoda Octavia RS Combi je sportski druzinski karavan, ki zdruzuje 184 KM TDI motor z ogromnim prtljaznikomom. Pravo razmerje med zabavo in prakticnostjo.",
        "prednosti": [
            "184 KM diesel v karavanu",
            "Ogromno prostora (610L)",
            "Sportski RS videz",
            "Zanesljiv in pocen za vzdrzevanje",
            "Odlicna vrednost"
        ],
        "slabosti": [
            "Manj prestizna znamka",
            "Notranjost manj luksuzna kot BMW/Audi",
            "Dizajn nevtralen",
            "Pogoste na cestah"
        ],
        "poraba": "5-6.5 L/100km",
        "zakaj": "Octavia RS Combi je perfektna za druzine, ki hocejo zmogljiv karavan brez premium stroskev. Odlicno razmerje.",
        "tuning": {
            "stage1_moc": 225,
            "stage1_opis": "2.0 TDI 184 KM je odlicen za tuning. Stage 1 prinese 220-230 KM in do 460 Nm. RS Combi postane resno hiter karavan.",
            "stage1_cena": "200-350 EUR",
            "zvok_stock": "octaviars_stock_sound.mp3",
            "zvok_tuning": "octaviars_tuning_sound.mp3",
            "zvok_opis": "Octavia RS z Milltek izpuhom dobi sportski diesel ton ki ustreza RS znacaju avta."
        },
                "cas_0_100": 7.5,
        "masa": 1490,
        "prtljaznik": 610,
        "slug": "skoda-octavia-combi-rs"
    },

    {
        "id": "ford-mondeo-mk4-estate",
        "znamka": "Ford",
        "model": "Mondeo Mk4 Estate 2.0 TDCi",
        "polno_ime": "Ford Mondeo Mk4 Estate 2.0 TDCi 140 KM",
        "cena": 5500,
        "letnik": "2007-2014",
        "motor": "2.0 TDCi diesel",
        "gorivo": "diesel",
        "moc": 140,
        "kategorija": "druzinski",
        "slika": "mondeo.png",
        "slika_tuning": "mondeo_tuning.png",
        "opis": "Ford Mondeo Mk4 Estate je prostoren in udoben druzinski karavan po izjemno dostopni ceni. Ford je v Mondeou dal vec prostora kot pri BMW ali Mercedes za tretjino cene.",
        "prednosti": [
            "Izjemna vrednost za denar",
            "Ogromno prostora",
            "Udobna voznja",
            "Ford TDCi motor zanesljiv",
            "Najcenejsi luksuz v segmentu"
        ],
        "slabosti": [
            "Manj prestizna znamka",
            "Slabse vrednotenje pri prodaji",
            "Ford servis manj razsirien",
            "Dizajn konservativen"
        ],
        "poraba": "5.5-7 L/100km",
        "zakaj": "Mondeo Estate je avto za pametne kupce. Enako prostoren kot BMW 5 Touring ali Mercedes E, za trikrat manjso ceno.",
        "tuning": {
            "stage1_moc": 175,
            "stage1_opis": "Ford 2.0 TDCi motor se dobro odziva na remap. Stage 1 prinese 170-180 KM in do 380 Nm. Za druzinski karavan je to idealno.",
            "stage1_cena": "180-300 EUR",
            "zvok_stock": "mondeo_stock_sound.mp3",
            "zvok_tuning": "mondeo_tuning_sound.mp3",
            "zvok_opis": "Z zamenjavo izpuha dobi Mondeo prijetnejsi diesel ton. Ford ima dober zvok pri visokih vrtljajih."
        },
                "cas_0_100": 10.2,
        "masa": 1600,
        "prtljaznik": 537,
        "slug": "ford-mondeo-mk4-estate"
    },

    {
        "id": "volvo-v70-d5",
        "znamka": "Volvo",
        "model": "V70 III D5",
        "polno_ime": "Volvo V70 III 2.4 D5 AWD",
        "cena": 7000,
        "letnik": "2007-2013",
        "motor": "2.4 D5 5-valjni diesel",
        "gorivo": "diesel",
        "moc": 185,
        "kategorija": "druzinski",
        "slika": "volvov70.png",
        "slika_tuning": "volvov70_tuning.png",
        "opis": "Volvo V70 III D5 AWD je skandinavski luksuzni karavan z edinstvenim 5-valjnim dieselskim motorjem in AWD pogonom. Prostoren, varen in udoben - idealen za druzine z aktivnim slogom zivljenja.",
        "prednosti": [
            "5-valjni diesel - edinstven zvok",
            "AWD pogon za zimo",
            "Ogromno prostora",
            "Vrhunska Volvo varnost",
            "Unikatni skandinavski karakter"
        ],
        "slabosti": [
            "Vzdrzevanje drazje",
            "Poraba AWD sistema",
            "Rezervni deli tezje dostopni",
            "Elektronika zahteva pozornost"
        ],
        "poraba": "7-9 L/100km",
        "zakaj": "V70 D5 AWD je za tiste, ki cenijo unikatnost in skandinavski karakter. 5-valjni motor, AWD in Volvo prostor - edinstvena kombinacija.",
        "tuning": {
            "stage1_moc": 230,
            "stage1_opis": "D5 5-valjni diesel odlicno reagira na remap. Stage 1 prinese 225-235 KM in do 500 Nm. AWD pa ta moc izvrstno prenese na cesto.",
            "stage1_cena": "220-380 EUR",
            "zvok_stock": "volvov70_stock_sound.mp3",
            "zvok_tuning": "volvov70_tuning_sound.mp3",
            "zvok_opis": "5-valjni motor ima edinstven zvok ze v originalu - globok burble z znacilnim ritmom. Z izpuhom se ta karakter se bolj izrazi."
        },
                "cas_0_100": 7.9,
        "masa": 1840,
        "prtljaznik": 575,
        "slug": "volvo-v70-d5"
    },


    # =========================================================================
    # CENEJŠI AVTOMOBILI (pod 6.000 €)
    # =========================================================================

    {
        "id": "renault-megane-2-rs",
        "znamka": "Renault",
        "model": "Mégane II RS",
        "polno_ime": "Renault Mégane II RS 2.0 turbo",
        "cena": 4200,
        "letnik": "2004-2009",
        "motor": "2.0 turbo bencin F4Rt",
        "gorivo": "bencin",
        "moc": 225,
        "kategorija": "sporten",
        "slika": "meganers2.png",
        "slika_tuning": "meganers2_tuning.png",
        "opis": "Renault Mégane II RS je francoski hot-hatch klasik z 225 KM, ki velja za enega najboljših voznikov svojega časa. Izjemno ravnanje, odlična prednjeosna dinamika in unikaten Renault karakter.",
        "prednosti": [
            "225 KM za zelo majhno ceno",
            "Legendarno ravnanje",
            "Kultni status med ljubitelji",
            "Lahek in agilen",
            "Dober zvok 2.0 turbo"
        ],
        "slabosti": [
            "Starejši letnik (2004-2009)",
            "Vzdrževano dražje kot Golf",
            "Rezervni deli težje dostopni",
            "Mehanske napake pri slabo vzdrževanih"
        ],
        "poraba": "8-11 L/100km",
        "zakaj": "Mégane II RS je legendaren hot-hatch po dostopni ceni. Za tiste, ki hočejo pravo vozno izkušnjo brez velikih stroškov.",
        "tuning": {
            "stage1_moc": 270,
            "stage1_opis": "F4Rt motor odlično reagira na remap. Stage 1 prinese 265-275 KM in do 380 Nm navora. Sprememba je mocno občutna.",
            "stage1_cena": "220-380 EUR",
            "zvok_stock": "meganers2_stock_sound.mp3",
            "zvok_tuning": "meganers2_tuning_sound.mp3",
            "zvok_opis": "Z izpuhom (npr. Akrapovič ali Milltek) dobi Mégane RS agresiven, glasen ton ki ustreza njegovemu karakterju."
        },
                "cas_0_100": 6.5,
        "masa": 1290,
        "prtljaznik": 330,
        "slug": "renault-megane-2-rs"
    },

    {
        "id": "renault-megane-3-rs",
        "znamka": "Renault",
        "model": "Mégane III RS",
        "polno_ime": "Renault Mégane III RS 2.0 turbo 265 KM",
        "cena": 8000,
        "letnik": "2010-2015",
        "motor": "2.0 turbo bencin (M4R)",
        "gorivo": "bencin",
        "moc": 265,
        "kategorija": "sporten",
        "slika": "meganers3.png",
        "slika_tuning": "meganers3_tuning.png",
        "opis": "Renault Mégane III RS je naslednik legendarne RS tradicije z 265 KM, diferencialom Torsen in edinstvenim podvozjem. Večkrat zmagal na Nürburgringu v svojem razredu.",
        "prednosti": [
            "265 KM z diferencialom Torsen",
            "Rekord Nürburgringa v razredu",
            "Odlično ravnanje in podvozje",
            "Sportski videz",
            "Edinstven francoski karakter"
        ],
        "slabosti": [
            "Trdo vzmetenje za vsak dan",
            "Vzdrževano dražje",
            "Rezervni deli težje dostopni",
            "Manjša prepoznavnost znamke"
        ],
        "poraba": "8-11 L/100km",
        "zakaj": "Mégane III RS je eden najboljših hot-hatchev kar je bilo narejenih. Za tiste, ki resnično cenijo vozno dinamiko.",
        "tuning": {
            "stage1_moc": 310,
            "stage1_opis": "M4R 2.0 turbo se odlično odziva na remap. Stage 1 prinese 305-315 KM in do 420 Nm navora.",
            "stage1_cena": "250-400 EUR",
            "zvok_stock": "meganers3_stock_sound.mp3",
            "zvok_tuning": "meganers3_tuning_sound.mp3",
            "zvok_opis": "Z Akrapovičem ali Milltek izpuhom dobi Mégane RS agresiven, sportski zvok z znacilnimi turbopoki."
        },
                "cas_0_100": 6.0,
        "masa": 1370,
        "prtljaznik": 340,
        "slug": "renault-megane-3-rs"
    },

    {
        "id": "toyota-yaris-ts",
        "znamka": "Toyota",
        "model": "Yaris 1.3 VVT-i",
        "polno_ime": "Toyota Yaris II 1.3 VVT-i",
        "cena": 3800,
        "letnik": "2005-2011",
        "motor": "1.3 bencin VVT-i",
        "gorivo": "bencin",
        "moc": 87,
        "kategorija": "navaden",
        "slika": "yaris.png",
        "slika_tuning": "yaris_tuning.png",
        "opis": "Toyota Yaris II je eden najzanesljivejših malih avtomobilov na trgu. Japonska kakovost, nizki vzdrževalni stroški in enostavnost ga naredijo za idealen prvi avto ali mestno vozilo.",
        "prednosti": [
            "Izjemna zanesljivost Toyota",
            "Najnižji stroški vzdrževanja",
            "Nizka poraba goriva",
            "Idealen za mesto",
            "Poceni zavarovanje"
        ],
        "slabosti": [
            "87 KM ni vznemirljivo",
            "Brez posebnega karakterja",
            "Majhen prtljažnik",
            "Slabša vožnja na avtocesti"
        ],
        "poraba": "5-7 L/100km",
        "zakaj": "Toyota Yaris je idealen avto za tiste, ki hočejo zanesljiv in poceni transport brez presenečenj. Japonska kvaliteta za majhen denar.",
        "tuning": {
            "stage1_moc": 100,
            "stage1_opis": "1.3 VVT-i motor ima omejen tuning potencial. Stage 1 (intake + izpuh + remap) prinese priblizno 98-105 KM. Ni dramatično, ampak odzivnost se izboljša.",
            "stage1_cena": "150-250 EUR",
            "zvok_stock": "yaris_stock_sound.mp3",
            "zvok_tuning": "yaris_tuning_sound.mp3",
            "zvok_opis": "Z zamenjavo izpuha dobi Yaris bolj sportski ton - presenetljivo prijetna sprememba za majhen avto."
        },
                "cas_0_100": 13.4,
        "masa": 1015,
        "prtljaznik": 286,
        "slug": "toyota-yaris-ts"
    },

    {
        "id": "fiat-punto-evo",
        "znamka": "Fiat",
        "model": "Punto Evo 1.4",
        "polno_ime": "Fiat Punto Evo 1.4 MultiAir",
        "cena": 3000,
        "letnik": "2009-2012",
        "motor": "1.4 turbo bencin MultiAir",
        "gorivo": "bencin",
        "moc": 105,
        "kategorija": "navaden",
        "slika": "puntoevo.png",
        "slika_tuning": "puntoevo_tuning.png",
        "opis": "Fiat Punto Evo je eleganten in stilsko zanimiv mali avto po izjemno dostopni ceni. Italijanski dizajn in 105 KM MultiAir motorja ga naredita za zabavno mestno vozilo.",
        "prednosti": [
            "Nizka nakupna cena",
            "Italijanski dizajn",
            "105 KM - dovolj za mestno vožnjo",
            "Lahek in odziven",
            "Nizka poraba"
        ],
        "slabosti": [
            "Fiat zanesljivost vprašljiva",
            "Vzdrževano dražje kot Toyota",
            "Rezervni deli včasih težko dostopni",
            "Elektronske napake na starejših"
        ],
        "poraba": "5.5-7.5 L/100km",
        "zakaj": "Punto Evo je za tiste, ki hočejo stil in zabavo za minimalen denar. Idealen prvi avto z italijanskim karakterjem.",
        "tuning": {
            "stage1_moc": 135,
            "stage1_opis": "1.4 MultiAir turbo motor se dobro odziva na remap. Stage 1 prinese 130-140 KM in boljšo odzivnost po celotnem obratnem območju.",
            "stage1_cena": "180-300 EUR",
            "zvok_stock": "punto_stock_sound.mp3",
            "zvok_tuning": "punto_tuning_sound.mp3",
            "zvok_opis": "Z zamenjavo izpuha dobi Punto živahen, sportski ton ki dobro pristoji njegovemu stilu."
        },
                "cas_0_100": 10.2,
        "masa": 1110,
        "prtljaznik": 275,
        "slug": "fiat-punto-evo"
    },

    {
        "id": "opel-astra-h-1-6",
        "znamka": "Opel",
        "model": "Astra H 1.6 Twinport",
        "polno_ime": "Opel Astra H 1.6 Twinport",
        "cena": 3200,
        "letnik": "2004-2010",
        "motor": "1.6 bencin Twinport",
        "gorivo": "bencin",
        "moc": 115,
        "kategorija": "navaden",
        "slika": "astrah.png",
        "slika_tuning": "astrah_tuning.png",
        "opis": "Opel Astra H je soliden in zanesljiv kompaktni avto po zelo dostopni ceni. Prostornejši od konkurence v razredu in dobro vzdrževan v Evropi.",
        "prednosti": [
            "Cenovno dostopen",
            "Prostoren za razred",
            "Zanesljiv motor",
            "Poceni vzdrževano",
            "Dobra vidljivost"
        ],
        "slabosti": [
            "Dizajn nevtralen",
            "Notranjost plastična",
            "Malo manj zabaven za vožnjo",
            "Slabša vrednost pri prodaji"
        ],
        "poraba": "6-8 L/100km",
        "zakaj": "Astra H je praktičen, zanesljiv avto za minimalen denar. Dober za tiste, ki hočejo le zanesljiv transport.",
        "tuning": {
            "stage1_moc": 145,
            "stage1_opis": "1.6 Twinport motor se odziva na remap in stage 1 prinese priblizno 140-148 KM in boljšo odzivnost.",
            "stage1_cena": "180-280 EUR",
            "zvok_stock": "astrah_stock_sound.mp3",
            "zvok_tuning": "astrah_tuning_sound.mp3",
            "zvok_opis": "Z sport izpuhom dobi Astra H prijetnejši, sportski ton."
        },
                "cas_0_100": 10.5,
        "masa": 1265,
        "prtljaznik": 330,
        "slug": "opel-astra-h-1-6"
    },

    {
        "id": "honda-jazz-ii",
        "znamka": "Honda",
        "model": "Jazz II 1.4",
        "polno_ime": "Honda Jazz II 1.4 i-DSi",
        "cena": 4200,
        "letnik": "2008-2013",
        "motor": "1.4 bencin i-DSi",
        "gorivo": "bencin",
        "moc": 100,
        "kategorija": "navaden",
        "slika": "hondajazz.png",
        "slika_tuning": "hondajazz_tuning.png",
        "opis": "Honda Jazz II je eden najpametnejših malih avtomobilov na trgu. Edinstvena notranjost s sklopljivimi sedeži daje neverjeten prostor v kompaktnem telesu. Japonska zanesljivost zagotovljena.",
        "prednosti": [
            "Izjemno pametna notranjost",
            "Japonska zanesljivost Honda",
            "Nizki stroški vzdrževanja",
            "Presenetljivo prostoren",
            "Nizka poraba"
        ],
        "slabosti": [
            "100 KM ni vznemirljivo",
            "Dizajn ni za vsakogar",
            "Brez sportskega karakterja",
            "Cena malo višja od Fiata/Opla"
        ],
        "poraba": "5-6.5 L/100km",
        "zakaj": "Honda Jazz je idealen avto za tiste, ki cenijo pametno zasnovo in zanesljivost. Za ves denar dobite največ prostora.",
        "tuning": {
            "stage1_moc": 115,
            "stage1_opis": "1.4 i-DSi motor je atmosferski in ima omejen tuning potencial. S intake in izpuhom priblizno 110-115 KM.",
            "stage1_cena": "150-250 EUR",
            "zvok_stock": "jazz_stock_sound.mp3",
            "zvok_tuning": "jazz_tuning_sound.mp3",
            "zvok_opis": "Z sport izpuhom dobi Jazz Honda prijetnejši VTEC ton - presenetljivo dober zvok za mali avto."
        },
                "cas_0_100": 12.5,
        "masa": 980,
        "prtljaznik": 355,
        "slug": "honda-jazz-ii"
    },

    {
        "id": "vw-polo-9n3",
        "znamka": "Volkswagen",
        "model": "Polo 9N3 1.4 TDI",
        "polno_ime": "Volkswagen Polo 9N3 1.4 TDI",
        "cena": 3000,
        "letnik": "2005-2009",
        "motor": "1.4 TDI diesel",
        "gorivo": "diesel",
        "moc": 80,
        "kategorija": "navaden",
        "slika": "vwpolo.png",
        "slika_tuning": "vwpolo_tuning.png",
        "opis": "Volkswagen Polo 9N3 1.4 TDI je eden najupornejših malih avtomobilov. Izjemna poraba goriva (do 4 L/100km), VW zanesljivost in nizki stroški ga naredijo za idealen vsakodnevni avto.",
        "prednosti": [
            "Izjemno nizka poraba (3.5-5 L/100km)",
            "VW zanesljivost",
            "Nizki vzdrževalni stroški",
            "Poceni gorivo diesel",
            "Dobra vrednost pri prodaji"
        ],
        "slabosti": [
            "80 KM - počasen",
            "Majhen in neugoden na avtocesti",
            "Majhen prtljažnik",
            "Brez kakšnega karakterja"
        ],
        "poraba": "3.5-5 L/100km",
        "zakaj": "Polo TDI je ultimativni ekonomičen avto. Nihče drug ne ponuja take porabe po tej ceni. Idealen za mestno vožnjo.",
        "tuning": {
            "stage1_moc": 105,
            "stage1_opis": "1.4 TDI se dobro odziva na remap. Stage 1 prinese 100-108 KM in do 230 Nm. Avto postane bistveno bolj odziven za vsakdanjo vožnjo.",
            "stage1_cena": "160-280 EUR",
            "zvok_stock": "polo_stock_sound.mp3",
            "zvok_tuning": "polo_tuning_sound.mp3",
            "zvok_opis": "Z zamenjavo izpuha dobi Polo TDI globlji diesel ton ki je precej prijetnejši od originalnega."
        },
                "cas_0_100": 15.0,
        "masa": 1138,
        "prtljaznik": 270,
        "slug": "vw-polo-9n3"
    },

    # =========================================================================
    # DRAŽJI AVTOMOBILI (nad 30.000 €)
    # =========================================================================

    {
        "id": "chevrolet-corvette-c8",
        "znamka": "Chevrolet",
        "model": "Corvette C8 Stingray",
        "polno_ime": "Chevrolet Corvette C8 Stingray 6.2 V8",
        "cena": 72000,
        "letnik": "2020-danes",
        "motor": "6.2 V8 atmosferski bencin LT2",
        "gorivo": "bencin",
        "moc": 502,
        "kategorija": "sporten",
        "slika": "corvettec8.png",
        "slika_tuning": "corvettec8_tuning.png",
        "opis": "Chevrolet Corvette C8 je revolucionarni mid-engine američki supercar. Z 502 KM V8 motorjem, postavljenim za kabino, in cenovno dostopnostjo v primerjavi z evropsko konkurenco je C8 eden najboljših vrednosti v svetu supercars.",
        "prednosti": [
            "502 KM V8 za ceno kot Porsche 911 baza",
            "Mid-engine layout - supercar dinamika",
            "Brutalen V8 zvok",
            "Odlično razmerje cena/zmogljivost",
            "Ekskluziven videz"
        ],
        "slabosti": [
            "Visoki servisni stroški v EU",
            "Rezervni deli iz Amerike",
            "Leva stran volana (večina uvoza)",
            "Visoka poraba (13-16 L/100km)"
        ],
        "poraba": "13-16 L/100km",
        "zakaj": "C8 Corvette je eden redkih priložnosti, kjer dobite pravi supercar izkušnjo brez supercar cene. 502 KM V8, mid-engine in 0-100 v 2.9 sekunde.",
        "tuning": {
            "stage1_moc": 560,
            "stage1_opis": "LT2 V8 odlično reagira na remap in E85 gorivo. Stage 1 prinese 555-565 KM in bistveno boljšo odzivnost po vsem obratnem območju.",
            "stage1_cena": "500-900 EUR",
            "zvok_stock": "corvettec8_stock_sound.mp3",
            "zvok_tuning": "corvettec8_tuning_sound.mp3",
            "zvok_opis": "Corvette V8 ima enega najboljših zvokov na svetu - grozeč, globok ropot pri nizkih vrtljajih in divji krik pri visokih. Z Borla ali Corsa izpuhom postane eden najboljših zvokov na cestah."
        },
                "cas_0_100": 2.9,
        "masa": 1527,
        "prtljaznik": 357,
        "slug": "chevrolet-corvette-c8"
    },

    {
        "id": "bmw-m3-f80",
        "znamka": "BMW",
        "model": "M3 F80",
        "polno_ime": "BMW F80 M3 3.0 turbo S55",
        "cena": 38000,
        "letnik": "2014-2018",
        "motor": "3.0 turbo bencin S55",
        "gorivo": "bencin",
        "moc": 431,
        "kategorija": "sporten",
        "slika": "bmwm3f80.png",
        "slika_tuning": "bmwm3f80_tuning.png",
        "opis": "BMW M3 F80 je zadnji 'pravi' M3 - brez AWD, samo zadnji pogon, ročni menjalnik opcijsko in S55 motor, ki je eden najboljših BMW-jevih motorjev vseh časov. Benchmark med sportnimi sedani.",
        "prednosti": [
            "431 KM S55 motor",
            "Zadnji pogon - čisto BMW ravnanje",
            "Ročni menjalnik (Competition ima DCT)",
            "Benchmark za sportne sedane",
            "Izjemen S55 motor za tuning"
        ],
        "slabosti": [
            "Visoka cena",
            "Vzdrževano drago",
            "Visoka poraba",
            "Rezervni deli dragi"
        ],
        "poraba": "10-14 L/100km",
        "zakaj": "M3 F80 je morda zadnji 'puristični' M3. S55 motor, zadnji pogon in opcijski ročni menjalnik ga delajo za verjetno zadnjega pravega M3 konja.",
        "tuning": {
            "stage1_moc": 510,
            "stage1_opis": "S55 motor je eden najboljših BMW-jevih motorjev za tuning. Stage 1 remap prinese 505-515 KM in do 710 Nm navora. Absolutna preobrazba.",
            "stage1_cena": "500-800 EUR",
            "zvok_stock": "bmwm3f80_stock_sound.mp3",
            "zvok_tuning": "bmwm3f80_tuning_sound.mp3",
            "zvok_opis": "S55 ima eden najboljših 6-valjnih zvokov na svetu. Z downpipe in sport izpuhom (Akrapovič, Milltek) postane zvok resnično spektakularen - glasen, brutalen in melodičen hkrati."
        },
                "cas_0_100": 4.0,
        "masa": 1545,
        "prtljaznik": 480,
        "slug": "bmw-m3-f80"
    },

    {
        "id": "audi-rs4-b8",
        "znamka": "Audi",
        "model": "RS4 Avant B8",
        "polno_ime": "Audi RS4 B8 Avant 4.2 FSI V8",
        "cena": 32000,
        "letnik": "2012-2015",
        "motor": "4.2 V8 FSI bencin",
        "gorivo": "bencin",
        "moc": 450,
        "kategorija": "druzinski",
        "slika": "audirs4b8.png",
        "slika_tuning": "audirs4b8_tuning.png",
        "opis": "Audi RS4 B8 Avant je ultimativni sports karavan z 4.2 V8 motorjem, Quattro pogonom in ogromnim prtljažnikom. Eden redkih avtomobilov, ki zdruje pravo supercar zmogljivost z druzinsko prakticnostjo.",
        "prednosti": [
            "450 KM V8 v karavanu",
            "Quattro AWD pogon",
            "Ogromno prostora za druzino",
            "Brutalen V8 zvok",
            "Ultimativni sports druzinski avto"
        ],
        "slabosti": [
            "Visoka poraba V8 (13-16 L/100km)",
            "Vzdrzevano drago",
            "Rezervni deli dragi",
            "Verižni gonilnik zahteva pozornost"
        ],
        "poraba": "13-16 L/100km",
        "zakaj": "RS4 B8 Avant je avto za tiste, ki hočejo vse - V8 zvok, supercar pospeške in prostor za dve koli v prtljažniku. Absolutno ultimativni druzinski avto.",
        "tuning": {
            "stage1_moc": 480,
            "stage1_opis": "4.2 FSI V8 je atmosferski motor z omejenim tuning potencialom. Stage 1 prinese ~470-480 KM. Pravi karakter je v zvoku.",
            "stage1_cena": "300-500 EUR",
            "zvok_stock": "audirs4_stock_sound.mp3",
            "zvok_tuning": "audirs4_tuning_sound.mp3",
            "zvok_opis": "RS4 B8 V8 ima enega najboljsih zvokov med karavanimi vseh časov. Z Milltek ali Akrapovič izpuhom postane zvok res spektakularen."
        },
                "cas_0_100": 4.7,
        "masa": 1870,
        "prtljaznik": 485,
        "slug": "audi-rs4-b8"
    },

    {
        "id": "mercedes-amg-c63-w204",
        "znamka": "Mercedes-AMG",
        "model": "C63 AMG W204",
        "polno_ime": "Mercedes-AMG C63 W204 6.2 V8",
        "cena": 28000,
        "letnik": "2008-2014",
        "motor": "6.2 V8 atmosferski bencin M156",
        "gorivo": "bencin",
        "moc": 457,
        "kategorija": "sporten",
        "slika": "amgc63w204.png",
        "slika_tuning": "amgc63w204_tuning.png",
        "opis": "Mercedes-AMG C63 W204 z 6.2 litrim V8 motorjem M156 je legendarna kombinacija. Brutalna, glasna in nič subtilna - pravi AMG karakter brez filtrov. Eden zadnjih AMG-jev z atmosferskim V8.",
        "prednosti": [
            "6.2 V8 atmosferski - eden najboljsih zvokov",
            "457 KM čiste moči",
            "Mercedes premium notranjost",
            "Legendarni status AMG",
            "Zadnji veliki atmosferski AMG V8"
        ],
        "slabosti": [
            "Visoka poraba (14-18 L/100km)",
            "Vzdrzevano drago",
            "M156 zahteva redne oljne menjave",
            "Rezervni deli dragi"
        ],
        "poraba": "14-18 L/100km",
        "zakaj": "C63 W204 z M156 motorjem je eden zadnjih pravih AMG-jev. Atmosferski V8, brez elektronike ki bi te zadrzevala, in zvok, ki ga ne pozabiš.",
        "tuning": {
            "stage1_moc": 490,
            "stage1_opis": "M156 je atmosferski motor - stage 1 remap prinese ~480-495 KM. Pravi tuning je v izpuhu in mehaniki.",
            "stage1_cena": "300-500 EUR",
            "zvok_stock": "amgc63_stock_sound.mp3",
            "zvok_tuning": "amgc63_tuning_sound.mp3",
            "zvok_opis": "M156 V8 ima eden najboljsih zvokov avtomobilskega sveta - globok, brutalen, brez filtrov. Z Akrapovičem ali RENNtech izpuhom postane absolutno spektakularen."
        },
                "cas_0_100": 4.5,
        "masa": 1795,
        "prtljaznik": 480,
        "slug": "mercedes-amg-c63-w204"
    },

    {
        "id": "porsche-911-997",
        "znamka": "Porsche",
        "model": "911 Carrera 997",
        "polno_ime": "Porsche 911 Carrera 997 3.6",
        "cena": 35000,
        "letnik": "2004-2008",
        "motor": "3.6 atmosferski bencin boxer",
        "gorivo": "bencin",
        "moc": 325,
        "kategorija": "sporten",
        "slika": "porsche997.png",
        "slika_tuning": "porsche997_tuning.png",
        "opis": "Porsche 911 997 je čistokrven sportski avto z edinstvenim zadnjim boxer motorjem. 997 generacija velja za zadnji 'analogni' 911 brez preveč elektronike - pravi puristični voznik's avto.",
        "prednosti": [
            "Legendarni Porsche 911 karakter",
            "Edinstven boxer zvok",
            "Zadnji 'analogni' 911",
            "Odlično ravnanje in balans",
            "Ikona avtomobilizma"
        ],
        "slabosti": [
            "Visoki stroški vzdrževanja Porsche",
            "IMS tezava na nekaterih motorjih",
            "Rezervni deli dragi",
            "Visoka poraba"
        ],
        "poraba": "10-13 L/100km",
        "zakaj": "997 je za tiste, ki hočejo pravega Porsche 911 brez preveč moderne elektronike. Čistokrven, analogni in ikoničen.",
        "tuning": {
            "stage1_moc": 360,
            "stage1_opis": "3.6 boxer je atmosferski motor z omejenim remap potencialom. Stage 1 prinese ~355-365 KM. Pravi gain je v izpuhu in Sport Chrono paketu.",
            "stage1_cena": "400-700 EUR",
            "zvok_stock": "porsche997_stock_sound.mp3",
            "zvok_tuning": "porsche997_tuning_sound.mp3",
            "zvok_opis": "Porsche boxer motor ima ikoničen zvok - visokofrekvenčen, čist in melodičen. Z sport izpuhom postane eden najboljsih zvokov na svetu."
        },
                "cas_0_100": 5.0,
        "masa": 1395,
        "prtljaznik": 105,
        "slug": "porsche-911-997"
    },

    {
        "id": "bmw-m5-f10",
        "znamka": "BMW",
        "model": "M5 F10",
        "polno_ime": "BMW F10 M5 4.4 V8 biturbo S63",
        "cena": 34000,
        "letnik": "2011-2016",
        "motor": "4.4 V8 biturbo bencin S63",
        "gorivo": "bencin",
        "moc": 560,
        "kategorija": "druzinski",
        "slika": "bmwm5f10.png",
        "slika_tuning": "bmwm5f10_tuning.png",
        "opis": "BMW M5 F10 z 560 KM S63 biturbo V8 motorjem je ultimativni sportski sedan. 4 sedeži, ogromno prostora, 560 KM in 0-100 v 4.2 sekunde. M5 F10 je eden najboljsih avtomobilov vseh časov.",
        "prednosti": [
            "560 KM biturbo V8",
            "Prostoren luksuzni sedan",
            "0-100 v 4.2 sekunde",
            "S63 motor - izvrsten za tuning",
            "Pravi BMW M karakter"
        ],
        "slabosti": [
            "Vzdrzevano drago",
            "Visoka poraba",
            "Rezervni deli dragi",
            "DCT menjalnik zahteva vzdrzevanje"
        ],
        "poraba": "12-16 L/100km",
        "zakaj": "M5 F10 je avto za tiste, ki hočejo vse. 560 KM, luksuz za 5 potnikov in BMW dinamika v enem paketu.",
        "tuning": {
            "stage1_moc": 650,
            "stage1_opis": "S63 biturbo V8 je eden najboljsih motorjev za tuning. Stage 1 remap prinese 640-660 KM in do 850 Nm navora. Absolutno neverjeten rezultat.",
            "stage1_cena": "600-1000 EUR",
            "zvok_stock": "bmwm5f10_stock_sound.mp3",
            "zvok_tuning": "bmwm5f10_tuning_sound.mp3",
            "zvok_opis": "S63 V8 biturbo ima izjemen zvok - globok V8 ton s turbo šumom. Z Akrapovičem postane eden najboljsih zvokov na cestah."
        },
                "cas_0_100": 4.2,
        "masa": 1870,
        "prtljaznik": 520,
        "slug": "bmw-m5-f10"
    },

    {
        "id": "lamborghini-huracan",
        "znamka": "Lamborghini",
        "model": "Huracán LP610-4",
        "polno_ime": "Lamborghini Huracán LP610-4 5.2 V10",
        "cena": 155000,
        "letnik": "2014-2019",
        "motor": "5.2 V10 atmosferski bencin",
        "gorivo": "bencin",
        "moc": 610,
        "kategorija": "sporten",
        "slika": "huracan.png",
        "slika_tuning": "huracan_tuning.png",
        "opis": "Lamborghini Huracán je pravi supercar z 5.2 litrskim V10 atmosferskim motorjem in 610 KM. 0-100 v 3.2 sekunde, AWD pogon in zvok, ki ga ni drugega. Za tiste, ki ne kompromisov.",
        "prednosti": [
            "610 KM V10 atmosferski",
            "0-100 v 3.2 sekunde",
            "AWD Lamborghini pogon",
            "Edinstven V10 zvok",
            "Ikonična Lamborghini oblika"
        ],
        "slabosti": [
            "Izjemno drago vzdrzevano",
            "Praktično neuporaben za vsakdan",
            "Zavarovanje drago",
            "Visoka poraba (18-25 L/100km)"
        ],
        "poraba": "18-25 L/100km",
        "zakaj": "Huracán ni avto - je izkušnja. Za tiste, ki hočejo najboljše kar obstaja in si to lahko privoščijo.",
        "tuning": {
            "stage1_moc": 650,
            "stage1_opis": "5.2 V10 je atmosferski motor z omejenim remap potencialom. Stage 1 prinese ~645-655 KM. Pravi tuning je Performante paket ali supercharger.",
            "stage1_cena": "800-1500 EUR",
            "zvok_stock": "huracan_stock_sound.mp3",
            "zvok_tuning": "huracan_tuning_sound.mp3",
            "zvok_opis": "V10 atmosferski zvok je eden najboljsih na svetu - visokofrekvenčen, brutalen krik pri visokih vrtljajih. Z aftermarket izpuhom postane absolutno nepozaben."
        },
                "cas_0_100": 3.2,
        "masa": 1422,
        "prtljaznik": 100,
        "slug": "lamborghini-huracan"
    },

]


def poisci_avtomobile(budget, tip, gorivo):
    """Poišče avtomobile glede na kriterije. Prazen budget vrne vse avte."""
    rezultati = []
    brez_budget_filtra = (not budget or budget <= 0)
    budget_extended = budget * 1.15 if budget else 0

    for avto in AVTOMOBILI:
        if gorivo != "vseeno" and avto["gorivo"] != gorivo:
            continue
        if tip != "vseeno" and avto["kategorija"] != tip:
            continue
        if not brez_budget_filtra and avto["cena"] > budget_extended:
            continue

        ocena = izracunaj_oceno(avto, budget, tip, gorivo)
        nad_budgetom = (not brez_budget_filtra) and avto["cena"] > budget

        rezultati.append({
            "avto": avto,
            "ocena": ocena,
            "nad_budgetom": nad_budgetom,
            "razlika_cene": (avto["cena"] - budget) if budget else 0
        })

    if brez_budget_filtra:
        rezultati.sort(key=lambda x: x["avto"]["cena"])
    else:
        rezultati.sort(key=lambda x: x["ocena"], reverse=True)
    return rezultati


def izracunaj_oceno(avto, budget, tip, gorivo):
    ocena = 50

    if budget and budget > 0:
        if avto["cena"] <= budget:
            razmerje = avto["cena"] / budget
            if razmerje >= 0.85:
                ocena += 30
            elif razmerje >= 0.70:
                ocena += 20
            else:
                ocena += 10
        else:
            presezenost = (avto["cena"] - budget) / budget
            ocena -= presezenost * 50

    if tip == "vseeno":
        ocena += 10
    elif avto["kategorija"] == tip:
        ocena += 20

    if gorivo == "vseeno":
        ocena += 5
    elif avto["gorivo"] == gorivo:
        ocena += 10

    return max(0, min(100, ocena))


def poisci_avto_po_slugu(slug):
    for avto in AVTOMOBILI:
        if avto["slug"] == slug:
            return avto
    return None
