class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def addVal(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            n = self.root
            while True:
                if value < n.val:
                    if n.left == None:
                        n.left = Node(value)
                        break
                    n = n.left
                else:
                    if n.right == None:
                        n.right = Node(value)
                        break
                    n = n.right
        print("Enter True if you want to continue else False")
        ans = input().lower() == 'true'
        if not ans:
            return self.root
        val = int(input(print("Enter the valur to be inserted in BST")))
        return self.addVal(val)
    def printNode(self, root):
        if root == None:
            return
        print(root.val)
        self.printNode(root.left)
        self.printNode(root.right)
if __name__ == '__main__':
    val = int(input(print("Enter the first value to be entred")))
    node = BinarySearchTree()
    root = node.addVal(val)
    node.printNode(root)