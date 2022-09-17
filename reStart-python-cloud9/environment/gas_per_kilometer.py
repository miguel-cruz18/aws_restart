# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 22:25:54 2022

@author: Miguel
"""
"""
Se necesita un programa que solicite al usuario ingresar la cantidad de 
kilómetros recorridos por una motocicleta y la cantidad de litros de 
combustible que consumió durante ese recorrido para mostrar el consumo de 
combustible por kilómetro.
Input: Kilómetros recorridos (float > 0), Litros de combustible gastados (float > 0)
Output: Consumo por kilómetro.
Ejemplo de ejecución:
Kilómetros recorridos: 260
Litros de combustible gastados: 12.5
El consumo por kilómetro es de 20.8.
"""

while True:
    kilometrosRecorridos = float(input("\nInserte los kilometros recorridos: "))
    combustibleGastado = int(input("\nInserte el combustible gastado en Litros: "))
    if kilometrosRecorridos > 0 and combustibleGastado > 0:
        combustiblePorKilometro = kilometrosRecorridos/combustibleGastado
        print(f"\nEl consumo por kilómetro es de {combustiblePorKilometro}")
        break
    else:
        print("\nVuelva e ingrese sus datos correctamente\n") 