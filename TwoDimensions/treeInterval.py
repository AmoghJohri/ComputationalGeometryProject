# importing modules
from line import Line 
# this corresponds to the segment tree interval stored at every node
class TreeInterval:
    # initialization method
    def __init__(self, line, inter):
        if not line.isVertical():
            interval    = ((inter.getLeft()*line.getSlope() + line.getConstant()),  (inter.getRight()*line.getSlope() + line.getConstant()))
        else:
            interval    = (line.getTopPoint(), line.getBottomPoint())
        self.mid        = (interval[0] + interval[1])/2
        self.interval   = [interval[0], interval[1]]
        self.height     = 1

    # overloading operators
    def __lt__(self, other):
        if type(other) == int or type(other) == float:
            if min(self.interval) < other:
                return True 
            return False 
        elif type(other) == type(self):
            if self.mid < other.mid:
                return True 
            return False

    def __gt__(self, other):
        if type(other) == int or type(other) == float:
            if max(self.interval) > other:
                return True 
            return False
        elif type(other) == type(self):
            if self.mid > other.mid:
                return True 
            return False

    def __eq__(self, other):
        if type(other) == int or type(other) == float:
            if min(self.left, self.right) <= other and max(self.left, self.right) >= other:
                return True 
            return False
        elif type(other) == type(self):
            if self.mid == other.mid:
                return True 
            return False

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)
    
    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __str__(self):
        return str(self.interval)