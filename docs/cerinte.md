# Cerințe: dashboard KPI pe date bancare (Berka)

## 1. Context
Dataset public cu date bancare cehe (Berka, 1993-1998): conturi, clienți, tranzacții, credite. Scopul: un set mic de indicatori calculați în SQL, exportați cu Python și afișați într-un dashboard Tableau Public.

## 2. Întrebări de business
- Cum evoluează volumul și valoarea tranzacțiilor de la o lună la alta?
- Câte conturi sunt active pe lună?
- Cum evoluează valoarea tranzacțiilor față de luna anterioară?
- Cum arată soldul mediu în timp?
- Cum arată portofoliul de credite (număr, sumă acordată, pe status, cu probleme)?

## 3. Definiții
- **Tranzacție** = un rând din tabelul `trans`.
- **Client activ** = cont cu cel puțin o tranzacție în luna respectivă. Berka măsoară conturi, nu persoane, deci „client activ" înseamnă „cont activ".
- **Valoarea tranzacțiilor** = suma coloanei `amount`, fără separare între încasări și plăți (în Berka `amount` e mereu pozitiv; tipul e în coloana `type`).
- **Creștere lunară** = `(valoare lună curentă - valoare lună anterioară) / valoare lună anterioară * 100`. Prima lună nu are valoare (nu există lună anterioară).
- **Sold mediu** = media coloanei `balance` din `trans`, pe lună. E o medie pe tranzacții, nu pe conturi.
- **Statusuri credit**: A = contract terminat, rambursat; B = contract terminat, nerambursat; C = în derulare, fără probleme; D = în derulare, client în datorii.
- **Credit cu probleme** = status B sau D.
- **Rata creditelor cu probleme** = credite cu probleme / total credite * 100.

## 4. Indicatori (KPI)
| # | Indicator | Interogare |
|---|---|---|
| 1 | Număr și valoare tranzacții pe lună | `sql/01_tranzactii_lunar.sql` |
| 2 | Conturi active pe lună | `sql/02_clienti_activi.sql` |
| 3 | Creștere lunară a valorii tranzacțiilor | `sql/03_crestere_lunara.sql` |
| 4 | Credite pe status (număr, sumă, medie) | `sql/04_credite_status.sql` |
| 5 | Sold mediu pe lună | `sql/05_sold_mediu.sql` |
| 6 | Rata creditelor cu probleme | `sql/06_rata_probleme.sql` |

## 5. Criterii de acceptanță
- Numărul total de tranzacții din Tableau = numărul din SQL (1.056.320).
- Seria lunară are 72 de luni (ian 1993 - dec 1998), fără luni lipsă.
- Numărul de conturi active dintr-o lună din dashboard = rezultatul interogării SQL pentru acea lună și nu depășește 4.500 (conturile existente).
- Suma creditelor pe status = 682 (total credite).
- Rata creditelor cu probleme din dashboard = rezultatul din SQL.

## 6. Limitări și observații
- Valoarea tranzacțiilor amestecă încasările cu plățile, deci arată volumul de bani mișcați, nu venitul băncii.
- Conturile active cresc în 1993-1998 în mare parte pentru că se deschid conturi noi, nu neapărat pentru că se folosesc mai mult. De aceea și creșterile lunare din 1993 sunt foarte mari, iar graficul de creștere începe din 1994.
- În fiecare ianuarie apare un vârf la numărul de tranzacții. Cauza nu a fost investigată.
- Soldul mediu pornește jos în 1993 din același motiv (conturile abia se deschid).

## 7. Validare
Cifrele din dashboard au fost comparate cu cele din SQL.

| Indicator | SQL | Dashboard | OK |
|---|---|---|---|
| Total tranzacții | 1.056.320 | 1.056.320 | da |
| Luni în serie | 72 | 72 | da |
| Tranzacții ianuarie 1998 | 42.940 | 42.940 | da |
| Conturi active martie 1993 | 298 | 298 | da |
| Total credite | 682 | 203 + 31 + 403 + 45 = 682 | da |
| Credite cu probleme | 76 (31 B + 45 D) | 31 + 45 = 76 | da |
| Rata credite cu probleme | 11,14% | 11,14% | da |

Data validării: 27.10.2026