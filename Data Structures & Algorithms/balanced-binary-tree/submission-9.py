# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        balanced = True
        def dfs(node):
            if node is None:
                return True


            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            maxDepth = max(right_depth, left_depth) + 1

            if abs(left_depth - right_depth) > 1:
                nonlocal balanced
                balanced = False

            return maxDepth

            


        dfs(root)
        return balanced