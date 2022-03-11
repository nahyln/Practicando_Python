
def bin_(n,z):
    l = 0 #límite inferior
    h = len(n)-1 #longitud del arreglo como límite superior inicial
    m = 0 #punto medio
    #ordenar arreglo:
    n.sort()
    while(True):
        m = round(l+((h-l)/2)) #fórmula para calcular el punto medio
        if(n[m] == z):
            return 1
        if(n[m] < z): #si punto medio es menor al número buscado, se suma 1 para mover la zona de búsqueda hacia la derecha
            l = m + 1
        if(n[m] > z): #si punto medio es menor al número buscado, se resta 1 para mover la zona de búsqueda hacia la izquierda
            h = m - 1     
        if(l > h): 
            return 0
          
        

#donde A: un arreglo de números enteros.
# B = número entero a buscar en el arreglo.

#bin_(A,B)
