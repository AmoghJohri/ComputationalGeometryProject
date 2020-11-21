import tkinter as tk
from SegmentTree import createSegmentTree
from screen import Screen
from demostrationScreen import DemonstrationScreen
import SegmentTree

class Main:
    def __init__(self):
        # main window
        root = tk.Tk()
        root.title("Main Window")
        # get screen width and height
        screen_width     = root.winfo_screenwidth()
        screen_height    = root.winfo_screenheight()
        # placing the toplevel
        root.geometry("500x300+%d+%d" % (((280/1900)*screen_width + 425), (((1040.0-220)/1000)*screen_height)-670))
        # defining the toplevels
        screenWindow = Screen()
        demonstrationScreenWindow = DemonstrationScreen()

        self.intervals   = []
        self.queryPoints = []

        self.root = None
        self.counter = 0

        def clearScreen():
            screenWindow.clearScreen()

        def clearDemoScreen():
            demonstrationScreenWindow.clearScreen()

        def getIntervals():
            self.intervals = screenWindow.getIntervals()

        def showElementaryIntervals():
            elemIntervals = SegmentTree.getElementaryIntervals(self.intervals, returnList=1)
            demonstrationScreenWindow.drawElementaryIntervals(elemIntervals, self.intervals)
            
        def drawLines():
            screenWindow.changeBinding("line")
    
        def drawPoints():
            screenWindow.changeBinding("point")
        
        def getQueryPoints():
            self.queryPoints = screenWindow.getPoints()

        def buildSegmentTree():
            self.root = createSegmentTree(self.intervals)

        def resetCounter():
            self.counter = 0

        def drawQuery():
            arr = SegmentTree.query(self.root, self.queryPoints[self.counter])
            demonstrationScreenWindow.drawQuery(self.queryPoints[self.counter], arr)
            self.counter = (self.counter + 1)%len(self.queryPoints)

        def drawSegmentTree():
            demonstrationScreenWindow.drawSegmentTree(self.root)
        
        clearScreenButton = tk.Button(root, text="Clear Screen", command=clearScreen, height=1, width=20)
        getIntervalsButton = tk.Button(root, text="Get Intervals", command=getIntervals, height=1, width=20)
        showElementaryIntervalsButton = tk.Button(root, text="Show Elem. Intervals", command=showElementaryIntervals, height=1, width=20)
        clearDemoScreenButton = tk.Button(root, text="Clear Demo. Screen", command=clearDemoScreen, height=1, width=20)
        drawLinesButton = tk.Button(root, text="Draw Intervals", command=drawLines, height=1, width=20)
        drawPointsButton = tk.Button(root, text="Draw Query Segments", command=drawPoints, height=1, width=20)
        getQueryPointsButton = tk.Button(root, text="Get Query Segments", command=getQueryPoints, height=1, width=20)
        buildSegmentTreeButton = tk.Button(root, text="Build Segment Tree", command=buildSegmentTree, height=1, width=20)
        resetCounterButton = tk.Button(root, text="Reset Counter", command=resetCounter, height=1, width=20)
        drawQueryButton = tk.Button(root, text="Draw Query Result", command=drawQuery, height=1, width=20)
        # drawSegmentTreeButton = tk.Button(root, text="Draw Segment Tree", command=drawSegmentTree, height=1, width=20)
        clearScreenButton.grid(row=0,column=0,padx=(30,30),pady=(5,5))
        getIntervalsButton.grid(row=0,column=1,padx=(30,30),pady=(5,5))
        showElementaryIntervalsButton.grid(row=1, column=0,padx=(30,30),pady=(5,5))
        clearDemoScreenButton.grid(row=1,column=1,padx=(30,30),pady=(5,5))
        drawLinesButton.grid(row=2, column=0,padx=(30,30),pady=(5,5))
        drawPointsButton.grid(row=2,column=1,padx=(30,30),pady=(5,5))
        getQueryPointsButton.grid(row=3,column=1,padx=(30,30),pady=(5,5))
        buildSegmentTreeButton.grid(row=3,column=0,padx=(30,30),pady=(5,5))
        resetCounterButton.grid(row=4,column=0,padx=(30,30),pady=(5,5))
        drawQueryButton.grid(row=4,column=1,padx=(30,30),pady=(5,5))
        # drawSegmentTreeButton.grid(row=5,column=0,padx=(30,30),pady=(5,5))

        root.mainloop()

if __name__ == "__main__":
    Main()