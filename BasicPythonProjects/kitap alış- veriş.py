# -*- coding: utf-8 -*-
"""
Created on Sun May 30 19:31:27 2021

@author: aysen
"""

# Listedeki kitaplardan seçilenin fiyatının öğrenilmesi programı

print(" Hosgeldınız. Alttaki listeden istediginiz kitabı seçiziz. ")
print("""1_Yabancı - Albert Camus 
      2_Küçük Prens - Antoine de Saint-Exupéry
      3_Fareler ve İnsanlar - John Steinbeck
      4_ Silahlara Veda - Ernest Hemingway
      5_Hayvan Çiftligi - George Orwell
      6_Kapıların Dışında - Wolfgang Borchert
      7_Açlık - Knut Hamsung
      8_Kendine Ait Bir Oda - Virginia Woolf
      9_Koleksiyoncu - John Fowles 
      10_Veronika Ölmek İstiyor – Paulo Coelho""")   
y =(input("Seçtiğiniz kitabın listedeki sırasını giriniz : " ))
i = (input(""" İnternetten sipariş edecekseniz 1'e kitapçıdan alacaksanız 2'ye basınız.
           Not:İnternet siparisinde barkot fiyatı üzerinden %30 indirim uygulanmaktadır."""))

if y== "1": 
  if i== "1" :
    t = 21*(70/100) ;
  elif i == "2" :
    t = 21 ;
elif y == "2":
   if i== "1" :
    t = 10*(70/100) ;
   elif i == "2" :
    t = 10;
elif y== "3": 
  if i== "1" :
    t = 20*(70/100) ;
  elif i == "2" :
    t = 20 ; 
elif y== "4": 
  if i== "1" :
    t = 44*(70/100) ;
  elif i == "2" :
    t = 44 ; 
elif y== "5": 
  if i== "1" :
    t = 11*(70/100) ;
  elif i == "2" :
    t = 11 ; 
elif y== "6": 
  if i== "1" :
    t = 21.50*(70/100) ;
  elif i == "2" :
    t = 21.50 ; 
elif y== "7": 
  if i== "1" :
    t = 21*(70/100) ;
  elif i == "2" :
    t = 21 ; 
elif y== "8": 
  if i== "1" :
    t = 15*(70/100) ;
  elif i == "2" :
    t = 15 ; 
elif y== "9": 
  if i== "1" :
    t = 38*(70/100) ;
  elif i == "2" :
    t = 38 ; 
elif y== "10": 
  if i== "1" :
    t = 33*(70/100) ;
  elif i == "2" :
    t = 33 ;     
    
print ("\n Kitap fiyatı (tl): {:.2f}\n" .format(t))
