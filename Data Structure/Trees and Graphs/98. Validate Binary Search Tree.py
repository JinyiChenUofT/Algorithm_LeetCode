# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root):
        
        def inorder(root):
            if not root:
                return True

            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False

            self.prev = root.val
            return inorder(root.right)
        self.prev = -math.inf
        return inorder(root)

root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
s = Solution()
s.isValidBST(root)