class Node:
    def __init__(self, interval, parent = None, leftChild = None, rightChild = None, height = None, intervalArr = None):
        self.interval = interval 
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.height = height
        self.intervalArr = intervalArr

    def getInterval(self):
        return self.interval 

    def getIntervalArr(self):
        return self.intervalArr

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

    def setIntervalArr(self, intervalArr):
        self.intervalArr = intervalArr
