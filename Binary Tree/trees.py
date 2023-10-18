class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def adds(self):
        value = int(input(print("Enter the root node val")))
        self.root = Node(value)
        self.addelements(self.root)
        
    def printN(self):
        self.printNode(self.root)
        
    def addelements(self, node):
        print("do want to enter the left side of {}, Enter True or False".format(node.val))
        Left = input().lower() == 'true'
        if Left == True:
            val = input(print("Enter the value to be inserted"))
            l = node.left = Node(val)
            self.addelements(l)
            
        print("do want to enter the right side of {}, Enter True or False".format(node.val))
        Right = input().lower() == 'true'
        if Right:
            val = input(print("Enter the value to be inserted"))
            r = node.right = Node(val)
            self.addelements(r)
           

    def printNode(self, node):
        if node == None:
            return
        print(node.val)
        self.printNode(node.left)
        self.printNode(node.right)
        
if __name__=="__main__":
    ans = BinaryTree()
    ans.adds()
    ans.printN()
        
            
                    
                