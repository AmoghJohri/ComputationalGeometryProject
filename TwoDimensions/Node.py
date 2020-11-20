from bintrees import AVLTree 
from Line     import Line

class Node:
    def __init__(self, interval, parent = None, leftChild = None, rightChild = None, height = None, root = AVLTree({})):
        self.interval    = interval 
        self.parent      = parent
        self.leftChild   = leftChild
        self.rightChild  = rightChild
        self.height      = height 
        self.root        = root

    def getTree(self):
        return self.root

    def addSegment(self, line):
        key = ((self.interval.getLeft()*line.getSlope() + line.getConstant()) + (self.interval.getRight()*line.getSlope() + line.getConstant()))/2.
        self.root.insert(key, line)

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
