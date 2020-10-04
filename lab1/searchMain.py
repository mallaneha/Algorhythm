from search import linear_search
from search import binary_search
from time import time

import random
import matplotlib.pyplot as plt

def partition(arr, low, high): 
    i = (low - 1) 
    pivot = arr[high]    
  
    for j in range(low , high): 
        if arr[j] <= pivot: 
            i = i + 1 
            arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return i+1
 
def quickSort(arr, low, high): 
    if low < high: 
        q = partition(arr, low, high) 
        quickSort(arr, low, q - 1) 
        quickSort(arr, q + 1, high) 

linearBest = []
linearWorst = []
binaryBest = []
binaryWorst = []

i = 10000
dataSize = []
 
while i <= 100000:
    dataSize.append(i)
    data = random.sample(range(i), i)
    
    start = time()
    indexLB = linear_search(data, data[0])
    end = time()
    linearBest.append(end - start)
    
    start = time()
    indexLW = linear_search(data, data[-1])
    end = time()
    linearWorst.append(end - start)
    
    quickSort(data, 0, len(data) - 1) #sorted(data)
    
    start = time()
    indexBB = binary_search(data, data[(len(data) - 1)//2])
    end = time()
    binaryBest.append(end - start)
    
    start = time()
    indexBW = binary_search(data, data[-1])
    end = time()
    binaryWorst.append(end - start)
    
    i += 10000
    
print(indexLB)
print(indexLW)
print(indexBB)
print(indexBW)

print(linearBest)
print(linearWorst)
print(binaryBest)
print(binaryWorst)


plt.plot(dataSize,linearBest,"g")
plt.show()

plt.plot(dataSize,linearWorst,"r")
plt.show()

plt.plot(dataSize,binaryBest,"g")
plt.show()

plt.plot(dataSize,binaryWorst,"r")
plt.show()
