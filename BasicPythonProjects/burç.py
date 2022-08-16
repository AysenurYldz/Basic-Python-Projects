# -*- coding: utf-8 -*-
"""
Created on Mon May 31 17:14:41 2021

@author: aysen
"""

# Doğum günü bilgilerini alarak hangi burç olduğunu bulan program

a=int(input("Dogum gününü giriniz:"))
b=int(input("Dogum ayını sayı olarak giriniz:"))

if ((a>=22) and (b==1)) or ((a<=19) and (b==2)):
    y="Kova"
elif ((a>=20) and (b==2)) or ((a<=20) and (b==3)):
    y="Balık"
elif ((a>=21) and (b==3)) or ((a<=20) and (b==4)):
    y="Koç"
elif ((a>=21) and (b==4)) or ((a<=21) and (b==5)):
    y="Boğa"
elif ((a>=22) and (b==5)) or ((a<=22) and (b==6)):
    y="İkizler"
elif ((a>=23) and (b==6)) or ((a<=22) and (b==7)):
    y="Yengeç"
elif ((a>=23) and (b==7)) or ((a<=22) and (b==8)):
    y="Aslan"
elif ((a>=23) and (b==8)) or ((a<=22) and (b==9)):
    y="Başak"
elif ((a>=23) and (b==9)) or ((a<=22) and (b==10)):
    y="Terazi"
elif ((a>=23) and (b==10)) or ((a<=21) and (b==11)):
    y="Akrep"
elif ((a>=22) and (b==11)) or ((a<=21) and (b==12)):
    y="Yay"
else:
    y="Oğlak"

print('Burcunuz: {}'.format(y))