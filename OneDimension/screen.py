# importing standard libraries
import copy
import tkinter as tk
class Screen:
    # this corresponds to the screen which accepts input
    # initialization method
    def __init__(self):
        # defining the window
        self.window = tk.Toplevel()
        self.window.title("Screen")
        self.width  = 600
        self.height = 600
        # defining the placement of the window
        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height, bg='white')
        self.canvas.pack()
        self.canvas.old_coords = None
        # defining the local variables
        self.intervals = []
        self.points    = []
        # draws the grid lines
        self.drawGrid()

        # approximates the poistion of the input according to grid lines
        def near(x):
            if x%20 < 10:
                return x - x%20
            return x + (20 - x%20)

        # to take a line as an input
        def draw_line(event):
            if str(event.type) == 'ButtonPress':
                self.canvas.old_coords = event.x, event.y
            elif str(event.type) == 'ButtonRelease':
                x, y = event.x, event.y
                x1, y1 = self.canvas.old_coords
                self.canvas.create_line(near(x), near(y), near(x1), near(y), width=3)
                self.intervals.append([min(near(x),near(x1)) + 40, max(near(x),near(x1)) + 40])

        # to take the query point as input
        def draw_point(event):
            if str(event.type) == 'ButtonPress':
                self.canvas.old_coords = event.x, event.y
            elif str(event.type) == 'ButtonRelease':
                x, y   = event.x, event.y
                x1, y1 = self.canvas.old_coords
                self.canvas.create_line(near(x), 0, near(x), 560, width=3)
                self.points.append(near(x)+40)
        
        def reset_coords(event):
            self.canvas.old_coords = None

        # variables to toggle between interval input and point input
        self.drawFunctions = [draw_line, draw_point]
        self.f = self.drawFunctions[0]
        self.window.bind('<ButtonPress-1>', self.f)
        self.window.bind('<ButtonRelease-1>', self.f)

    # function to toggle between interval input and point input
    def changeBinding(self, s):
        if s == "line":
            self.f = self.drawFunctions[0]
        else:
            self.f = self.drawFunctions[1]
        self.window.bind('<ButtonPress-1>', self.f)
        self.window.bind('<ButtonRelease-1>', self.f)
        
    # drawing grid lines
    def drawGrid(self):
        fine = 20
        for i in range(int(self.width/fine)-1):
            self.canvas.create_line((i+2)*fine, 0, (i+2)*fine, 600-2*fine)
            self.canvas.create_line(2*fine, i*fine, 600, i*fine)
        for j in range(0, 600, 40):
            if j == 560 or j == 0:
                continue
            self.canvas.create_text(20,j,fill="darkblue",font="Times 10 italic bold",
                        text=str(560-j))
            self.canvas.create_text(j+40,580,fill="darkblue",font="Times 10 italic bold",
                        text=str(j))
        self.canvas.create_text(40,580,fill="darkblue",font="Times 10 italic bold",
                        text=str(0))
        self.canvas.create_text(20,560,fill="darkblue",font="Times 10 italic bold",
                        text=str(0))

    # clears the screen and the local vairables with the values
    def clearScreen(self):
        self.canvas.delete('all')
        self.intervals = []
        self.points    = []
        self.drawGrid()

    # returns the deep copy of the intervals
    def getIntervals(self):
        return copy.deepcopy(self.intervals)
    
    # returns the deep copy of query points
    def getPoints(self):
        return copy.deepcopy(self.points)

if __name__ == "__main__":
    screen = Screen()