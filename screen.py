import copy
import tkinter as tk

class Screen:

    def __init__(self):
        window = tk.Toplevel()
        window.title("Screen")
        self.width = 600
        self.height = 600
        self.canvas = tk.Canvas(window, width=self.width, height=self.height, bg='white')
        self.canvas.pack()
        self.canvas.old_coords = None
        self.intervals = []
        self.drawGrid()

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
                self.canvas.create_line(x, y, x1, y1, width=3)
                self.intervals.append([min(x,x1), max(x,x1)])

        def reset_coords(event):
            self.canvas.old_coords = None

        window.bind('<ButtonPress-1>', draw_line)
        window.bind('<ButtonRelease-1>', draw_line)

    # drawing grid lines
    def drawGrid(self):
        fine = 20
        for i in range(int(self.width/fine)):
            self.canvas.create_line(i*fine, 0, i*fine, 600)
            self.canvas.create_line(0, i*fine, 600, i*fine)

    def clearScreen(self):
        self.canvas.delete('all')
        self.intervals = []
        self.drawGrid()

    def getIntervals(self):
        return copy.deepcopy(self.intervals)

if __name__ == "__main__":
    screen = Screen()