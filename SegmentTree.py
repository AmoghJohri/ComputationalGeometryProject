import sys
import operator
from Interval import Interval
from Node import Node

MIN = sys.float_info.min
MAX = sys.float_info.max
epsilon = 1e-7

def getElementaryIntervals(intervals, returnList = 0):
    arr         = []
    intervalsFirst = sorted(intervals, key = operator.itemgetter(0))
    for each in intervals:
        arr.append(each[0])
        arr.append(each[1])
    arr = list(set(sorted(arr)))
    elementaryIntervals = []
    elementaryIntervals.append(Interval(MIN, arr[0]))
    for i in range(0, len(arr)-1):
        elementaryIntervals.append(Interval(arr[i], arr[i]))
        elementaryIntervals.append(Interval(arr[i]+epsilon, arr[i+1]-epsilon))
    elementaryIntervals.append(Interval(arr[-1], MAX))
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
                leftChild=nodes[i], rightChild=nodes[i+1], height=max(nodes[i].getHeight(), nodes[i+1].getHeight()) + 1)
        newNode.getLeftChild().setParent(newNode)
        newNode.getRightChild().setParent(newNode)
        newNodes.append(newNode)
        i += 2
    if len(nodes) % 2 == 1:
        newNode = Node(nodes[-1].getInterval(), parent=None, \
                  leftChild=nodes[-1], rightChild=nodes[-1], height=nodes[-1].getHeight() + 1)
        newNode.getLeftChild().setParent(newNode)
        newNode.getRightChild().setParent(newNode)
        newNodes.append(newNode)
        # newNodes.append(nodes[-1]) : becomes harder to pretty print

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

# auxillary functions
def prettyPrint(node):
    queue = []
    queue.append(node)
    curr = 0
    while queue:
        currNode = queue.pop(0)
        if currNode.getLeftChild() != None:
            queue.append(currNode.getLeftChild())
        if currNode.getRightChild() != None:
            queue.append(currNode.getRightChild())
        if currNode.getHeight() == curr:
            for i in range(curr):
                print("\t",end='')
        else:
            print("\n")
            curr = currNode.getHeight() 
            for i in range(curr+1):
                print("\t",end='')
        print(str(currNode.getInterval().getInterval()), end='')
    print("\n")
    
if __name__ == "__main__":
    intervals = [[1., 3.], [2., 5.], [1., 6.]] 
    elemIntervals = getElementaryIntervals(intervals)
    root = createSegmentTree(intervals)
    print(searchForElemInterval(root, 2.5).getInterval().getInterval())