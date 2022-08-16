# -*- coding: utf-8 -*-
"""
Created on Mon May 31 21:29:45 2021

@author: aysen
"""

# Mükemmel Sayı
#Kendisi hariç bütün pozitif bölenlerinin toplamı kendisine eşit olan sayılara mükemmel sayı denir.

s= int(input("Bir sayi giriniz: "))
 
toplam=0
 
for i in range(1,s):
    if(s%i == 0):
        toplam +=i    
if(s == toplam):
    print("Mükemmel sayidir.")
else:
    print("Mükemmel sayi degildir")