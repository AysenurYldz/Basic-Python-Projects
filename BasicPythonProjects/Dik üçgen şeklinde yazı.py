# -*- coding: utf-8 -*-
"""
Created on Mon May 31 22:00:25 2021

@author: aysen
"""

# Dik üçgen şeklinde yazı yazdırma
a= input("Kelime giriniz: "); print("")
for i in range ( len(a) ) :
    for j in range (i+1):
        print("%c" %a[j], end ="")
    print ("")