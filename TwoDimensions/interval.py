class Interval:
    # this class corresponds to an interval on the real-line
    def __init__(self, left, right):
        self.left  = left 
        self.right = right
        self.mid   = (right + left)/2

    # makes a deep copy of the interval
    def copy(self):
        return Interval(self.left, self.right)
        
    # getters
    def getLeft(self):
        return self.left 
    
    def getRight(self):
        return self.right

    def getMid(self):
        return self.mid

    def getInterval(self):
        return (self.left, self.right)

    # prints the interval as a tuple
    def print(self):
        print((self.left, self.right))

    # checks whether interval I is contained inside this interval
    def contains(self, I):
        if self.getLeft() <= I.getLeft() and self.getRight() >= I.getRight():
            return True 
        return False

    # checks whether interval I is overlapping with this interval
    def overlaps(self, I):
        if self.contains(I) or I.contains(self):
            return True
        elif self.getLeft() <= I.getLeft() and self.getRight() >= I.getLeft() and self.getRight() <= I.getRight():
            return True 
        elif I.getLeft() <= self.getLeft() and I.getRight() >= self.getLeft() and I.getRight() <= self.getRight():
            return True 
        return False 

    # returns the union of two intervals
    @staticmethod
    def union(I1, I2):
        return Interval(min(I1.getLeft(), I2.getLeft()), max(I1.getRight(), I2.getRight()))

    # checks whether the value belongs to interval I
    @staticmethod
    def liesInInterval(I, val):
        if (val - I.getLeft()) * (I.getRight() - val) > 0:
            return True 
        return False 

    # checks whether the value belongs on the end-points of interval I
    @staticmethod
    def liesOnInterval(I, val):
        if val == I.getLeft() or val == I.getRight():
            return True 
        return False 