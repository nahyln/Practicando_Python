
#Encontrar la suma máxima de números consecutivos dentro de una matriz unidimensional.

def kadane(a, length):

    n=a[0]
    act=a[0]

    for i in range(1, length):
        act = max(A[i], act + A[i])
        n = max(n, act)
    return n





