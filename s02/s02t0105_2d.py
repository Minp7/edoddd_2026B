
from array import array as arr

#impresion de un atabla 
def print_table(table):
    #Imprimiendo cada elemnto 
    for row in table:
        for column in row:
            print(column, end=",")
        print("\b ") 

table = [
    arr('i', [1,2,3]),
    arr('i', [4,5,6]),
    arr('i', [7,8,9]),
]

print_table(table)

#Insercion
row = 1 
column = 2
value = 99

#Insertar en la fila 1 columna 2 el valor 99
table[row].insert(column, value)

#Imprimiendo msj 
print("---- Después de la inserción del elemento ----")
print_table(table) #DRY (don't repeat yourself)

#Insertndo una fila completa
new_row = arr('i', [100, 200, 300])
pos = 1
table.insert(pos, new_row)

#Imprimiendo msj 
print("---- Después de la inserción de fila ----")
print_table(table) #DRY (don't repeat yourself)

#Elimicacion de elemnetos 
del table[2]

#Imprimiendo msj 
print("---- Después de la eliminación de fila ----")
print_table(table) #DRY (don't repeat yourself)