# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 18:47:59 2022

@author: Miguel
"""

'''
Desarrollar un programa que muestre los primeros 10 numeros de una sucsion
'''

#Se crea un lista vacia para pedir numeros al usuario y ubicarlos en la lista
sucecion = []
for i in ["Primer", "Segundo"]:
    sucecion.append(int(input(f"\nInserte el {i} numero de la sucecion: ")))

#se suma la sucecion de los ultimos dos numeros en la lista hasta tener 10
while len(sucecion) < 10:
    sucecion.append(sucecion[-1] + sucecion[-2])

print(sucecion)