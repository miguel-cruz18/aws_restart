# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 20:04:53 2022

@author: Miguel
"""

# Piden al usuario cuantos ingresos ingresan
# El usuario va a ingresar sus ingresos
# Piden al usuario cuantos gastos ingresan
# El usuario va a ingresar sus gastos
# Sumar los gastos y tener un total de gastos
# Sumar los ingresos y tener un total de ingresos
# Calcular el dinero total que le queda al usuario

g = int(input("Cuantos ingresos va a ingresar?: "))
ingresos = []
ingresoTotal = 0
for i in range(g):
    ingresos.append(int(input("Ingresa tu ingreso: ")))
    ingresoTotal += ingresos[-1]

p = int(input("Cuantos gastos va a tener?: "))
gastos = []
gastoTotal = 0
for i in range(p):
    gastos.append(int(input("Ingresa tu ingreso: ")))
    gastoTotal += gastos[-1]
print(f"\nEl dinero total que le queda es {ingresoTotal-gastoTotal}")