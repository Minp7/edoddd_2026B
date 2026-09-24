"""
escribir un programa que calcule
 la suma de los "n" numeros naturales.
Por ejemplo si n = 100, el programa
calculara la suma del 1 al 100
42
"""
# importamos biblioteca time
import time

# Funcion k suma los  
# primeros "n" numeros naturales 
def sum_of_n(n):
    total_sum = 0
    
    #Sumando los "n" numeros 
    #ciclo for
    for number in range(1,n+1):
      total_sum = total_sum + number
      #Retornando el total de la suma 
      return total_sum 
   # variable para gaurdar 
   # el data set 
    
    dataset =[]#[(n,time,sum),()]
    #generando el contenido del data set 
    for repetition in range(1,11):
      #Tomo el tiempo 
      #creando una marca de tiempo
      timestamp_01 = time.time()
      #suma de los n numeros 
      n = repetition*500 
      #Guardo el resultado en results 
      result = sum_of_n(n)


     #tomando el tiempo final
    timestamp_02 = time.time()

     #Calculando el tiempo 
    elapsed_time= round ((timestamp_02-timestamp_01) * 1e6,2) 
   
     #Agregar la tripleta de los 
     #datos a dataset 
    dataset.append((n,elapsed_time,result))
   #imprimir dataset 
   #imprimir el dataset
for tup in dataset:
   print(tup)





