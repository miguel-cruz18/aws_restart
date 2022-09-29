# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 18:56:15 2022

@author: Migue
"""

'''
Funcion que calcula el factorial de un numero
'''

def factorialCalculator(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    print(factorial)

