# -*- coding: utf-8 -*-
"""
Created on Sun May 30 23:43:39 2021

@author: aysen
"""


import random
import time

k=input('Birinci kullanıcının adı: ')
l=input('İkinci kullanıcının adı: ')

a=["Taş","Kagıt","Makas"]

def sonuc():
    if b==i:
        print("Beraberlik")
    elif (b=="Taş") and (i=="Kagıt"):
        print("{} kazandı.".format(l))
    elif (b=="Taş") and (i=="Makas"):
        print("{} kazandı.".format(k))
    elif (b=="Kagıt") and (i=='Taş'):
        print("{} kazandı.".format(k))
    elif (b=="Kagıt") and (i=="Makas"):
        print("{} kazandı.".format(l))
    elif (b=="Makas") and (i=="Taş"):
        print("{} kazandı.".format(l))
    else:
        print("{} kazandı.".format(k))
        
while 1:
    time.sleep(0.5)
    b=random.choice(a)
    time.sleep(0.5)
    i=random.choice(a)
    print("{}=".format(k),b)
    print("{}=".format(l),i)
    sonuc()
    break    