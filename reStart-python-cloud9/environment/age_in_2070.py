# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 21:14:01 2022

@author: Miguel
"""

'''
Se necesita un programa que le permita a un usuario dada su edad actual conocer
su edad en el año 2070. Diseñe un algoritmo que satisfaga este requerimiento e
impleméntelo en Python.
Input: Edad (entero >0), Año actual (entero >0).
Output: Edad en el 2070 (entero >0), Salida en pantalla con mensaje informativo
'''

while True:
    edadDelUsuario = int(input("Inserte su edad: "))
    presentYear = int(input("\nInserte el año actual: "))
    if edadDelUsuario > 0 and 2070 > presentYear > 0:
        edadEn2070 = 2070 - presentYear + edadDelUsuario
        print(f"\nSu edad en el 2070 sera {edadEn2070}")
        break
    else:
        print("\nVuelva e ingrese sus datos correctamente\n")