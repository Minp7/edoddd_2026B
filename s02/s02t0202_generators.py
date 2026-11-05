"""
generators

los generadores son funciones que pueden
pausar en ejecucion

cuando se invoca un funcion generadora
devuelve un objeto generador (aka iterador)

el codigo dentro de la funcion no se ejecuta 
de imediato, solo se compila.

la funcion se ejecuta unicamente cuando
iteras sobre el generador

"""

def my_generador():
   yield 1
   yield 2
   yield 3
   yield 4
   yield 5
   yield 6
   yield 7

#se invoca funcion generadora 
my_iterador = my_generador()

#se itera manualmente sobre el generador 
# print(next(my_iterador))#imprime 1 
# print(next(my_iterador))#imprime 2
# print(next(my_iterador))#imprime 3 
# print(next(my_iterador))#imprime 4 

#los iteradores se mpueden iterar con un for
for value in my_iterador:
   print(value)
