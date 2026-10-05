"""
escribir un programa que calcule
 la suma de los "n" numeros naturales.
Por ejemplo si n = 100, el programa
calculara la suma del 1 al 100
42 usando ciclo while
"""
#importar la biblioteca del tiempo 
import time

#Crear la variable para
# el problema 
n = 100 
the_sum = 0

#tomando el tiempo 1 
timestamp_01 = time.time()

#iniciando la suma 
#100
while(n > 0):
    the_sum = the_sum + n #100 + 99 + 98
    n = n - 1

    #tomando el t2
timestamp_02 =time.time()

#imprimimos la solucion 
print(f"La suma es {the_sum}")

#Calculando el tiempo 
elapsed_time = round ((timestamp_02-timestamp_01) * 1e6,2)
print(f"Tiempo de ejecucion: {elapsed_time}us")