# -*- coding: utf-8 -*-
"""
Created on Mon May 31 21:20:26 2021

@author: aysen
"""

#Ohm Kanunu ile gerilimi hesaplayan program (V=I*R)

r=int(input("İletkenin direncini giriniz: "))
ı=int(input("İletkenin içinden geçen akımı giriniz: "))
v=ı*r
print("Gerilim: {}" .format(v))