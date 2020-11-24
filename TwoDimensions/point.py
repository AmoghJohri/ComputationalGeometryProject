# this corresponds to a node in the plane
class Point:
    # initialization function
    def __init__(self, x, y, line=None):
        self.x = x 
        self.y = y 
        self.line = line 

    # getters
    def getX(self):
        return self.x 
    
    def getY(self):
        return self.y 

    def getLine(self):
        return self.line 

    def getPoints(self):
        return (self.x, self.y)