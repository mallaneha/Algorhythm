from mergesort import mergesort
from time import time
import random
import matplotlib.pyplot as plt


mergeTime = []
i = 100000
dataSize = []
 
while i <= 1000000:
    dataSize.append(i)
    data = random.sample(range(i), i)
    
    start = time()
    mergesort(data, 0, len(data) - 1)
    end = time()
    mergeTime.append(end - start)
    
    i += 100000


print(mergeTime)


plt.plot(dataSize,mergeTime,"g")
plt.show()
