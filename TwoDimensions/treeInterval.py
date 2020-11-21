class TreeInterval:
    def __init__(self, interval):
        self.mid = (interval[0] + interval[1])/2
        self.interval = [interval[0], interval[1]]
        self.height = 1

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