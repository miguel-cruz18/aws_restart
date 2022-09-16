"""
Se estara creando un menu d desayuno donde se le dara la bienevenida
al cliente, se le pedira su palto se le confirmara y se le informara
el valor total de este plato que ha pedidio de desayuno
"""

#Se mostrara un mensaje de bienvenida
print("-"*100)
print('''Bienvenido al restaurante Desayuno 24/7
Una vez vea el menu me deja saber que plato desea''')
print("-"*100)

#Se le mostrara una lista de posibles huevos
print("""\nEscoja uno:
Huevos Fritos
Clara de Huevo
Huevos Reveultos
Huevo en Tortilla\n""")

tipoDeHuevo=input("Digame cual de estos desea, solo 1: ")

#Ahora se le preguntara por la proteina que desea
print('''\nPerfecto ahora observe las proteinas disponibles:
Jamon de Pavo
Jamon Virginia
Tocineta
Salchicha\n''')

tipoDeProteina=input("Digame cual de estos desea, solo 1: ")

#Ahora se le preguntara por el carbohidrato del plato
print('''\nPerfecto ahora observe los carbohidratos disponibles:
Pankakes
Waffles
Tostadas Francesas
Tostadas con mantequilla\n''')

tipoDeCarbohidrato=input("Digame cual de estos desea, solo 1: ")

#Se pedira por ultimo que desea tomar
print('''\nSuena muy bien y por ultimo que desea tomar:
Agua
Jugo
Cafe\n''')

bebida=input("Digame cual de estos desea, solo 1: ")

#Se repite la orden final con el valor monetario
print('''\nExcelente, su plato seria de {} con {} y {}, 
y de tomar seria {}. Tiene un total de $15'''.format(tipoDeHuevo,tipoDeCarbohidrato,tipoDeProteina,bebida))
