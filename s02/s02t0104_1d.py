#mportando funcion de array
#del modulo array 
#como arr
from array import array as arr

#Archivo 
from s02t0102_1d import print_array

my_array = arr('i', [5, 10, 15, 20, 10])

print("---- Antes de la eliminación ----")
print_array(my_array)

#eliminacion
try:
    my_array.remove(10)
except:
    print("El elemento no se encuentra en el arreglo")
print("---- Después de la eliminacion ----")
print_array(my_array)

