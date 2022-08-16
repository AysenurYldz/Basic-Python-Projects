# -*- coding: utf-8 -*-
"""
Created on Mon May 31 11:41:02 2021

@author: aysen
"""

# Rastgele sayı seçilip ve 3 tahmin hakkı verilince seçilen sayıyı bulmaya çalışma programı.

import random

s = random.randint(1,100)
th= 3
print("1 ile 100 arsından rastgele secilen sayıyı tahmin ediniz. Toplam 3 tahmin hakkınız bulunmaktadır.")
while True:
    t = int(input("Tahmininizi Giriniz: "))
    if t == s:
        print("Tebrikler! Kazandınız.")
        break
    elif t> s:
        th -= 1
        print("Yanlıs tahmin, tahmininizi kücültünüz. ")
        print("Kalan tahmin hakkı: ", th)
    elif t < s:
        th -= 1
        print("Yanlıs tahmin, tahmininizi büyütünüz. ")
        print("Kalan tahmin hakkı: ", th)
    if th == 0:
        print("Hakkınız bitmistir.", "Seçilen sayı: ", s)
        break
