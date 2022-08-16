 # -*- coding: utf-8 -*-
"""
Created on Mon May 31 12:11:39 2021

@author: aysen
"""

#Vücut kitle indeksini hesaplayan ve buna göre durumunuzu söyleyen program.
#Vücut Kitle İndeksi Hesaplama Formülü : Vücut Kitle İndeksi (VKİ) = Vücut Ağırlığı (kg.) / Boy uzunluğunun karesi (m2.)
"""
Vücut Kitle İndeksi Sınıflandırma
18.5 ve altı Düşük Kilolu
18.5 - 24.9 Normal Kilolu
25-29.9 Fazla Kilolu
30-40 Obez
40 ve üstü Aşırı Obez
"""

b=eval (input ("Boyunuzu giriniz (m olarak):"))
k=eval (input ("Kilonuzu giriniz (kg olarak): "))
i= (k/b**2)
print("Vücut kitle indeksiniz:",i)
if i >=40:
    print("Aşırı obez olarak sınıflandırılan gruptasınız.")
elif i>=30:
    print("Obez olarak sınıflandırılan gruptasınız.")
elif i>=25:
    print("Fazla kilolu olarak sınıflandırılan gruptasınız.")
elif i>=18.5:
    print("Normal kilolu olarak sınıflandırılan gruptasınız.")    
else:
    print("Düşük kilolu olarak sınıflandırılan gruptasınız.")