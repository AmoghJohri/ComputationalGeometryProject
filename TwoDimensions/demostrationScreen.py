# importing standard libraries
import tkinter as     tk
from   tkinter import ttk
# defining the font
FONT="Times 10 italic bold" 
LARGE_FONT="Times 25 italic bold" 
class DemonstrationScreen:
    # This is used for demonstrating and visualizing the various aspects related to the algorithm
    # initialization method
    def __init__(self):
        # defining the window
        self.window = tk.Toplevel()
        self.window.title("Demonstration Screen")
        self.width  = 600
        self.height = 600
        # defining the placement of the window
        self.window.geometry("600x600+%d+%d" % (2.25*self.width, self.height/5))
        # definin the canvas
        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height, bg='white')
        self.canvas.pack()
        self.canvas.old_coords = None
        # declaring class variables
        self.intervals         = []
        self.segTreeNodes      = []
        self.active            = 1

        # to take a point as a input
        def draw_point(event):
            # doing an in-order traversal on BST
            def inOrder(root, arr=[]): 
                if not root: 
                    return
                inOrder(root.left, arr)
                arr.append(root.data) 
                inOrder(root.right, arr) 
            # book-keeping function 
            def sub(arr):
                return [[arr[0][0]-80, 600 - arr[0][1]], [arr[1][0]-80, 600 - arr[1][1]]] 
            # pop-message with the information about the segment tree node
            if self.active:
                # identify the node
                if str(event.type) == 'ButtonPress':
                    self.canvas.old_coords = event.x, event.y
                elif str(event.type) == 'ButtonRelease':
                    x, y    = event.x, event.y
                    x1, y1  = self.canvas.old_coords 
                    x       = (x + x1)/2 
                    y       = (y + y1)/2 
                    # get the segment tree node
                    for each in self.segTreeNodes: 
                        # get the relevant information
                        if abs(each[1][0] - x) <= 3 and abs(each[1][1] - y) <= 3:
                            arr = []
                            aux = ""
                            inOrder(each[0].getTree(), arr)
                            for line in arr:
                                aux += (str(sub(line.getLine()))) + "\n"
                            inter = each[0].getInterval().getInterval()
                            msg   = "Corresponding Elementary Interval: \n" + str([inter[0]-80, inter[1]-80]) + "\n" \
                                +   "Corresponding Lines: " + aux + "\n"
                            self.popupmsg(msg, each[0].getTree())
        # attaching mouse-clicks to functions
        self.window.bind('<ButtonPress-1>', draw_point)
        self.window.bind('<ButtonRelease-1>', draw_point)
        # drawing the grid
        self.drawGrid()

    # toggle popupmessage
    def toggle(self):
        self.active = (self.active + 1)%2

    # drawing grid lines
    def drawGrid(self):
        fine = 20
        # drawing the grid
        for i in range(int(self.width/fine)-1):
            self.canvas.create_line((i+2)*fine, 0, (i+2)*fine, 600-2*fine)
            self.canvas.create_line(2*fine, i*fine, 600, i*fine)
        # labelling the grid
        for j in range(0, 600, 40):
            if j == 560 or j == 0:
                continue
            self.canvas.create_text(20,j,fill="darkblue",font=FONT,
                        text=str(560-j))
            self.canvas.create_text(j+40,580,fill="darkblue",font=FONT,
                        text=str(j))
        self.canvas.create_text(40,580,fill="darkblue",font=FONT,
                        text=str(0))
        self.canvas.create_text(20,560,fill="darkblue",font=FONT,
                        text=str(0))

    # checks whether a node belongs in a list
    def belongs(self, node, list):
        for each in list:
            if node.getInterval().getInterval()[0] == each.getInterval().getInterval()[0] and \
                node.getInterval().getInterval()[1] == each.getInterval().getInterval()[1]:
                return True 
        return False

    # match interval
    def match(self, l1, l2):
        if min(l1) == min(l2) and max(l1) == max(l2):
            return True 
        return False

    # clears the demonstration screen
    def clearScreen(self):
        self.canvas.delete('all')

    # drawing elementary intervals corresponding to the input
    def drawElementaryIntervals(self, intervals, intervals2):
        # intervals2 consist of input intervals
        # intervals consist of elementary intercals
        self.canvas.delete('all')
        self.drawGrid()
        # drawing the elementary intervals
        for each in intervals:
            self.canvas.create_line(each[0]-40, 0, each[0]-40, 560, width=3)
            self.canvas.create_line(each[1]-40, 0, each[1]-40, 560, width=3)
        # drawing the input intervals
        for each in intervals2:
            self.canvas.create_line(each[0][0]-40, each[0][1]-40, each[1][0]-40, each[1][1]-40, width=3, fill="blue")

    # draws vertical query segment and all the corresponding query intervals
    def drawQuery(self, point, arr):
        self.canvas.delete('all')
        self.drawGrid()
        # drawing the vertical query segment
        self.canvas.create_line(point[0]-40, point[1][0]-40, point[0]-40, point[1][1]-40, width=3, fill="blue")
        # drawing the corresponding query intervals
        for each in arr:
            each = each.getLine()
            self.canvas.create_line(each[0][0]-40, each[0][1]-40, each[1][0]-40, each[1][1]-40, width=3)

    # to popup and display values
    def popupmsg(self, msg, root):
        def drawBST():
            popupBST = tk.Toplevel()
            popupBST.title("BST Screen")
            width  = 600
            height = 600
            # defining the placement of the window
            popupBST.geometry("600x600+%d+%d" % (2.25*width, height/5))
            # definin the canvas
            canvas = tk.Canvas(popupBST, width=width, height=height, bg='white')
            canvas.pack()
            fine = 20
            # drawing the grid
            for i in range(int(width/fine)-1):
                canvas.create_line((i+2)*fine, 0, (i+2)*fine, 600-2*fine)
                canvas.create_line(2*fine, i*fine, 600, i*fine)
            # labelling the grid
            for j in range(0, 600, 40):
                if j == 560 or j == 0:
                    continue
                canvas.create_text(20,j,fill="darkblue",font=FONT,
                            text=str(560-j))
                canvas.create_text(j+40,580,fill="darkblue",font=FONT,
                            text=str(j))
            canvas.create_text(40,580,fill="darkblue",font=FONT,
                            text=str(0))
            canvas.create_text(20,560,fill="darkblue",font=FONT,
                            text=str(0))
            # drawing the BST
            q           = [root]
            max_height  = root.height
            i           = 50
            while q:
                curr = q.pop()
                if curr == None:
                    return
                if curr.left != None:
                    q.append(curr.left)
                if curr.right != None:    
                    q.append(curr.right) 
                canvas.create_line(((max_height - curr.height) + 1) * i, 520 - curr.val.interval[0], ((max_height - curr.height) + 1) * i, 520 - curr.val.interval[1], width=3, fill="red")
                if curr.left:
                    canvas.create_line(((max_height - curr.height) + 1) * i, ((520 - curr.val.interval[0]) +  (520 - curr.val.interval[1]))/2, ((max_height - curr.left.height) + 1) * i, ((520 - curr.left.val.interval[0]) +  (520 - curr.left.val.interval[1]))/2, width=3, fill="blue")
                if curr.right:
                    canvas.create_line(((max_height - curr.height) + 1) * i, ((520 - curr.val.interval[0]) +  (520 - curr.val.interval[1]))/2, ((max_height - curr.right.height) + 1) * i,((520 - curr.right.val.interval[0]) +  (520 - curr.right.val.interval[1]))/2, width=3, fill="blue")
        # trigger for the pop-up window
        if self.active:
            popup = tk.Tk()
            popup.geometry("600x300+%d+%d" % (1.25*self.width, self.height/5))
            popup.wm_title("Interval")
            label = ttk.Label(popup, text=msg, font=LARGE_FONT)
            label.pack(side="top", fill="x", pady=30)
            B1    = ttk.Button(popup, text="Close!",   command = popup.destroy)
            B2    = ttk.Button(popup, text="Draw BST", command = drawBST)
            B1.pack()
            B2.pack()
            popup.mainloop()

    # visualizing the query
    def visualizeQuery(self, root, arr):
        self.drawSegmentTree(root, arr)

    # draws the segment tree corresponding to the elementary intervals
    def drawSegmentTree(self, root, visualize=[]):
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
            self.canvas.create_oval((mid-3)-40, 500 - curr.getHeight()*50, (mid+3)-40, 500 - curr.getHeight()*50, width=3)
            self.segTreeNodes.append([curr, [mid-40, (500 - curr.getHeight()*50)]])
            # drawing the connecting segment to left-child
            if curr.getLeftChild() != None:
                leftChild  = max(0, curr.getLeftChild().getInterval().getLeft())
                leftChild  = min(leftChild, 600)
                rightChild = min(600, curr.getLeftChild().getInterval().getRight())
                rightChild = max(rightChild, 0)
                midChild   = (leftChild + rightChild)/2
                self.canvas.create_line(mid-40, 500 - curr.getHeight()*50, midChild-40, 500 - (curr.getLeftChild().getHeight())*50, width=3)
            # drawing the connecting segment to right-child
            if curr.getRightChild() != None:
                leftChild  = max(0, curr.getRightChild().getInterval().getLeft())
                leftChild  = min(leftChild, 600)
                rightChild = min(600, curr.getRightChild().getInterval().getRight())
                rightChild = max(rightChild, 0)
                midChild   = (leftChild + rightChild)/2
                self.canvas.create_line(mid-40, 500 - curr.getHeight()*50, midChild-40, 500 - (curr.getRightChild().getHeight())*50, width=3)
            # marking query path
            if self.belongs(curr, visualize):
                self.markPath(curr)

    # marks the query path
    def markPath(self, curr):
        if curr.getParent() == None:
            return 
        currP = curr.getParent()
        # drawing the connecting segment to right-child
        left       = max(0, currP.getInterval().getLeft())
        left       = min(left, 600)
        right      = min(600, currP.getInterval().getRight())
        right      = max(right, 0)
        mid        = (left + right)/2
        leftChild  = max(0, curr.getInterval().getLeft())
        leftChild  = min(leftChild, 600)
        rightChild = min(600, curr.getInterval().getRight())
        rightChild = max(rightChild, 0)
        midChild   = (leftChild + rightChild)/2
        self.canvas.create_line(mid-40, 500 - currP.getHeight()*50, midChild-40, 500 - (curr.getHeight())*50, width=3, fill = "red")
        self.markPath(currP)

if __name__ == "__main__":
    demonstrationScreen = DemonstrationScreen()