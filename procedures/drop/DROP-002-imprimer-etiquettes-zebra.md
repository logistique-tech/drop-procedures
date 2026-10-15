---
code: DROP-002
titre: Imprimer des étiquettes sur la Zebra
poste: PC entrepôt
version: 1.0
date: 2026-10-15
responsable: Fabrice
statut: brouillon (calibration validée, étapes à confirmer sur le poste)
---

# DROP-002 : Imprimer des étiquettes sur la Zebra

## Objectif

Imprimer une étiquette depuis un fichier ZPL sur la Zebra ZD220/ZD230 du PC entrepôt.

## Réglages validés

- Imprimante partagée sous le nom `\\localhost\Zebra`.
- Calibration : `^LH-200,15` puis `^CI28` (accents) en tête du fichier ZPL.
- Envoi en mode binaire (`copy /b`).

## Étapes

1. Vérifier que la Zebra est allumée et que le rouleau d'étiquettes est en place.
2. Ouvrir l'invite de commandes dans le dossier du fichier `.zpl`.
3. Lancer : `copy /b nom_du_fichier.zpl \\localhost\Zebra`
4. Contrôler la première étiquette : texte entier, code-barres net.

## En cas de problème

| Symptôme | Action |
|---|---|
| Rien ne sort | Vérifier le partage `Zebra` et l'état de l'imprimante : à compléter |
| Texte décalé ou coupé | Vérifier `^LH-200,15` en tête du fichier |
| Accents illisibles | Vérifier `^CI28` en tête du fichier |

## Règle

Les étiquettes emplacement et produit sont produites par Odoo (module `drop_labels`), pas fabriquées à la main : cette fiche sert à les envoyer à l'imprimante.
