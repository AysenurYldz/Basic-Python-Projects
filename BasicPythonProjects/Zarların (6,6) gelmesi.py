# -*- coding: utf-8 -*-
"""
Created on Sun May 30 01:04:10 2021

@author: aysen
"""


# Atılan iki zarın aynı anda 6 olduğu durumun kaçıncı denemede gerçekleştiğinin bulunması programı

import random
import time

i = 1
while True:
    zar1 = random.randint(1, 6)
    zar2 = random.randint(1, 6)

    if zar1 == 6 and zar2 == 6:
        print("""Deneme {}:\t({},{}) """.format(i, zar1, zar2))
        time.sleep(1)
        break

    print("""Deneme {}:\t({},{}) """.format(i, zar1, zar2))
    i += 1
    time.sleep(0.4)

print("""\n {}. deneme """.format(i))

