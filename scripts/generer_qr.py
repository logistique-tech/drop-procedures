"""Génère un QR code PNG par fiche de procedures/ vers qr/.

Les fiches sont rangées par famille (procedures/drop, procedures/atelier) :
l'arborescence est reprise dans qr/ et dans l'URL, pour que chaque famille
ait ses propres QR. BASE_URL vient du workflow pour rester indépendant du compte.
"""
import logging
import os
import sys
from pathlib import Path

import qrcode

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
RACINE = Path(__file__).resolve().parent.parent
SOURCE = RACINE / "procedures"


def main() -> int:
    base_url = os.environ.get("BASE_URL", "").rstrip("/")
    if not base_url:
        logging.error("BASE_URL absente")
        return 1
    fiches = sorted(
        p for p in SOURCE.rglob("*.md")
        if not p.name.startswith("_") and p.name.lower() != "readme.md"
    )
    for fiche in fiches:
        rel = fiche.relative_to(SOURCE).with_suffix("")
        url = f"{base_url}/procedures/{rel.as_posix()}.html"
        cible = (RACINE / "qr" / rel).with_suffix(".png")
        try:
            cible.parent.mkdir(parents=True, exist_ok=True)
            # Correction d'erreur élevée : le QR reste lisible s'il est plastifié ou abîmé.
            qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
            qr.add_data(url)
            qr.make(fit=True)
            qr.make_image().save(cible)
            logging.info("%s -> %s", fiche.name, url)
        except Exception:
            logging.exception("Échec pour %s", fiche.name)
            return 1
    logging.info("%d QR générés", len(fiches))
    return 0


if __name__ == "__main__":
    sys.exit(main())
