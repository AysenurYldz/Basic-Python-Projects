# -*- coding: utf-8 -*-
"""
Created on Mon May 31 03:15:18 2021

@author: aysen
"""
#Kare, dikdörtgen, üçgen ve paralelkenarın alanını hesaplayan program

import time
    
def kare(a):
    print("Karenin alanı: {}".format(a*a))
def dikdortgen(a,b):
    print("Dikdörtgenin alanı: {}".format(a*b))
def ucgen(t,y):
    u = (t*y) / 2
    print("Üçgenin alanı: {}".format(u))
def paralelKenar(t,y):
    print("Paralel kenarın alanı: {}".format(t*y))

while True:
    print("""
    1: Kare
    2: Diktörgen
    3: Dik Ücgen
    4: Paralel Kenar
    5: Cıkıs
    """)
    s= int(input("Alanını hesaplamak istediginiz geometrik sekli seciniz: "))
    if s == 1:
        a= int(input(" Bir kenar uzunlugunu giriniz: "))
        kare(a)
    elif s == 2:
        a = int(input("Kısa kenar uzunlugunu giriniz: "))
        b= int(input("Uzun kenar uzunlugunu giriniz: "))
        dikdortgen(a,b)
    elif s == 3:
        t = int(input("Taban uzunluğunu giriniz: "))
        y = int(input("Yüksekligini giriniz: "))
        ucgen(t,y)
    elif s == 4:
        t = int(input("Taban uzunluğunu giriniz: "))
        y = int(input("Yüksekliğini giriniz: "))
        paralelKenar(t,y)
    elif s==5:
        print("Cikis yapılıyor")
        time.sleep(2)
        break
    
    