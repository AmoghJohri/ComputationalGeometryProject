import sys
import copy
import operator
from Interval import Interval
from Node import Node

MIN = sys.float_info.min
MAX = sys.float_info.max
epsilon = 1e-4

def getElementaryIntervals(intervals, returnList = 0):
    arr         = []
    for each in intervals:
        arr.append((each[0]))
        arr.append((each[1]))
    arr = (sorted(arr))
    elementaryIntervals = []
    elementaryIntervals.append(Interval(MIN, arr[0]-epsilon))
    for i in range(0, len(arr)-1):
        if arr[i+1] == arr[i]:
            continue
        elementaryIntervals.append(Interval(arr[i], arr[i]))
        elementaryIntervals.append(Interval(arr[i]+epsilon, arr[i+1]-epsilon))
    elementaryIntervals.append(Interval(arr[-1], arr[-1]))
    elementaryIntervals.append(Interval(arr[-1]+epsilon, MAX))
    # returning a list of lists
    if returnList == 1:
        arr = []
        for each in elementaryIntervals:
            arr.append([each.getLeft(), each.getRight()])
        return arr
    return elementaryIntervals

def recursiveCreateSegmentTree(nodes):
    newNodes = []
    i = 0
    while i < len(nodes)-1:
        newNode = Node(Interval.union(nodes[i].getInterval(), \
                nodes[i+1].getInterval()), parent=None, \
                leftChild=copy.deepcopy(nodes[i]), rightChild=copy.deepcopy(nodes[i+1]), height=max(nodes[i].getHeight(), nodes[i+1].getHeight()) + 1)
        newNode.getLeftChild().setParent(copy.deepcopy(newNode))
        newNode.getRightChild().setParent(copy.deepcopy(newNode))
        newNodes.append(copy.deepcopy(newNode))
        i += 2
    if len(nodes) % 2 == 1:
            newNodes.append(copy.deepcopy(nodes[-1]))
    if len(newNodes) > 1:
        return recursiveCreateSegmentTree(newNodes)
    return newNodes[0]

def createSegmentTree(intervals):
    elemIntervals = getElementaryIntervals(intervals)
    nodes = []
    for each in elemIntervals:
        nodes.append(Node(each, height=0))   
    return recursiveCreateSegmentTree(nodes)

def searchForElemInterval(root, value):
    curr = root 
    while True:
        if curr.getLeftChild() != None:
            if Interval.liesOnInterval(curr.getLeftChild().getInterval(), value):
                curr = curr.getLeftChild()
                continue 
        if curr.getRightChild() != None:
            if Interval.liesOnInterval(curr.getRightChild().getInterval(), value):
                curr = curr.getRightChild()
                continue 
        if curr.getLeftChild() != None:
            if Interval.liesInInterval(curr.getLeftChild().getInterval(), value):
                curr = curr.getLeftChild()
                continue 
        if curr.getRightChild() != None:
            if Interval.liesInInterval(curr.getRightChild().getInterval(), value):
                curr = curr.getRightChild()
                continue 
        return curr

def query(root, value):
    out = []
    curr = root 
    while True:
        if len(curr.getIntervalArr()) > 0:
            out.extend(curr.getIntervalArr())
        if curr.getLeftChild() != None:
            if Interval.liesOnInterval(curr.getLeftChild().getInterval(), value):
                curr = curr.getLeftChild()
                continue 
        if curr.getRightChild() != None:
            if Interval.liesOnInterval(curr.getRightChild().getInterval(), value):
                curr = curr.getRightChild()
                continue 
        if curr.getLeftChild() != None:
            if Interval.liesInInterval(curr.getLeftChild().getInterval(), value):
                curr = curr.getLeftChild()
                continue 
        if curr.getRightChild() != None:
            if Interval.liesInInterval(curr.getRightChild().getInterval(), value):
                curr = curr.getRightChild()
                continue 
        return out

def attachIntervals(root, intervals):
    def attachInterval(curr, interval):
        if curr == None:
            return 
        else:
            if interval.contains(curr.getInterval()):  
                curr.addInterval(interval.getInterval())
            else:
                if curr.getLeftChild() != None:
                    if curr.getLeftChild().getInterval().overlaps(interval):
                        attachInterval(curr.getLeftChild(), interval)
                if curr.getRightChild() != None:
                    if curr.getRightChild().getInterval().overlaps(interval):
                        attachInterval(curr.getRightChild(), interval)
    for each in intervals:
        attachInterval(root, Interval(each[0], each[1]))
    return root

def BFS(root):
    q = []
    q.append(root)
    while q:
        curr = q.pop(0)
        if curr.getLeftChild() != None:
            q.append(curr.getLeftChild())
        if curr.getRightChild() != None:    
            q.append(curr.getRightChild())
        print("Interval: ", end="")
        curr.getInterval().print()
        print("Associated Intervals: ", end="")
        print(curr.getIntervalArr())
    
if __name__ == "__main__":
    intervals = [[54, 75], [26, 72], [35, 84], [0, 84], [82, 85]]
    root = createSegmentTree(intervals)
    root = attachIntervals(root, intervals)
    elemIntervals = getElementaryIntervals(intervals)
    for each in elemIntervals:
        each.print()
    print(query(root, 4.9))