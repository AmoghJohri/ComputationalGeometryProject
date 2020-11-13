class Interval:
    def __init__(self, left, right, intervalArr = None):
        self.left = left 
        self.right = right
        self.mid = (right + left)/2
        self.intervalArr = intervalArr
    
    def getLeft(self):
        return self.left 
    
    def getRight(self):
        return self.right

    def getMid(self):
        return self.mid

    def getIntervalArr(self):
        return self.intervalArr

    def getInterval(self):
        return [self.left, self.right]

    def setIntervalArr(self, intervalArr):
        self.intervalArr = intervalArr

    def print(self):
        print([self.left, self.right])

    @staticmethod
    def union(I1, I2):
        return Interval(min(I1.getLeft(), I2.getLeft()), max(I1.getRight(), I2.getRight()))

    @staticmethod
    def liesInInterval(I, val):
        if (val - I.getLeft()) * (I.getRight() - val) > 0:
            return True 
        return False 

    @staticmethod
    def liesOnInterval(I, val):
        if val == I.getLeft() or val == I.getRight():
            return True 
        return False 

    @staticmethod 
    def intersects(I1, I2):
        if I1.getLeft() > I2.getRight() and I1.getMid() > I2.getMid():
            return False
        elif I2.getLeft() > I1.getRight() and I2.getMid() > I1.getMid():
            return False
        return True
