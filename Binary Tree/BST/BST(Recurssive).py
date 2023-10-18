class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def addel(self):
        print("Enter the value to be enterd")
        val = int(input())
        if self.root == None:
            self.root = TreeNode(val)
        else:
            self.addelement(val, self.root)

    def addelement(self, val, node):
        
        if val < node.val:
            if node.left == None:
                node.left = TreeNode(val)
            else:
                self.addelement(val, node.left)
              
        else: 
            if node.right == None:
                node.right = TreeNode(val)
            else:
                self.addelement(val, node.right)
    
            
    def display(self):
        self.displaytree(self.root)
    def displaytree(self, node):
        if node == None:
            return
        print(node.val)
        self.displaytree(node.left)
        self.displaytree(node.right)
        
if __name__ == "__main__":
    tree = BinarySearchTree()
    while True:
        print("Enter True if you want to enter value else False")
        ans = input().lower() == 'true'
        if ans:
            tree.addel()
        else:
            break
    tree.display()