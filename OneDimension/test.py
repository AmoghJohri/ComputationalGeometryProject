# importing standard libraries
import time
import random
import progressbar
import matplotlib.pyplot as plt 
# importing modules
from   segmentTree import *

# function to determine whether a contains all elements of b
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

# function to determine whether two list of intervals are identical
def compare_list_of_lists(a, b):
    return equal_ignore_order(a, b) and equal_ignore_order(b, a)

# function for brute force query
def bruteForce(arr, query):
    out = []
    for each in arr:
        if query >= each[0] and query <= each[1]:
            out.append(each)
    return out

# function for efficient query using segment tree
def segSearch(root, queryPoint):
    return query(root, queryPoint)

# function to generate random-tests
def randomTest(n):
    rangeMin = 0        # min x-value in an interval
    rangeMax = 100      # max x-value in an interval
    queryNum = 100      # number of queries
    # generating random query points
    queryArr = [random.random()*rangeMax for i in range(queryNum)] 
    arr      = []       # generating input set
    i        = 0
    while i < n:
        var1 = random.randint(rangeMin, rangeMax)
        var2 = random.randint(rangeMin, rangeMax)
        arr.append([min(var1, var2), max(var1, var2)])
        i   += 1
    # creating the segment tree
    root        = createSegmentTree(arr)
    acc         = 0. # to determine the accuracy of efficient algorithm
    bruteTime   = [] # stores the time takes by brute force for each query
    segmentTime = [] # stores the time taken by efficient algo. for each query
    # running for all queries
    for each in queryArr:
        # using the efficient algorithm
        start_time  = time.time()
        a           = segSearch(root, each)
        segmentTime.append(time.time() - start_time)
        # using brute force
        start_time  = time.time()
        b           = bruteForce(arr, each)
        bruteTime.append(time.time() - start_time)
        # comparing the results
        if compare_list_of_lists(a, b):
            acc += 1.
        # if the results do not match
        else:
            print("Query: " + str(each))
            print("Intervals: " + str(arr))
    # returns the stats
    return [(acc/queryNum)*100, sum(bruteTime), sum(segmentTime)]

if __name__ == "__main__":
    n               = 20000 # number of different tests
    err             = 0     # number of errors
    bruteForceTime  = []    # storing the time stats
    segmentTreeTime = []    # storing the time stats
    # instantiating the progress bar
    bar             = progressbar.ProgressBar(maxval=n, \
    widgets         = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    print("Running " + str(n) + " Randomized Tests...")
    bar.start()
    # runnning for values of n
    for i in range(1, n, 50):
        bar.update(i+1)
        var         = randomTest(i)
        acc         = var[0]
        bruteTime   = var[1]
        segmentTime = var[2]
        bruteForceTime.append(bruteTime)
        segmentTreeTime.append(segmentTime)
        # if the results for 100 queries do not match
        if  acc != 100:
            print("Something Went Wrong!!!")
            err = 1
    bar.finish()
    # if there were no errors
    if not err:
        print("Passed " + str(n) + " Tests Successfully!")
    # plotting the time values
    plt.plot([i for i in range(0, n, 50)], bruteForceTime)
    plt.plot([i for i in range(1, n, 50)], segmentTreeTime)
    plt.legend(["Brute Force Time", "Segment Tree Time"], loc="upper left")
    plt.xlabel("Number of Intervals")
    plt.ylabel("Query Time (for 100 queries)")
    plt.title("Time Analysis")
    plt.show()