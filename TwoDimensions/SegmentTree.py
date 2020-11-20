import sys
import copy
from bintrees import AVLTree 

from Node     import Node
from Line     import Line 
from Point    import Point
from Interval import Interval

MIN     = sys.float_info.min
MAX     = sys.float_info.max
epsilon = 1e-9 # to perturb points

def getPoints(intervals):
    arr         = []
    # adding all the end points of the intervals
    for each in intervals:
        l = Line((each[0][0], each[1][0]), (each[0][1], each[1][1]))
        arr.append(Point(each[0][0], each[0][1], line=l))
        arr.append(Point(each[1][0], each[1][1], line=l))
    return arr

def getLineSegments(intervals):
    arr = []
    for each in intervals:
        arr.append(Line((each[0][0], each[1][0]), (each[0][1], each[1][1])))
    return arr

def getElementaryIntervals(intervals, returnList = 0):
    arr = getPoints(intervals)
    # sorting the array with all the end points
    arr                 = (sorted(arr, key = lambda x : x.getX()))
    arr_                = [each.getX() for each in arr]
    # array to store all the elementary intervals
    elementaryIntervals = []
    # adding all the elementary intervals
    elementaryIntervals.append(Interval(MIN, arr_[0]-epsilon))
    for i in range(0, len(arr_)-1):
        # skipping over duplicate values
        if arr_[i+1] == arr_[i]:
            continue
        elementaryIntervals.append(Interval(arr_[i], arr_[i]))
        elementaryIntervals.append(Interval(arr_[i]+epsilon, arr_[i+1]-epsilon))
    elementaryIntervals.append(Interval(arr_[-1], arr_[-1]))
    elementaryIntervals.append(Interval(arr_[-1]+epsilon, MAX))
    # for when the return value needs to be a list
    if returnList == 1:
        arr_ = []
        for each in elementaryIntervals:
            arr_.append([each.getLeft(), each.getRight()])
        return arr_
    # returning the list of elementary intervals
    return elementaryIntervals

def recursiveCreateSegmentTree(nodes):
    # these shall contain the new nodes that are added
    newNodes = []
    i = 0
    # going through all the nodes at the current level
    while i < len(nodes)-1:
        # combining two adjacent intervals into one interval for the parent node
        newNode = Node(Interval.union(nodes[i].getInterval(), \
                nodes[i+1].getInterval()), parent=None, \
                leftChild=copy.deepcopy(nodes[i]), rightChild=copy.deepcopy(nodes[i+1]), height=max(nodes[i].getHeight(), nodes[i+1].getHeight()) + 1)
        # adding the parent information for the child nodes
        newNode.getLeftChild().setParent((newNode))
        newNode.getRightChild().setParent((newNode))
        # appending the new node
        newNodes.append((newNode))
        i += 2
    # adding any unpaired nodes
    if len(nodes) % 2 == 1:
            newNodes.append((nodes[-1]))
    # if the length of nodes at this level is > 1, recursive call to the same function
    if len(newNodes) > 1:
        return recursiveCreateSegmentTree(newNodes)
    # returning the root node
    return newNodes[0]

def createSegmentTree(intervals):
    # getting all the elementary intervals
    elemIntervals = getElementaryIntervals(intervals)
    # all the nodes corresponding to the elementary intervals
    nodes         = [Node(each, height=0) for each in elemIntervals] 
    # recursively generate the segment tree
    root          = recursiveCreateSegmentTree(nodes)
    # attach all the intervals
    segments = getLineSegments(intervals)
    return attachIntervals(root, segments)

def attachIntervals(root, segments):
    # attaching an interval to segment tree
    def attachInterval(curr, segment):
        if curr == None:
            return 
        else:
            interval = Interval(segment.getLeftPoint(), segment.getRightPoint())
            if interval.contains(curr.getInterval()):  
                curr.addSegment(segment)
            else:
                if curr.getLeftChild() != None:
                    if curr.getLeftChild().getInterval().overlaps(interval):
                        attachInterval(curr.getLeftChild(), segment)
                if curr.getRightChild() != None:
                    if curr.getRightChild().getInterval().overlaps(interval):
                        attachInterval(curr.getRightChild(), segment)
    for each in segments:
        attachInterval(root, each)
    return root

def query(root, query):
    out  = []
    curr = root 
    x_value = query[0]
    interval = query[1]
    while True:
        if not curr.getTree().is_empty():
            out.extend(curr.getTree()[interval[0]:interval[1]].values())
        if curr.getLeftChild() != None:
            if Interval.liesOnInterval(curr.getLeftChild().getInterval(), x_value):
                curr = curr.getLeftChild()
                continue 
        if curr.getRightChild() != None:
            if Interval.liesOnInterval(curr.getRightChild().getInterval(), x_value):
                curr = curr.getRightChild()
                continue 
        if curr.getLeftChild() != None:
            if Interval.liesInInterval(curr.getLeftChild().getInterval(), x_value):
                curr = curr.getLeftChild()
                continue 
        if curr.getRightChild() != None:
            if Interval.liesInInterval(curr.getRightChild().getInterval(), x_value):
                curr = curr.getRightChild()
                continue 
        return out

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
        print(curr.getTree())
    
if __name__ == "__main__":
    intervals = [[(1.,1.), (4.,5.)], [(3.,1.), (4.,3.)], \
                [(4.,4.), (6.,2.)], [(5.,5.), (7.,3.)], \
                [(1.,5.), (6.,6.)], [(4.,7.), (5.,6.)], \
                [(2.,6.), (5.,8.)]]
    root = createSegmentTree(intervals)
    q = (3, (1, 8))
    out = query(root, q)
    for each in out:
        each.print()