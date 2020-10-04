def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


def binary_search(data, target): 
    first = 0
    last = len(data) - 1

    while first <= last:
        mid = (first + last)//2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            first =  mid + 1
        else:
            last = mid - 1
    return -1