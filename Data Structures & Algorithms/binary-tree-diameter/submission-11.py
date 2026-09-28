# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        def dfs(node):
            nonlocal maxDiameter
            if not node:
                return 0

            left_length = dfs(node.left)
            right_length = dfs(node.right)
            
            diameter = left_length + right_length

            maxDiameter = max(diameter, maxDiameter)

            return 1 + max(left_length, right_length)

        dfs(root)
        return maxDiameter