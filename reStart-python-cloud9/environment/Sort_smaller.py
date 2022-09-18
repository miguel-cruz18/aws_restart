# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 22:16:54 2022

@author: USER
"""

'''
Se necesita un programa que solicite al usuario 3 números y muestre en pantalla el menor de los 3
Ejemplo de ejecución:
Primer número: 20
Segundo número: 30
Tercer número: 10
Menor: 10
'''

listaDeNumeros = []
for x in ["primer", "segundo", "tercer"]:
    listaDeNumeros.append(int(input(f"\nInserte el {x} numero: ")))

listaDeNumeros.sort()
print(f"\nEl menor de los tres numeros es {listaDeNumeros[0]}")
