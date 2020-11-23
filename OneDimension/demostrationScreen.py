# importing standard libraries
import copy
import random
import tkinter as tk
# importing modules
from node import Node
class DemonstrationScreen:
    # This is used for demonstrating and visualizing the various aspects related to the algorithm
    # initialization method
    def __init__(self):
        # defining the window
        window = tk.Toplevel()
        window.title("Demonstration Screen")
        self.width  = 600
        self.height = 600
        # defining the placement of the window
        window.geometry("600x600+%d+%d" % (2.25*self.width, self.height/5))
        # defining the canvas
        self.canvas = tk.Canvas(window, width=self.width, height=self.height, bg='white')
        self.canvas.pack()
        self.canvas.old_coords = None
        # this stores the intervals which shall to display
        self.intervals         = []

    # clears the demonstration screen
    def clearScreen(self):
        self.canvas.delete('all')

    # drawing elementary intervals corresponding to the unit
    def drawElementaryIntervals(self, intervals, intervals2):
        # intervals2 consist of input intervals
        # intervals consist of elementary intercals
        self.canvas.delete('all')
        # drawing the elementary intervals
        for each in intervals:
            self.canvas.create_line(each[0], 0, each[0], 600, width=3)
            self.canvas.create_line(each[1], 0, each[1], 600, width=3)
        i = 100
        j = 0
        # randomly selecting the color for the input interval
        arr  = random.sample(range(0, 99), len(intervals2))
        arr2 = ["a","b","c","d","e"]
        # drawing the input intervals
        for each in intervals2:
            self.canvas.create_line(each[0], i, each[1], i, width=3, fill="#" + arr2[j%5] + "%02x" % arr[j])
            j += 1
            i += 20

    # draws vertical query segment and all the corresponding query intervals
    def drawQuery(self, point, arr):
        self.canvas.delete('all')
        # drawing the vertical query segment
        self.canvas.create_line(point, 0, point, 600, width=3)
        i = 100
        # drawing the corresponding query intervals
        for each in arr:
            self.canvas.create_line(each[0], i, each[1], i, width=3)
            i += 20

    # draws the segment tree corresponding to the elementary intervals
    def drawSegmentTree(self, root):
        # declaring the queue for a level-order traversal (BFS)
        q = []
        q.append(root)
        while q:
            # traversing through the levels
            curr = q.pop(0)
            if curr.getLeftChild() != None:
                q.append(curr.getLeftChild())
            if curr.getRightChild() != None:    
                q.append(curr.getRightChild())
            left  = max(0, curr.getInterval().getLeft())
            left  = min(left, 600)
            right = min(600, curr.getInterval().getRight())
            right = max(right, 0)
            mid   = (left + right)/2
            # drawing the current node
            self.canvas.create_line(mid-3, 500 - curr.getHeight()*50, mid+3, 500 - curr.getHeight()*50, width=3)
            # drawing the connecting segment to left-child
            if curr.getLeftChild() != None:
                leftChild  = max(0, curr.getLeftChild().getInterval().getLeft())
                leftChild  = min(leftChild, 600)
                rightChild = min(600, curr.getLeftChild().getInterval().getRight())
                rightChild = max(rightChild, 0)
                midChild   = (leftChild + rightChild)/2
                self.canvas.create_line(mid, 500 - curr.getHeight()*50, midChild, 500 - (curr.getLeftChild().getHeight())*50, width=3)
            # drawing the connecting segment to right-child
            if curr.getRightChild() != None:
                leftChild  = max(0, curr.getRightChild().getInterval().getLeft())
                leftChild  = min(leftChild, 600)
                rightChild = min(600, curr.getRightChild().getInterval().getRight())
                rightChild = max(rightChild, 0)
                midChild   = (leftChild + rightChild)/2
                self.canvas.create_line(mid, 500 - curr.getHeight()*50, midChild, 500 - (curr.getRightChild().getHeight())*50, width=3)

if __name__ == "__main__":
    demonstrationScreen = DemonstrationScreen()