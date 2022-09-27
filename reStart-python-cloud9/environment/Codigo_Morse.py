# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 20:16:34 2022

@author: Migue
"""

'''
Tenemos guardado en un diccionario los códigos morse correspondientes a cada carácter.
Escribir un programa que lea una palabra y la muestre usando el código morse
'''

codigoMorse = {
'A': '.-', 'B': '-...', 'C': '-.-.',
'D': '-..', 'E': '.', 'F': '..-.',
'G': '--.', 'H': '....', 'I': '..',
'J': '.---', 'K': '-.-', 'L': '.-..',
'M': '--', 'N': '-.', 'O': '---',
'P': '.--.', 'Q': '--.-', 'R': '.-.',
'S': '...', 'T': '-', 'U': '..-',
'V': '...-', 'W': '.--', 'X': '-..-',
'Y': '-.--', 'Z': '--..', '1': '.----',
'2': '..---', '3': '...--', '4': '....-',
'5': '.....', '6': '-....', '7': '--...',
'8': '---..', '9': '----.', '0': '-----',
'.': '.-.-.-', ',': '--..--', ':': '---...',
';': '-.-.-.', '?': '..--..', '!': '-.-.--',
'"': '.-..-.', "'": '.----.', '+': '.-.-.',
'-': '-....-', '/': '-..-.', '=': '-...-',
'_': '..--.-', '$': '...-..-', '@': '.--.-.',
'&': '.-...', '(': '-.--.', ')': '-.--.-'
}

mensaje = input("\nEscriba mensaje a traducir: ")
mensaje = mensaje.upper()
traduccion = []
for i in mensaje:
    traduccion.append(codigoMorse[i])
print(traduccion)
