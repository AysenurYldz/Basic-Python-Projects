# -*- coding: utf-8 -*-
"""
Created on Mon May 31 18:33:15 2021

@author: aysen
"""

#Girilen sayının Armstrong sayısı olup olmadığını bulan program
#Sayıyı rakamlara ayırıp, basamak sayısını bu rakamlara üs olarak verip bu sayıları topladığımızda toplama işlemi sonucu yine aynı sayı çıkıyorsa bu sayıya Armstrong Sayı denir..

while True:
   
    s=input("Sayı girin : ")
    print("Not: Programı sonlandırmak için w'a basmanız gerekmektedir..")
    
    if s=="w":
        break
    
    l=len(s)
    t=0
    for i in range(l):
        t = t + int(s[i])**l
    if(t==int(s)):
        print("Girdiginiz sayı bir Armstrong sayısıdır!")
    else:
        print("Girdiginiz sayı Armstrong sayısı degildir!")
 
 