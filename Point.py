class Point:
    def __init__(self, val, interval):
        self.value = val 
        self.interval = interval 

    def getValue(self):
        return self.value 
    
    def getInterval(self):
        return self.interval 
    
    def setValue(self, val):
        self.value = val 
    
    def setInterval(self, interval):
        self.interval = interval