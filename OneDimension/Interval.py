class Interval:
    def __init__(self, left, right):
        self.left  = left 
        self.right = right
        self.mid   = (right + left)/2
        
    def getLeft(self):
        return self.left 
    
    def getRight(self):
        return self.right

    def getMid(self):
        return self.mid

    def getInterval(self):
        return [self.left, self.right]

    def print(self):
        print([self.left, self.right])

    def contains(self, I):
        if self.getLeft() <= I.getLeft() and self.getRight() >= I.getRight():
            return True 
        return False

    def overlaps(self, I):
        if self.contains(I) or I.contains(self):
            return True
        elif self.getLeft() < I.getLeft() and self.getRight() > I.getLeft() and self.getRight() < I.getRight():
            return True 
        elif I.getLeft() < self.getLeft() and I.getRight() > self.getLeft() and I.getRight() < self.getRight():
            return True 
        return False 

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

    @staticmethod 
    def listOverlap(l1, l2):
        if l1[0] >= l2[0] and l1[0] <= l2[1]:
            return True 
        elif l2[0] >= l1[0] and l2[0] <= l1[1]:
            return True 
        else:
            False
