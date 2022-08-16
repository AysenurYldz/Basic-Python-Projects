# -*- coding: utf-8 -*-
"""
Created on Mon May 31 21:47:46 2021

@author: aysen
"""

# Dizi elemanlarını toplama

a=[];
s=int(input("Dizinin eleman sayısı: "))
for i in range (0,s):
    print("A(%d) = " %i, end="");
    a.append(int(input()))
print("Dizi elemanları toplamı: %d" %sum(a))