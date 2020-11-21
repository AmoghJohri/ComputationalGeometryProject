import time
import random
import progressbar
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

def randomTest(n):
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
    acc = 0.
    bruteTime = []
    segmentTime = []
    for each in queryArr:
        start_time = time.time()
        a = segSearch(root, each)
        segmentTime.append(time.time() - start_time)
        start_time = time.time()
        b = bruteForce(arr, each)
        bruteTime.append(time.time() - start_time)
        if compare_list_of_lists(a, b):
            acc += 1.
        else:
            print("Query: " + str(each))
            print("Intervals: " + str(arr))
    return [(acc/queryNum)*100, sum(bruteTime), sum(segmentTime)]

if __name__ == "__main__":
    n = 20000
    err = 0
    bruteForceTime = []
    segmentTreeTime = []
    bar = progressbar.ProgressBar(maxval=n, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    print("Running " + str(n) + " Randomized Tests...")
    bar.start()
    for i in range(1, n, 50):
        bar.update(i+1)
        var = randomTest(i)
        acc = var[0]
        bruteTime = var[1]
        segmentTime = var[2]
        bruteForceTime.append(bruteTime)
        segmentTreeTime.append(segmentTime)
        if  acc != 100:
            print("Something Went Wrong!!!")
            err = 1
    bar.finish()
    if not err:
        print("Passed " + str(n) + " Tests Successfully!")
    plt.plot([1000 + i for i in range(0, n, 50)], bruteForceTime)
    plt.plot([i for i in range(1, n, 50)], segmentTreeTime)
    plt.legend(["Brute Force Time", "Segment Tree Time"], loc="upper left")
    plt.xlabel("Number of Intervals")
    plt.ylabel("Query Time (for 100 queries)")
    plt.title("Time Analysis")
    plt.show()