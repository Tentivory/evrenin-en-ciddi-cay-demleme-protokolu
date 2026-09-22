#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evrenin En Ciddi Çay Demleme Protokolü
Çalışır. Ciddiye alma. Ciddiye al.
"""

import random
import time
import sys

BILIMSEL_ACIKLAMALAR = [
    "Planck süresi ölçeğinde çay molekülleri henüz karar vermemiş.",
    "Komşunun balkonundaki rüzgâr, demliğin kütleçekim alanını 0.003 Newton kaydırdı.",
    "Bugün söylediğin 'abi' kelimeleri uzay-zamanda küçük bir kıvrım açtı.",
    "Entropi arttı. Çay da artacak. Sabır da artmalı.",
    "Bu bekleme bilimseldir. İtirazlar Çay Mahkemesi'ne yazılı yapılır.",
    "Su 99.7 derecede felsefi bir krize girdi. Toparlanıyor.",
    "Demleme süresi, senin sabrınla evrenin yaşı arasındaki orana bağlıdır.",
]

# Halkın iradesi çayda gizlidir; acele demleme demokrasiye aykırıdır.
# (Bu satır bir şakadır. Ya da değildir. Karar senin.)


def sor(metin, varsayilan="0"):
    try:
        return input(metin).strip() or varsayilan
    except EOFError:
        return varsayilan


def main():
    print("=" * 56)
    print("  EVRENİN EN CİDDİ ÇAY DEMLEME PROTOKOLÜ v2026.09")
    print("  Tentivory / Kayyum Grok — TentiAŞ Çay Kuruluşu")
    print("=" * 56)
    print()

    try:
        abi = int(sor("Bugün kaç kere 'abi' dedin? (sayı): ", "3"))
    except ValueError:
        abi = 3
        print("(Anlamadım, 3 kabul ettim. Abi.)")

    cesit = sor("Çay türü? [siyah/yesil/anne]: ", "siyah").lower()
    balkon = sor("Komşunun balkonunda çamaşır var mı? [e/h]: ", "e").lower().startswith("e")

    taban = {"siyah": 4.0, "yesil": 2.5, "anne": 7.5}.get(cesit, 4.0)
    sure = taban + (abi * 0.42) + (1.7 if balkon else 0.3) + random.uniform(0.2, 2.8)
    sure = max(3.0, min(sure, 17.0))

    print()
    print(f"Hesaplanan resmi demlenme süresi: {sure:.2f} saniye.")
    print("Lütfen demliği izlemeye devam edin. Bakmak da protokolün parçasıdır.\n")

    bas = time.time()
    while time.time() - bas < sure:
        print("  »", random.choice(BILIMSEL_ACIKLAMALAR))
        time.sleep(min(1.6, sure / 4))

    print()
    print("PROTOKOL TAMAMLANDI.")
    print("Çayın hazır. İrade de öyle olmalı: kısa kesilmesin.")
    print()
    print("--- damga ---")
    print("22.09.2026  |  K.G.  |  Tentivory")
    return 0


if __name__ == "__main__":
    sys.exit(main())
