lst = [ 5, 4, 3, 2]

def swap(list1, x, y):
    temp = list1[x]
    list1[x] = list1[y]
    list1[y] = temp


print(lst)


def sort(list1):
    for y in range(len(list1) - 1):
        for i in range(len(list1) - 1 - y):
            if list1[i + 1] < list1[i]:
                swap(list1, i, i + 1)

sort(lst)

def sort2(list1):
    if len(list1) in [0,1]:
        return list1
    if len(list1) == 2:
        if list1[1] < list1[0]:
            swap(list1, 0, 1)
        return list1
    pivot = list1[0]
    smaller = []
    bigger = []
    for i in range(1, len(list1)):
        if list1[i] > pivot:
            bigger.append(list1[i])
        else:
            smaller.append(list1[i])
    smaller = sort2(smaller)
    bigger = sort2(bigger)
    pivot = [pivot]
    new_list = smaller + pivot + bigger
    return new_list


print(lst)


def generateList(n):
    import random
    empty_list = []
    for i in range(n):
        num = random.randint(0, 1000000)
        empty_list.append(num)
    return empty_list

generatedList = generateList(10000)
# print(generatedList)

import time
startTime = time.time()
#sort(generatedList)
generatedList = sort2(generatedList)
endTime = time.time()
totalTime = endTime - startTime
# print(generatedList)
print(totalTime)


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

fibnow = fib(5)
print(fibnow)
