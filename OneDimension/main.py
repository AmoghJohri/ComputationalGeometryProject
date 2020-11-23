# importing standard libraries
import tkinter as tk
# importing modules
import segmentTree as SegmentTree
from   screen             import Screen
from   demostrationScreen import DemonstrationScreen
class Main:
    def __init__(self):
        # main window
        root = tk.Tk()
        root.title("Main Window")
        # get screen width and height
        screen_width     = root.winfo_screenwidth()
        screen_height    = root.winfo_screenheight()
        # placing the toplevel
        root.geometry("500x250+%d+%d" % (((280/1900)*screen_width + 425), (((1040.0-220)/1000)*screen_height)-670))
        # defining the toplevels
        screenWindow              = Screen()
        demonstrationScreenWindow = DemonstrationScreen()
        # defining local variables
        self.intervals   = []
        self.queryPoints = []
        self.root        = None
        self.counter     = 0

        # clears the screen
        def clearScreen():
            screenWindow.clearScreen()

        # clears the demonstration screen
        def clearDemoScreen():
            demonstrationScreenWindow.clearScreen()

        # gets the input intervals
        def getIntervals():
            self.intervals = screenWindow.getIntervals()

        # displays the elementary intervals
        def showElementaryIntervals():
            elemIntervals = SegmentTree.getElementaryIntervals(self.intervals, returnList=1)
            demonstrationScreenWindow.drawElementaryIntervals(elemIntervals, self.intervals)

        # to switch to drawing input intervals  
        def drawLines():
            screenWindow.changeBinding("line")
    
        # to switch to drawing query points
        def drawPoints():
            screenWindow.changeBinding("point")
        
        # gets the query points
        def getQueryPoints():
            self.queryPoints = screenWindow.getPoints()

        # constructs the segment tree
        def buildSegmentTree():
            self.root = SegmentTree.createSegmentTree(self.intervals)

        # rests the query counter
        def resetCounter():
            self.counter = 0

        # draws each query point and the corresponding intervals
        def drawQuery():
            demonstrationScreenWindow.drawQuery(self.queryPoints[self.counter], SegmentTree.query(self.root, self.queryPoints[self.counter]))
            self.counter += 1
            self.counter  = self.counter%len(self.queryPoints)

        # draws the segment tree
        def drawSegmentTree():
            demonstrationScreenWindow.drawSegmentTree(self.root)

        # draws grid lines in demonstration screen
        def drawGridLines():
            demonstrationScreenWindow.drawGrid()

        # draws a visualization of the query
        def visualizeQuery():
            demonstrationScreenWindow.drawQuery(self.queryPoints[self.counter], SegmentTree.query(self.root, self.queryPoints[self.counter]))
            demonstrationScreenWindow.visualizeQuery(self.root, SegmentTree.query(self.root, self.queryPoints[self.counter], visualize=1))
            self.counter += 1
            self.counter  = self.counter%len(self.queryPoints)

        # toggle popup display
        def toggle():
            demonstrationScreenWindow.toggle()
        
        # defining the buttons
        clearScreenButton                 = tk.Button(root, text="Clear Screen",         command=clearScreen,             height=1, width=20)
        getIntervalsButton                = tk.Button(root, text="Get Intervals",        command=getIntervals,            height=1, width=20)
        showElementaryIntervalsButton     = tk.Button(root, text="Show Elem. Intervals", command=showElementaryIntervals, height=1, width=20)
        clearDemoScreenButton             = tk.Button(root, text="Clear Demo. Screen",   command=clearDemoScreen,         height=1, width=20)
        drawLinesButton                   = tk.Button(root, text="Draw Intervals",       command=drawLines,               height=1, width=20)
        drawPointsButton                  = tk.Button(root, text="Draw Points",          command=drawPoints,              height=1, width=20)
        getQueryPointsButton              = tk.Button(root, text="Get Query Points",     command=getQueryPoints,          height=1, width=20)
        buildSegmentTreeButton            = tk.Button(root, text="Build Segment Tree",   command=buildSegmentTree,        height=1, width=20)
        resetCounterButton                = tk.Button(root, text="Reset Counter",        command=resetCounter,            height=1, width=20)
        drawQueryButton                   = tk.Button(root, text="Draw Query Result",    command=drawQuery,               height=1, width=20)
        drawSegmentTreeButton             = tk.Button(root, text="Draw Segment Tree",    command=drawSegmentTree,         height=1, width=20)
        drawGridLinesButton               = tk.Button(root, text="Draw Grid Lines",      command=drawGridLines,           height=1, width=20)
        segmentTreeNodeInfoButton         = tk.Button(root, text="Visualize Query",      command=visualizeQuery,          height=1, width=20)
        popupToggleButton                 = tk.Button(root, text="Toggle Popup",         command=toggle,                  height=1, width=20)
        # placing the buttons
        clearScreenButton.grid            (row=0,column=0,padx=(30,30),pady=(5,5))
        getIntervalsButton.grid           (row=0,column=1,padx=(30,30),pady=(5,5))
        showElementaryIntervalsButton.grid(row=1,column=0,padx=(30,30),pady=(5,5))
        clearDemoScreenButton.grid        (row=1,column=1,padx=(30,30),pady=(5,5))
        drawLinesButton.grid              (row=2,column=0,padx=(30,30),pady=(5,5))
        drawPointsButton.grid             (row=2,column=1,padx=(30,30),pady=(5,5))
        getQueryPointsButton.grid         (row=3,column=1,padx=(30,30),pady=(5,5))
        buildSegmentTreeButton.grid       (row=3,column=0,padx=(30,30),pady=(5,5))
        resetCounterButton.grid           (row=4,column=0,padx=(30,30),pady=(5,5))
        drawQueryButton.grid              (row=4,column=1,padx=(30,30),pady=(5,5))
        drawSegmentTreeButton.grid        (row=5,column=0,padx=(30,30),pady=(5,5))
        drawGridLinesButton.grid          (row=5,column=1,padx=(30,30),pady=(5,5))
        segmentTreeNodeInfoButton.grid    (row=6,column=0,padx=(30,30),pady=(5,5))
        popupToggleButton.grid            (row=6,column=1,padx=(30,30),pady=(5,5))
        # trigger the main loop
        root.mainloop()

if __name__ == "__main__":
    Main()