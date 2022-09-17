# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 23:09:30 2022

@author: Miguel
"""
'''
Se necesita un programa que solicite al usuario el ingreso de una temperatura en escala
Fahrenheit (debe permitir decimales) y le muestre el equivalente en grados Celsius. La fórmula de
conversión que se usa para este cálculo es: _Celsius = (5/9) * (Fahrenheit-32)
Input: Temperatura en Fahrenheit (float)
Output: Temperatura en Celsius (float)
'''

fahrenheit = float(input("\nInserte Temperatura en Farenheit: "))
celcius = (5/9) * (fahrenheit-32)
print(f'Su temperatura en Celsius es {celcius}')
