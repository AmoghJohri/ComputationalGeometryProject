# importing standard libraries
import sys
import copy
# import modules
from   node     import Node
from   interval import Interval

MIN     = sys.float_info.min # for negative infinity
MAX     = sys.float_info.max # for infinity
epsilon = 1e-9               # to perturb points

# takes the input intervals, and returns the elementary intervals
def getElementaryIntervals(intervals, returnList = 0):
    # array to store all the end points of the interval
    arr         = []
    # adding all the end points of the intervals
    for each in intervals:
        arr.append((each[0]))
        arr.append((each[1]))
    # sorting the array with all the end points
    arr                 = (sorted(arr))
    # array to store all the elementary intervals
    elementaryIntervals = []
    # adding all the elementary intervals
    elementaryIntervals.append(Interval(MIN, arr[0]-epsilon))
    for i in range(0, len(arr)-1):
        # skipping over duplicate values
        if arr[i+1] == arr[i]:
            continue
        elementaryIntervals.append(Interval(arr[i], arr[i]))
        elementaryIntervals.append(Interval(arr[i]+epsilon, arr[i+1]-epsilon))
    elementaryIntervals.append(Interval(arr[-1], arr[-1]))
    elementaryIntervals.append(Interval(arr[-1]+epsilon, MAX))
    # for when the return value needs to be a list
    if returnList == 1:
        arr = []
        for each in elementaryIntervals:
            arr.append([each.getLeft(), each.getRight()])
        return arr
    # returning the list of elementary intervals
    return elementaryIntervals

# recursively creates the segment tree (bottom to top)
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

# creates the segement tree for the input intervals
def createSegmentTree(intervals):
    # getting all the elementary intervals
    elemIntervals = getElementaryIntervals(intervals)
    # all the nodes corresponding to the elementary intervals
    nodes         = [Node(each, height=0) for each in elemIntervals] 
    # recursively generate the segment tree
    root          = recursiveCreateSegmentTree(nodes)
    # attach all the intervals
    return attachIntervals(root, intervals)

# attaching the intervals to the correct nodes (for O(nlog(n)) space complexity)
def attachIntervals(root, intervals):
    # attaching an interval to segment tree
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

# querying for a point
def query(root, value):
    out  = []   # placeholder to store all the intervals which contain the query point
    curr = root 
    while True:
        # check whether the current node has intervals corresponding to it, if yes, then add those
        if len(curr.getIntervalArr()) > 0:
            out.extend(curr.getIntervalArr())
        if curr.getLeftChild() != None:
            # checks whether to move towards the left
            if Interval.liesOnInterval(curr.getLeftChild().getInterval(), value) or Interval.liesInInterval(curr.getLeftChild().getInterval(), value):
                curr = curr.getLeftChild()
                continue 
        if curr.getRightChild() != None:
            # checks whether to move towards the right
            if Interval.liesOnInterval(curr.getRightChild().getInterval(), value) or Interval.liesInInterval(curr.getRightChild().getInterval(), value):
                curr = curr.getRightChild()
                continue 
        # returns the list of intervals
        return out

# Does a level-order traversal of the segment tree
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
    print(query(root, 85))