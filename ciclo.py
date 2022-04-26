#recorrer arreglo en forma cíclica...

#donde: A es el arreglo a recorrer y N es la cantidad de ciclos...

def array_(A, N):
    temp = list()
    for i in range(0, N):
        last = A[len(A)-1]
        temp.append(last)
        for j in range(0, len(A)-1):
            temp.append(A[j])
        A = []
        A = temp
        temp = []
    return A
     
            



