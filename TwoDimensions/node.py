# importing modules
from avl          import AVL_Tree 
from treeInterval import TreeInterval
# this corresponds to a node in the segment tree
class Node:
    # initialization function
    def __init__(self, interval, parent = None, leftChild = None, rightChild = None, height = None, bst = AVL_Tree(), root = None):
        self.interval    = interval 
        self.parent      = parent
        self.leftChild   = leftChild
        self.rightChild  = rightChild
        self.height      = height 
        self.root        = root
        self.bst         = bst

    # getters
    def getTree(self):
        return self.root

    def getInterval(self):
        return self.interval 

    def getParent(self):
        return self.parent 
    
    def getLeftChild(self):
        return self.leftChild 
    
    def getRightChild(self):
        return self.rightChild 

    def getHeight(self):
        return self.height

    # setters
    def setParent(self, parent):
        self.parent = parent 

    def setLeftChild(self, leftChild):
        self.leftChild = leftChild 
    
    def setRightChild(self, rightChild):
        self.rightChild = rightChild
    
    def setInterval(self, interval):
        self.interval = interval

    # queries for a vertical line-segment in a node
    def query(self, x_value, interval):
        return self.bst.query(self.root, x_value, interval)

    # adds a segment to the node
    def addSegment(self, line):
        key = TreeInterval(line, self.interval) 
        self.root = self.bst.insert(self.root, key, line)