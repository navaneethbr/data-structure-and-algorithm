class BinarySearchTree:   
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 0
        
    def addelement(self, val):
        if val < self.val:
            if self.left == None:
                self.left = BinarySearchTree(val)
            else:
                self.left = self.left.addelement(val)
        else:
            if self.right == None:
                self.right = BinarySearchTree(val)
            else:
                self.right = self.right.addelement(val)
                
        self.height = max(self.left.height if self.left else -1, self.right.height if self.right else -1) + 1
        
        return self.rotate(val)
    
    def heightTree(self):
        return self.height
        
    def display(self):
        print("Vlaue of Node {}".format(self.val), "and the Height {}".format(self.height))
        if self.left:
            self.left.display()
        if self.right:
            self.right.display()
        
    def balancedTree(self):
        if abs((self.left.heightTree() if self.left else -1) - (self.right.heightTree() if self.right else -1)) <=1:
            return (self.left.balancedTree() if self.left else True) and (self.right.balancedTree() if self.right else True)
        else:
            return False
        
    def rotate(self, val):
        
        # For left unbalanced tree
        if ((self.left.height if self.left else -1) - (self.right.height if self.right else -1)) > 1:
            if val < self.left.val :
                return self.rightRotate()
                
            elif val > self.left.val:
                self.right = self.right.leftRotate()
                return self.rightRotate()
                
        # For right unbalanced tree
        if ((self.right.height if self.right else -1) - (self.left.height if self.left else -1)) >1:
            if val > self.right.val:
                return self.leftRotate()
            
            elif val < self.right.val:
                self.left = self.left.rightRotate()
                return self.leftRotate()
            
        return self
                
    def leftRotate(self):
        
        # Assigning right of 'p' as 'c' and left of c as 't' and 'self' is understood as 'p'
        c = self.right
        t = c.left
        
        c.left = self
        self.right = t 
        
        self.height = max((self.left.height if self.left else -1), (self.right.height if self.right else -1)) + 1
        c.height = max((c.left.height if c.left else -1), (c.right.height if c.right else -1)) + 1
        
        return c
        
    def rightRotate(self):
        
        # Assigning left of 'p' as 'c' and right of c as 't' and 'self' is understood as 'p'
        c = self.left
        t = c.right
        
        c.right = self
        self.left = t
        
        self.height = max((self.left.height if self.left else -1), (self.right.height if self.right else -1)) + 1
        c.height = max((c.left.height if c.left else -1), (c.right.height if c.right else -1)) + 1
        
        return c
        
        
if __name__ == "__main__":
    tree = BinarySearchTree(1)
    nums = [2, 3, 4, 5, 6, 7]
    for num in nums:
        tree = tree.addelement(num)

    print("Displaying the tree:")
    tree.display()
    
    print("\ncheck if the tree is balanced or not")
    # print(tree.balancedTree())