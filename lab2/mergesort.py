import math


def mergesort(array, p, r):
    if p < r:
        q = math.floor((p + r)/2)
        mergesort(array, p, q)
        mergesort(array, q + 1, r)
        merge(array, p, q, r)


def merge(array, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [] 
    R = []

    for i in range(n1):
        L.append(array[p+i])
    
    for j in range(n2):
        R.append(array[q+j+1])
    
    L.append(math.inf)
    R.append(math.inf)

    i, j = 0, 0

    for k in range(p, r + 1):
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
