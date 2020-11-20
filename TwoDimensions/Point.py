from Line import Line 

class Point:
    def __init__(self, x, y, line=None):
        self.x = x 
        self.y = y 
        self.line = line 

    def getX(self):
        return self.x 
    
    def getY(self):
        return self.y 

    def getLine(self):
        return self.line 

    def getPoints(self):
        return (self.x, self.y)