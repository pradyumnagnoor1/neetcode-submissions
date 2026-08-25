# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        

        #post order dfs
        #2 lengths of the subtrees need to be processed and passed back up
        maxDepth=0
        def dfs(node):
            if not node:
                return 0
            
            depthLeft= dfs(node.left)#depth of left subtree
            depthRight= dfs(node.right)#depth of right subtree
            nonlocal maxDepth
            maxDepth=max(depthLeft,depthRight)+1
            return maxDepth
        dfs(root)
        return maxDepth

