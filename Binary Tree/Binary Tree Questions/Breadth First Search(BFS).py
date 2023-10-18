# https://leetcode.com/problems/binary-tree-level-order-traversal/

def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        node = deque()
        if root: 
            node.append(root)
        while node:
            temp = []
            newnode = []
            while node:
                n = node.popleft()
                temp.append(n.val)
                if n.left:
                    newnode.append(n.left)
                if n.right:
                    newnode.append(n.right)
            ans.append(temp)
            node.extend(newnode)
        return ans
            
            
            