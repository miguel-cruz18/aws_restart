# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 19:13:56 2022

@author: Miguel
"""

'''
Escriba un programa que reciba el nombre y el apellido de una persona e imprima las iniciales de
su nombre completo.
Entrada: nombre (str)
Salida: Mensaje indicando las iniciales del nombre completo de la persona
Ejemplo: “Alfredo López” -> Las iniciales son A L
'''

firstName = input("\nEcriba su nombre: ")
lastName = input("\nEscriba su apellido: ")

print(f"Tus iniciales son {firstName[0].capitalize()}{lastName[0].capitalize()}")
