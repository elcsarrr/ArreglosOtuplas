"""
Una tupla o arreglo es una estructura de datos propia de python que permite almacenar distinto valores, son inmutables:no  cambian una vez inicializadas
"""

tupla = (1, 2, 3)
print (tupla)
tupla2 = (7, "oscar", True, 450.1, 16 + 7j, "felicidad", False)
print (tupla2)
tupla3 = (9, 3, (4, 5, 6))
print (tupla3)
print(tupla2[1])
# tupla2[1] = "asdwdasd" no se puede asignar
c=tupla[1]*2
print (c) # pero si puedo asignar si hago un cambio como multiplicar etc

print(tupla2[-1])# Acceder añ ultimo elemento
print(tupla2[0:4]) # va a tomar los elementos desde la pocicion 0 hasta la 4
print(tupla2[-2])# imprime lo penultimo contando desde final al principio

a, b, c = tupla
print(a)
print(b)
print(c)

tuplaFinal = tupla + tupla3
print (tuplaFinal)

print (tuplaFinal.count(3)) # cuenta cuantas veces hay un 3 por el count
print (tuplaFinal.index(3)) # cuenta desde el 0 en que posicion esta el 3 