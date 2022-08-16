# -*- coding: utf-8 -*-
"""
Created on Sun May 30 23:32:09 2021

@author: aysen
"""
# Girilen iki sayının en büyükortak bölenlerini hesaplayan ve ikisini de bölen tüm sayıları listeleyen program

def ebob(s1,s2):
    global liste
    liste = []
    i = 1
    while i < s1:
        if (s1 % i == 0) and (s2 % i == 0):
            liste.append(i)
        else:
            pass
        i += 1

s1 = int(input("Küçük sayıyı giriniz: "))
s2 = int(input("Büyük sayıyı giriniz: "))
ebob(s1,s2)
liste.sort()
print("Tam bölenlerinin listesi:",liste)
print("EBOB:",liste[len(liste) - 1])