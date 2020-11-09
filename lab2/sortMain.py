from mergesort import mergesort
from insertionsort import insertionsort
from time import time
import random
import matplotlib.pyplot as plt


mergeTime = []
insertTime = []
i = 5000
dataSize = []
 
while i <= 100000:
    dataSize.append(i)
    dataM = random.sample(range(i), i)
    # dataI = dataM
    
    mergeStart = time()
    mergesort(dataM, 0, len(dataM) - 1)
    mergeEnd = time()
    mergeTime.append(mergeEnd - mergeStart)

    # insertStart = time()
    # insertionsort(dataI)
    # insertEnd = time()
    # insertTime.append(insertEnd - insertStart)
    
    i += 5000


print("Time taken:")
print("For merge sort: ", mergeTime)
# print("For insertion sort: ", insertTime)


plt.plot(dataSize,mergeTime,"g")
plt.show()

# plt.plot(dataSize,insertTime,"r")
# plt.show()
