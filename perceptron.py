import numpy as np
import matplotlib.pyplot as plt
import sys as ss

class perceptron:
    #método para calcular los pesos
    def __init__(self, n):
        self.w = np.random.randn(n)
        self.n = n
    #método de propagación:suma del producto punto de cada valor por su peso correspondiente
    def prop(self, e):
        self.s = 1*(self.w.dot(e) > 0)
        self.e = e
    #método de actualización: dada la regla de entrenamiento = wi<-wi+(a*(yd-y)*xi) donde a es el ritmo de aprendizaje
    def upd(self, a, sd):
        for i in range(0, self.n):
            self.w[i]=self.w[i]+a*(sd-self.s)*self.e[i]
    #todo        
    #definir funcion para probar el aprendizaje
            
#entrenar para función lógica (ejemplos aqui)
#tabla AND
tabla_logica = np.array([[0,0,0,0],[0,0,1,0],[0,1,0,0],[0,1,1,0],[1,0,0,0],[1,0,1,0],[1,1,0,0],[1,1,1,1]])

#el argumento debe ser igual a los valores de entrada (para n argumentos dentro de cada objeto del arreglo: n-1, porque el último es la salida)
perceptron_fnl = perceptron(len(tabla_logica[0])-1)

#acumulador de los valores de los pesos actualizados
act_w = [perceptron_fnl.w]

#factor de aprendizaje
a = 0.21

#rango de épocas a recorrer con el metodo de propagación
for ep in range(0,100):
    for i in range(0, perceptron_fnl.n+1):
        perceptron_fnl.prop(tabla_logica[i,0:perceptron_fnl.n])
        perceptron_fnl.upd(a, tabla_logica[i,perceptron_fnl.n])
        act_w = np.concatenate((act_w, [perceptron_fnl.w]), axis = 0)

#exportar a un archivo de texto los resultados
ss.stdout=open("out.txt","w")
print("Pesos: \n",perceptron_fnl.w)
print("Curva de aprendizaje del perceptrón: \n", act_w)
ss.stdout.close()     

#dibujar el gráfico con los valores acumulados
for z in range(0, perceptron_fnl.n):
    plt.plot(act_w[:,[z]])

#mostrar gráfico de aprendizaje
plt.show()




