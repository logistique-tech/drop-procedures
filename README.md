# drop-procedures

Fiches procédure du dépôt Cheminées Hervé Gehin (projet D.R.O.P.), consultables sur tablette ou téléphone en scannant un QR code affiché au poste concerné.

## Principe

1. Une fiche = un fichier Markdown dans `procedures/`, nommé `PRO-XXX-titre-court.md`.
2. GitHub Pages publie chaque fiche sous une URL stable :
   `https://<compte>.github.io/drop-procedures/procedures/PRO-XXX-titre-court.html`
3. Le workflow `.github/workflows/qr.yml` génère le QR code de chaque fiche dans `qr/` à chaque modification.
4. On imprime le QR et on l'affiche au poste. Le QR pointe toujours vers la dernière version : modifier la fiche ne nécessite pas de réimprimer.

Le QR se lit avec l'appareil photo de la tablette ou d'un téléphone. La douchette Inateck BCST-70 ne lit pas le QR (Code128 uniquement) : elle reste réservée aux emplacements et articles.

## Rédiger une fiche

1. Copier `procedures/_modele.md` vers `procedures/PRO-XXX-titre-court.md`.
2. Remplir l'en-tête (code, titre, poste, version, date, responsable).
3. Étapes courtes, une action par ligne, verbe à l'infinitif.
4. Ajouter la fiche dans `index.md`.

## Règles

- Aucun identifiant, mot de passe, adresse IP ni donnée client dans ce dépôt.
- Ne jamais inventer une référence produit ou une désignation : écrire "à compléter".
- Toute fiche est validée par Fabrice avant affichage (champ `statut: validée`).

## Arborescence

```
procedures/   fiches Markdown
qr/           QR codes générés (PNG), un par fiche
scripts/      génération des QR
index.md      sommaire publié
_config.yml   configuration GitHub Pages
```
