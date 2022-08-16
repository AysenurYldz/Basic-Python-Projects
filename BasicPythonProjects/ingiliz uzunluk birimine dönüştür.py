# -*- coding: utf-8 -*-
"""
Created on Mon May 31 03:35:22 2021

@author: aysen
"""

# Metre olarak girilen uzunluğu İngiliz uzunluk birimlerine çeviren program
#1 fit 0,3048 metre, 1 yardanın uzunluğunu 0,9144 metre, inç 0,0254 metre'dir.

def fit(m):
    Fit = m * 0.3048
    return Fit

def yard(m):
    Yard = m * 0.9144
    return Yard

def inc(m):
    Inc = m * 0.0254
    return Inc



uzunluk = float(input("Lütfen metre olarak uzunlugu giriniz: "))
print("Fit: ", fit(uzunluk))
print("Yard: ", yard(uzunluk))
print("Inc: ", inc(uzunluk))