#Método de Lange para determinar la capacidad óptima de producción de una planta.

#Definir un arreglo con los costos de producción.
#Definir una variable que represente la inversión inicial.
#Definir una variable que represente el porcentaje de descuento.
#Definir una variable que represente la cantidad de períodos a evaluar.

import math

def Lange(ini, cp, i, t):
    sigma = 0
    for z in range(0, t):
        sigma += math.ceil(cp[z]/pow((1+i),z+1))
    total = ini + sigma
    return total

#donde:
#ini: valor entero correspondiente a la inversión inicial. (ej: n = 100)
#cp: arreglo contentivo de los costos de producción por año. (ej: a = [10,20,30,40])
#i: valor correspondiente al porcentaje. (ej: x = 0.10)
#t: valor correspondiente a los años que serán evaluados. (ej: w = 6)

#el valor de t debe ser igual a la cantidad de elementos en cp, dada la relación entre los costos por año y la cantidad de años.

#todo: mejorar redondeo.

