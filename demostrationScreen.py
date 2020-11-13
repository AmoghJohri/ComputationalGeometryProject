import copy
import random
import tkinter as tk

class DemonstrationScreen:
    def __init__(self):
        window = tk.Toplevel()
        window.title("Demonstration Screen")
        self.width = 600
        self.height = 600
        window.geometry("600x600+%d+%d" % (2.25*self.width, self.height/5))
        self.canvas = tk.Canvas(window, width=self.width, height=self.height, bg='white')
        self.canvas.pack()
        self.canvas.old_coords = None
        self.intervals = []
        # self.drawGrid()

    # drawing grid lines
    def drawGrid(self):
        fine = 20
        for i in range(int(self.width/fine)):
            self.canvas.create_line(i*fine, 0, i*fine, 600, width=1)
            self.canvas.create_line(0, i*fine, 600, i*fine, width=1)

    def clearScreen(self):
        self.canvas.delete('all')
        # self.drawGrid()

    def drawElementaryIntervals(self, intervals, intervals2):
        self.canvas.delete('all')
        # self.drawGrid()
        for each in intervals:
            self.canvas.create_line(each[0], 0, each[0], 600, width=3)
            self.canvas.create_line(each[1], 0, each[1], 600, width=3)
        i = 100
        for each in intervals2:
            self.canvas.create_line(each[0], i, each[1], i, width=3, fill="#f" + "%02x" % random.randint(0, 99))
            i += 20


if __name__ == "__main__":
    demonstrationScreen = DemonstrationScreen()