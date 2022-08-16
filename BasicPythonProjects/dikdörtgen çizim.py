# -*- coding: utf-8 -*-
"""
Created on Mon May 31 16:58:16 2021

@author: aysen
"""

# Kısa kenar ve uzun kenar girilen dikdörtgenin çizimi

a=int(input("Kısa kenarı giriniz: "))
b=int(input("Uzun kenarı giriniz: "))
def kk(a):
    print(' _'*a)
def uk(b):
    print((b-1)*('|'+(a*2-1)*' '+'|\n')+'|'+'_'+(a-1)*' _'+'|')
kk(a)
uk(b)