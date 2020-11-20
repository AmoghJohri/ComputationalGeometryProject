class Line: 
    def __init__(self, x_interval, y_interval):
        self.x_interval = x_interval
        self.y_interval = y_interval
        if y_interval[1] - y_interval[0] == 0:
            self.isVertical = True
            self.m = None 
            self.c = None
        else:
            self.isVertical = False
            self.m = (y_interval[1] - y_interval[0])/(x_interval[1] - x_interval[0])
            self.c = (y_interval[1] - self.m*x_interval[1])
    
    def getSlope(self):
        return self.m 

    def getConstant(self):
        return self.c 

    def getLeftPoint(self):
        return self.x_interval[0] 

    def getRightPoint(self):
        return self.x_interval[1]

    def getTopPoint(self):
        return self.y_interval[1]
    
    def getBottomPoint(self):
        return self.y_interval[0]

    def getXInterval(self):
        return self.x_interval
    
    def getYInterval(self):
        return self.y_interval

    def getKey(self):
        return (self.getTopPoint() + self.getBottomPoint())/2

    def getLine(self):
        return [ [self.x_interval[0], self.y_interval[0] ], [self.x_interval[1], self.y_interval[1]] ]

    def print(self):
        print([ [self.x_interval[0], self.y_interval[0] ], [self.x_interval[1], self.y_interval[1]] ])