 #Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # the successor is somewhere lower in the right subtree
        # successor: one step right and then left till you can
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
        
        # the successor is somewhere upper in the tree
        stack, inorder = [], float('-inf')
        
        # inorder: left, root, right
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            if inorder == p.val:
                return root
            inorder = root.val
            print(inorder)
            
            root = root.right
        return None

root = TreeNode(2)
root.left = TreeNode(1) 
root.right = TreeNode(33)
root.right.left = TreeNode(25) 
root.right.left.left = TreeNode(11) 
root.right.left.left.left = TreeNode(7)
root.right.left.left.right = TreeNode(12)       
s = Solution()
s.inorderSuccessor(root,TreeNode(12))