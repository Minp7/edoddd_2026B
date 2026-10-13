# Importando el modulo Arrays
#from array import array as arr
#from array import *
import array as arr

# Creacion de un arreglo
# i: Entero con signo
# I: Entero sin signo
# f: Numero decimal
# d: Numero decimal doble 
# u: Carácteres unicode
my_array = arr.array('i',[10,22,300,3,7,40,55,80,700,654,34])

# Busqueda de un elemento
num_to_search = 200

# Modificando un valor usando
# backet notation
my_array[7] = 200

try:
  print(f"Localizado {num_to_search}: {my_array.index(num_to_search)}")
except:
  print("⚠️ Numero no encontrado!!!")