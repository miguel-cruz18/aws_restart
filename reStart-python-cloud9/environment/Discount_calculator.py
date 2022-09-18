# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 21:56:19 2022

@author: Miguel
"""

'''
Se necesita un programa que calcule el precio final de un producto que cuenta con el 15% de
descuento.
Input: Precio del producto (float > 0)
Output: Precio total con descuento (float > 0)
'''

while True:
    precioOriginal = float(input("Inserte el precio del producto que desea: "))
    if precioOriginal > 0:
        print(f'\nSu total con descuento es {precioOriginal*0.85}')
        break
    else:
        print("\nInserte un precio mayor que 0\n")