# -*- coding: utf-8 -*-
"""
Created on Mon May 31 14:34:37 2021

@author: aysen
"""

# Girilen para birimini TL'ye dönüştürme

print("""
   1: Dolar
   2: Euro
   3: Pound
   4: Bulgar Levası
   """)


def dolar(tl):
    Dolar = tl * 8.4889
    return Dolar

def euro(tl):
    Euro = tl * 10.3511
    return Euro

def pound(tl):
    Pound = tl * 12.0376
    return Pound

def leva(tl):
    Bulgar_Levası = tl * 5.2920   
    return Bulgar_Levası

s=int(input("Lütfen TL'ye dönüştürmek istediginiz para birimini seciniz: "))
para= float(input("Lütfen TL'ye dönüştürmek istediginiz miktarı giriniz: "))

if s==1:
    print("Dolar: ", dolar(para))
if s==2:
    print("Euro: ", euro(para))
if s==3:
    print("Pound: ", pound(para))
if s==4:
    print("Bulgar Levası: ", leva(para))


    


