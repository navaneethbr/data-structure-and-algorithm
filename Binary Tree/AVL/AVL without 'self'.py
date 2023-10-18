class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 0
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def addel(self):
        for num in range(10):
            self.root = self.addelement(num, self.root)
        print(self.height(self.root))

    def addelement(self, val, node):
        if node == None:
            return  TreeNode(val)
        if val < node.val:
            node.left = self.addelement(val, node.left)
              
        else:
            node.right = self.addelement(val, node.right)
                
        node.height = max(self.height(node.left), self.height(node.right)) + 1 
        
        return self.rotate(node, val)

    
    def height(self, node):
        if node == None:
            return -1
        return node.height
            
    def display(self):
        self.displaytree(self.root)
        
    def displaytree(self, node):
        if node == None:
            return
        self.displaytree(node.left)
        print("Vlaue of Node {}".format(node.val), "and the Height {}".format(node.height))
        self.displaytree(node.right)
        
    def balance(self):
        return self.balanceTree(self.root)
        
    def balanceTree(self, node):
        if node == None:
            return True
        if abs(self.height(node.left) - self.height(node.right)) <= 1:
            return (self.balanceTree(node.left) and self.balanceTree(node.right))
        else:
            return False
    
    def rotate(self, node, val):
        if (self.height(node.left) - self.height(node.right)) > 1:
            if val < node.left.val:
                return self.rightRotate(node)
            if val > node.left.val:
                node.left = self.leftRotate(node)
                return self.rightRotate(node)
        if (self.height(node.right) - self.height(node.left)) > 1:
            if val > node.right.val:
                return self.leftRotate(node)
            if val < node.right.val:
                node.right = self.rightRotate(node)
                return self.leftRotate(node)
            
        return node
    
    def leftRotate(self, node):
        c = node.right
        t = c.left
        
        c.left = node
        node.right = t

        node.height = max(self.height(node.left), self.height(node.right)) + 1
        c.height = max(self.height(c.left), self.height(c.right)) + 1
        
        return c
    
    def rightRotate(self, node):
        c = node.left
        t = c.right
        
        c.right = node
        node.left = t 
        
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        c.height = max(self.height(c.left), self.height(c.right)) + 1
        
        return c
        
if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.addel()

    print("Displaying the tree:")
    tree.display()
    
    print("\ncheck if the tree is balanced or not")
    print(tree.balance())