#mportando funcion de array
#del modulo array 
#como arr
from array import array as arr

#Archivo 
from s02t0102_1d import print_array

my_array = arr('i', [5, 10, 15, 20])

print("---- Antes de la inserción ----")
print_array(my_array)

#insercion 
my_array.insert(1, 90)
print("---- Después de la inserción ----")
print_array(my_array)

print("---- Después de un append ----")
my_array.append(1000)
print_array(my_array)

print("---- Simular un append con insert ----")
my_array.insert(len(my_array), 90000)
print_array(my_array)