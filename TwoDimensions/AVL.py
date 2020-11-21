from treeNode import TreeNode
class AVL_Tree(object): 
  
    # Recursive function to insert key in  
    # subtree rooted with node and returns 
    # new root of subtree. 
    def insert(self, root, key, data): 
      
        # Step 1 - Perform normal BST 
        if not root: 
            return TreeNode(key, data) 
        elif key < root.val: 
            root.left = self.insert(root.left, key, data) 
        else: 
            root.right = self.insert(root.right, key, data) 
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                           self.getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and key < root.left.val: 
            return self.rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and key > root.right.val: 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and key > root.left.val: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and key < root.right.val: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 
  
    def leftRotate(self, z): 
  
        y = z.right 
        T2 = y.left 
  
        # Perform rotation 
        y.left = z 
        z.right = T2 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                         self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                         self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def rightRotate(self, z): 
  
        y = z.left 
        T3 = y.right 
  
        # Perform rotation 
        y.right = z 
        z.left = T3 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right) 

    def inOrder(self, root): 
        if not root: 
            return
        self.inOrder(root.left)
        print("{0} ".format(root.val), end="")  
        self.inOrder(root.right) 

    def getAll(self, root):
        out = []
        self.getAll_(root, out)
        return out

    def getAll_(self, root, out):
        if not root:
            return
        self.getAll_(root.left, out)
        out.append(root.val.interval)
        self.getAll_(root.right, out)

    def query(self, root, interval):
        out = []
        self.getQuery(root, interval, out)
        return out

    def getQuery(self, root, interval, out):
        if not root:
            return
        if not (min(interval) > max(root.val.interval) or max(interval) < min(root.val.interval)):
            out.append(root.data)
        if max(interval) > min(root.val.interval):
            self.getQuery(root.right, interval, out)
        if min(interval) < max(root.val.interval):
            self.getQuery(root.left, interval, out)