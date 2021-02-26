class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            cur_diameter = left + right + 1
            print(left, right)
            print(cur_diameter, self.diameter)
            if cur_diameter > self.diameter:
                self.diameter = cur_diameter
            return max(left, right) + 1
        dfs(root)
        return self.diameter

root = TreeNode(1)
root.left = TreeNode(2) 
root.right = TreeNode(3)
root.left.left = TreeNode(4) 
root.left.right = TreeNode(5) 

s = Solution()
s.diameterOfBinaryTree(root)