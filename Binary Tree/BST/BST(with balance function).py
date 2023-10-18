
################################################# Includes BST, height of tree, Balanced or not ############################################### 

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
                self.left.addelement(val)
        else:
            if self.right == None:
                self.right = BinarySearchTree(val)
            else:
                self.right.addelement(val)
                
        self.height = max(self.left.heightTree() if self.left else -1, self.right.heightTree() if self.right else -1) + 1
    
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
        
if __name__ == "__main__":
    tree = BinarySearchTree(10)
    nums = [11, 6, 5, 7, 4, 3]
    for num in nums:
        tree.addelement(num)

    print("Displaying the tree:")
    tree.display()
    
    print("\ncheck if the tree is balanced or not")
    print(tree.balancedTree())