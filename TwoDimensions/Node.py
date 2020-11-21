from AVL import AVL_Tree 
from Line     import Line
from treeInterval import TreeInterval

class Node:
    def __init__(self, interval, parent = None, leftChild = None, rightChild = None, height = None, bst = AVL_Tree(), root = None):
        self.interval    = interval 
        self.parent      = parent
        self.leftChild   = leftChild
        self.rightChild  = rightChild
        self.height      = height 
        self.root        = root
        self.bst         = bst

    def getTree(self):
        return self.root

    def query(self, interval):
        return self.bst.query(self.root, interval)

    def addSegment(self, line):
        key = TreeInterval(((self.interval.getLeft()*line.getSlope() + line.getConstant()),  (self.interval.getRight()*line.getSlope() + line.getConstant())))
        self.root = self.bst.insert(self.root, key, line)

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

    def setParent(self, parent):
        self.parent = parent 

    def setLeftChild(self, leftChild):
        self.leftChild = leftChild 
    
    def setRightChild(self, rightChild):
        self.rightChild = rightChild
    
    def setInterval(self, interval):
        self.interval = interval