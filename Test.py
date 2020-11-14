import time
import random
from SegmentTree import *
import matplotlib.pyplot as plt 

def equal_ignore_order(a, b):
    d = {}
    for each in a:
        d[tuple(each)] = 1
    for each in b:
        try:
            if d[each] == 0:
                return False 
        except:
            return False 
    return True

def bruteForce(arr, query):
    out = []
    for each in arr:
        if query >= each[0] and query <= each[1]:
            out.append(each)
    return out

def segSearch(root, queryPoint):
    return query(root, queryPoint)

if __name__ == "__main__":
    n = 50
    rangeMin = 0
    rangeMax = 100
    arr = []
    queryNum = 100
    queryArr = [random.random()*rangeMax for i in range(queryNum)]
    i = 0
    while i < n:
        var1 = random.randint(rangeMin, rangeMax)
        var2 = random.randint(rangeMin, rangeMax)
        arr.append([min(var1, var2), max(var1, var2)])
        i += 1
    root = createSegmentTree(arr)
    root = attachIntervals(root, arr)
    # print("Intervals: ", arr)
    time_analysis_brute = []
    time_analysis_seg = []
    for each in queryArr:
        s = time.time()
        b = segSearch(root, each)
        time_analysis_seg.append(time.time() - s)
        s = time.time()
        b = bruteForce(arr, each)
        time_analysis_brute.append(time.time() - s)
    i = 1
    while i < queryNum:
        time_analysis_seg[i] = time_analysis_seg[i-1] + time_analysis_seg[i]
        time_analysis_brute[i] = time_analysis_brute[i-1] + time_analysis_brute[i]
        i += 1
    plt.plot([i for i in range(1, queryNum+1)], time_analysis_brute)
    plt.plot([i for i in range(1, queryNum+1)], time_analysis_seg)
    plt.legend(["Brute Force", "Segment Tree"])
    plt.ylabel("Time Taken")
    plt.xlabel("Number of Queries")
    plt.title("Time Analysis")
    plt.grid()
    plt.plot()
    plt.show()