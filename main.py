import tkinter as tk
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

        self.intervals = []

        def clearScreen():
            screenWindow.clearScreen()

        def clearDemoScreen():
            demonstrationScreenWindow.clearScreen()

        def getIntervals():
            self.intervals = screenWindow.getIntervals()

        def showElementaryIntervals():
            elemIntervals = SegmentTree.getElementaryIntervals(self.intervals, returnList=1)
            demonstrationScreenWindow.drawElementaryIntervals(elemIntervals, self.intervals)
            
        
        clearScreenButton = tk.Button(root, text="Clear Screen", command=clearScreen, height=1, width=20)
        getIntervalsButton = tk.Button(root, text="Get Intervals", command=getIntervals, height=1, width=20)
        showElementaryIntervalsButton = tk.Button(root, text="Show Elem. Intervals", command=showElementaryIntervals, height=1, width=20)
        clearDemoScreenButton = tk.Button(root, text="Clear Demo. Screen", command=clearDemoScreen, height=1, width=20)
        clearScreenButton.grid(row=0,column=0,padx=(30,30),pady=(5,5))
        getIntervalsButton.grid(row=0,column=1,padx=(30,30),pady=(5,5))
        showElementaryIntervalsButton.grid(row=1, column=0,padx=(30,30),pady=(5,5))
        clearDemoScreenButton.grid(row=1,column=1,padx=(30,30),pady=(5,5))
        
        root.mainloop()

if __name__ == "__main__":
    Main()