# -*- coding: utf-8 -*-
"""
Created on Mon May 31 14:37:24 2021

@author: aysen
"""

# Kalıtımları bilinen iki bezelyenin çaprazlanması sonucu oluşacak bezelyenin kalıtımının belirlenmesi
print("""
      Bezelyede tohum renginde sarı renk yeşil renge göre daha baskındır. Yeşil renk çekiniktir.  
      1. SS (Sarı renk- homozigot) olur 
      2. ss (Yesil renk- homozigot)
      3. Ss (Sarı renk- heterozigot)""")
a= int(input("1. bezelyenin kalıtımını giriniz (sayı olarak):"))
b= int(input("2. bezelyenin kalıtımını giriniz (sayı olarak):"))

if a==1 and b==1:
    print("Oluşan bezelyenin kalıtımı SS (Sarı renk- homozigot) olur")
elif a==1 and b==2:
    print("Oluşan bezelyenin kalıtımı Ss (Sarı renk- heterozigot")  
elif a==1 and b==3:
    print("""Oluşan bezelyenin kalıtımı %50 Ss (Sarı renk- heterozigot),
          %50 SS (Sarı renk- homozigot) olur""")
elif a==2 and b==1:
    print("Oluşan bezelyenin kalıtımı Ss (Sarı renk- heterozigot")
elif a==2 and b==2:
    print("Oluşan bezelyenin kalıtımı ss (Yeşil renk- homozigot) olur")
elif a==2 and b==3:
    print("""Oluşan bezelyenin kalıtımı %50 Ss (Sarı renk- heterozigot),
          %50 ss (Yeşil renk- homozigot) olur""")
elif a==3 and b==1:
    print("""Oluşan bezelyenin kalıtımı %50 Ss (Sarı renk- heterozigot),
          %50 SS (Sarı renk- homozigot) olur""")
elif a==3 and b==2:
    print("""Oluşan bezelyenin kalıtımı %50 Ss (Sarı renk- heterozigot),
          %50 ss (Yeşil renk- homozigot) olur""")
elif a==3 and b==3:
    print("""Oluşan bezelyenin kalıtımı %50 Ss (Sarı renk- heterozigot), 
          %25 SS (Sarı renk- homozigot), %25 ss (Yesil renk- homozigot) olur.""")
             