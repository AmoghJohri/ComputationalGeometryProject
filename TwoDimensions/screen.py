import copy
import tkinter as tk

class Screen:

    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Screen")
        self.width = 600
        self.height = 600
        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height, bg='white')
        self.canvas.pack()
        self.canvas.old_coords = None
        self.intervals = []
        self.points = []
        self.drawGrid()

        def near(x):
            if x%20 < 10:
                return x - x%20 
            else:
                return x + (20 - x%20)

        def draw(event):
            x, y = event.x, event.y
            if self.canvas.old_coords:
                x1, y1 = self.canvas.old_coords
                self.canvas.create_line(x, y, x1, y1, width=3)
            self.canvas.old_coords = x, y

        def draw_line(event):
            if str(event.type) == 'ButtonPress':
                self.canvas.old_coords = event.x, event.y
            elif str(event.type) == 'ButtonRelease':
                x, y = event.x, event.y
                x1, y1 = self.canvas.old_coords
                self.canvas.create_line(near(x), near(y), near(x1), near(y1), width=3)
                if near(x) < near(x1):
                    self.intervals.append([(near(x), near(y)), (near(x1), near(y1))])
                else:
                    self.intervals.append([(near(x1), near(y1)), (near(x), near(y))])

        def draw_point(event):
            if str(event.type) == 'ButtonPress':
                self.canvas.old_coords = event.x, event.y
            elif str(event.type) == 'ButtonRelease':
                x, y = event.x, event.y
                x1, y1 = self.canvas.old_coords
                self.canvas.create_line(near(x), near(y), near(x), near(y1), width=3)
                self.points.append([(near(x), (min(near(y), near(y1)))), (near(x), max(near(y), near(y1)))])
        self.drawFunctions = [draw_line, draw_point]
        self.f = self.drawFunctions[0]
        self.window.bind('<ButtonPress-1>', self.f)
        self.window.bind('<ButtonRelease-1>', self.f)

        def reset_coords(event):
            self.canvas.old_coords = None

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
        for i in range(int(self.width/fine)):
            self.canvas.create_line(i*fine, 0, i*fine, 600)
            self.canvas.create_line(0, i*fine, 600, i*fine)

    def clearScreen(self):
        self.canvas.delete('all')
        self.intervals = []
        self.points = []
        self.drawGrid()

    def getIntervals(self):
        return copy.deepcopy(self.intervals)
    
    def getPoints(self):
        return copy.deepcopy(self.points)

if __name__ == "__main__":
    screen = Screen()