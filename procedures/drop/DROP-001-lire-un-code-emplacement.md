---
code: DROP-001
titre: Lire un code emplacement
poste: Tous postes (stockage, préparation)
version: 1.0
date: 2026-10-15
responsable: Fabrice
statut: validée (nomenclature du 11/05/2026)
---

# DROP-001 : Lire un code emplacement

## Objectif

Savoir où se trouve un emplacement à partir de son étiquette.

## Deux formats

| Type | Format | Exemple | Lecture |
|---|---|---|---|
| Palettier | `[N]P[LETTRE][N]-[NIVEAU]` | `9PJ1-0` | Secteur 9, allée PJ, case 1, niveau 0 (sol) |
| Rack (mezzanine) | `M[n]-R[nn]-C[n]-[niveau]` | `M1-R05-C2-0` | Mezzanine 1, rack 05, case 2, niveau 0 |

## Règles

- Secteurs : S1 à S10, plus S1V et S1A. Mezzanines : M1, M2, M3. La sous-mezzanine existe.
- Aucun palettier en mezzanine ni en sous-mezzanine : uniquement des racks. Un code `M*P*` est une erreur, à signaler à Fabrice.
- Secteur 9 : allée PJ (Classique G1 TLU/TTU) et allée PK (JERO Korpi/Puro/Hari).
- Les étiquettes sont en Code128 : la douchette les lit, le QR ne se lit pas à la douchette.

## En cas de doute

Ne pas deviner un emplacement : prévenir Fabrice.
