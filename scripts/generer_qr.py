"""Génère un QR code PNG par fiche de procedures/ vers qr/.

L'URL de base vient de BASE_URL (fournie par le workflow) pour que le
même script serve quel que soit le compte GitHub qui héberge le dépôt.
"""
import logging
import os
import sys
from pathlib import Path

import qrcode

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
RACINE = Path(__file__).resolve().parent.parent


def main() -> int:
    base_url = os.environ.get("BASE_URL", "").rstrip("/")
    if not base_url:
        logging.error("BASE_URL absente")
        return 1
    sortie = RACINE / "qr"
    sortie.mkdir(exist_ok=True)
    fiches = sorted(
        p for p in (RACINE / "procedures").glob("*.md") if not p.name.startswith("_")
    )
    for fiche in fiches:
        url = f"{base_url}/procedures/{fiche.stem}.html"
        try:
            # Correction d'erreur élevée : le QR reste lisible s'il est plastifié ou abîmé.
            qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
            qr.add_data(url)
            qr.make(fit=True)
            qr.make_image().save(sortie / f"{fiche.stem}.png")
            logging.info("%s -> %s", fiche.name, url)
        except Exception:
            logging.exception("Échec pour %s", fiche.name)
            return 1
    logging.info("%d QR générés", len(fiches))
    return 0


if __name__ == "__main__":
    sys.exit(main())
