# this corresponds to a node in the avl-tree
class TreeNode(object): 
    def __init__(self, val, data): 
        self.data = data
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1