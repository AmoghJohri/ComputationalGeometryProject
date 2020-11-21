import copy
import random
import tkinter as tk
from Node import Node
from Line import Line

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
        j = 0
        arr = random.sample(range(0, 99), len(intervals2))
        arr2 = ["a","b","c","d","e"]
        for each in intervals2:
            self.canvas.create_line(each[0][0], each[0][1], each[1][0], each[1][1], width=3, fill="#" + arr2[j%5] + "%02x" % arr[j])
            j += 1

    def drawQuery(self, point, arr):
        self.canvas.delete('all')
        self.canvas.create_line(point[0], point[1][0], point[0], point[1][1], width=3)
        for each in arr:
            each = each.getLine()
            self.canvas.create_line(each[0][0], each[0][1], each[1][0], each[1][1], width=3)

    def drawSegmentTree(self, root):
        q = []
        q.append(root)
        while q:
            curr = q.pop(0)
            if curr.getLeftChild() != None:
                q.append(curr.getLeftChild())
            if curr.getRightChild() != None:    
                q.append(curr.getRightChild())
            mid = curr.getInterval().getMid()
            self.canvas.create_line(mid-3, 500 - curr.getHeight()*50, mid+3, 500 - curr.getHeight()*50)
            if curr.getLeftChild() != None:
                self.canvas.create_line(mid, 500 - curr.getHeight()*50, curr.getLeftChild().getInterval().getMid(), 500 - curr.getLeftChild().getHeight()*50)
            if curr.getRightChild() != None:
                self.canvas.create_line(mid, 500 - curr.getHeight()*50, curr.getRightChild().getInterval().getMid(), 500 - curr.getRightChild().getHeight()*50)


if __name__ == "__main__":
    demonstrationScreen = DemonstrationScreen()