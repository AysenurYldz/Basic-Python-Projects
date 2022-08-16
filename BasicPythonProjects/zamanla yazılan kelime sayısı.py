# -*- coding: utf-8 -*-
"""
Created on Thu May 13 20:14:27 2021

@author: aysen
"""

# Yazılan herhangi bir metinin ne kadar zamanda yazıldığını ve ortalama olarak saniye başına kaç kelime yazıldığını bulan program

import time
import datetime
print("""Ölçüm için örnek metin: 
          Kadınlarımız için asıl mücadele alanı, asıl zafer kazanılması gereken alan,
          biçim ve kılıkta başarıdan çok, ışıkla, bilgi ve kültürle, gerçek faziletle süslenip donanmaktır.
          Ben muhterem hanımlarımızın Avrupa kadınlarının aşağısında kalmayacak, aksine pek çok yönden
          onların üstüne çıkacak şekilde ışıkla, bilgi ve kültürle donanacaklarından asla şüphe etmeyen
          ve buna kesinlikle emin olanlardanım.""")
print("3 saniye sonra yazmaya başlayınız.")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("Go!")
time.sleep(0.2)
before = datetime.datetime.now()
text=input("Yazın:")
after = datetime.datetime.now()
speed = after - before
seconds = round(speed.total_seconds(),2)
letter_per_second = round(len(text) / seconds,1)
print("Yazma süreniz: {} seconds.".format(seconds))
print("saniyede {} kelime yazdınız.".format(letter_per_second))