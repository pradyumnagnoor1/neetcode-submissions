# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        return the depth of the tree
        The depth of a binary tree is defined as the number of nodes 
        along the longest path from the root node down to the farthest leaf node.
        """

        def dfs(node):
            if node is None:
                return 0

            left_depth = dfs(node.left) #the depth of the left side of root
            right_depth = dfs(node.right) #depth of the right side of root

            maxDepth = max(left_depth, right_depth) + 1

            return maxDepth

        return dfs(root)        