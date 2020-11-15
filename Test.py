import random
from SegmentTree import *
import matplotlib.pyplot as plt 

def equal_ignore_order(a, b):
    d = {}
    for each in a:
        d[tuple(each)] = 1
    for each in b:
        try:
            if d[tuple(each)] == 0:
                return False 
        except:
            return False 
    return True

def compare_list_of_lists(a, b):
    return equal_ignore_order(a, b) and equal_ignore_order(b, a)

def bruteForce(arr, query):
    out = []
    for each in arr:
        if query >= each[0] and query <= each[1]:
            out.append(each)
    return out

def segSearch(root, queryPoint):
    return query(root, queryPoint)

if __name__ == "__main__":
    n        = 7
    rangeMin = 0
    rangeMax = 100
    arr      = []
    queryNum = 100
    queryArr = [random.random()*rangeMax for i in range(queryNum)]
    i        = 0
    while i < n:
        var1 = random.randint(rangeMin, rangeMax)
        var2 = random.randint(rangeMin, rangeMax)
        arr.append([min(var1, var2), max(var1, var2)])
        i   += 1
    root     = createSegmentTree(arr)
    # print("Intervals: ", arr)
    acc = 0.
    for each in queryArr:
        a = segSearch(root, each)
        b = bruteForce(arr, each)
        if compare_list_of_lists(a, b):
            acc += 1.
        else:
            print(a)
            print(b)
    print("Accuracy: ", (acc/queryNum)*100., "%")
