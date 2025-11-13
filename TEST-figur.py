#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 12:25:26 2025

@author: SiljeMarie
"""

print("Dette programmet regner ut areal og ytre omkrets av følgende figur:")

import sys
sys.path.append("PY1010")

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

bilde = mpimg.imread("FIGUR.png")
plt.imshow(bilde)
plt.axis("off")
plt.show()

import math 

a = 8
b = 16

def figur_a_yo(a,b):
    c = math.sqrt (a**2 + b**2)
    areal = math.pi * (a/2)**2 / 2 + (b*a)/2
    ytre_omkrets = math.pi * (a / 2) + b + c
    return areal, ytre_omkrets

res1 = float(figur_a_yo(a,b)[0])
res2 = float(figur_a_yo(a,b)[1])

print("La oss si at a =", a,"cm og b =", b,"cm. Da blir resultatet at "
      "figurens areal er", round(res1, 1),"cm2, " 
      "og den ytre omkretsen blir", round(res2, 1), "cm.")