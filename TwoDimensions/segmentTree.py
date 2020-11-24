# importing standard libraries
import sys
import copy
# importing modules
from node     import Node
from line     import Line 
from point    import Point
from interval import Interval

MIN     = -1* sys.float_info.max # for negative infinity
MAX     = sys.float_info.max     # for infinity
epsilon = 1e-9                   # to perturb points

# get the points from the intervals containing end-points
def getPoints(intervals):
    arr         = []
    # adding all the end points of the intervals
    for each in intervals:
        l = Line((each[0][0], each[1][0]), (each[0][1], each[1][1]))
        arr.append(Point(each[0][0], each[0][1], line=l))
        arr.append(Point(each[1][0], each[1][1], line=l))
    return arr

# get line segments from the intervals containing end-points
def getLineSegments(intervals):
    arr = []
    for each in intervals:
        arr.append(Line((each[0][0], each[1][0]), (each[0][1], each[1][1])))
    return arr

# get all elementary intervals
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

# recursively creates the segment tree
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

# creates the segment tree for a list of intervals
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

# attaches the intervals to the segment tree
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

# querying for a point
def query(root, query, visualize = 0):
    out      = [] # placeholder to store all the intervals which contain the query point
    vis_arr  = [] # for visualizing the search
    curr     = root 
    x_value  = query[0]
    interval = query[1]
    while True:
        # check whether the current node has intervals corresponding to it, if yes, then add those
        out.extend(curr.query(x_value, interval))
        if visualize:
            if len(curr.query(x_value, interval)):
                vis_arr.append(copy.deepcopy(curr))
        if curr.getLeftChild() != None:
            # checks whether to move towards the left
            if Interval.liesOnInterval(curr.getLeftChild().getInterval(), x_value) or Interval.liesInInterval(curr.getLeftChild().getInterval(), x_value):
                curr = curr.getLeftChild()
                continue 
        if curr.getRightChild() != None:
            # checks whether to move towards the right
            if Interval.liesOnInterval(curr.getRightChild().getInterval(), x_value) or Interval.liesInInterval(curr.getRightChild().getInterval(), x_value):
                curr = curr.getRightChild()
                continue 
        # returns the list of intervals or nodes
        if visualize:
            return vis_arr
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
        print(curr.getTree())
    
if __name__ == "__main__":
    # intervals = [[(1.,1.), (7.,5.)], [(3.,2.), (4.,1.)], \
    #             [(4.,2.), (6.,3.)], [(5.,3.), (7.,4.)], \
    #             [(1.,2.), (2.,4.)], [(1.,6.), (3.,3.)], \
    #             [(2.,5.), (4.,7.)], [(3.,5.), (5.,4.)], \
    #             [(4.,5.), (6.,6.)], [(4.,8.), (5.,7.)]]
    intervals = [[(160, 200), (460, 80)], [(360, 180), (500, 280)], [(260, 240), (420, 120)]]
    root = createSegmentTree(intervals)
    q = [420, [40, 120]]
    print("Query: " + str(q))
    out = query(root, q)
    for each in out:
        each.print()