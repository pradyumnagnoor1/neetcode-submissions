# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Given a binary tree, return true if it is height-balanced
        False otherwise.
        eight-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
        """

        #best way to approach this is via a postOrder DFS 
        balanced=True
        def dfs(node):
            if not node:
                return 0
            leftDepth=dfs(node.left)
            rightDepth=dfs(node.right)
            maxDepth=max(rightDepth,leftDepth)+1

            if rightDepth>leftDepth+1 or leftDepth>rightDepth+1:
                nonlocal balanced
                balanced=False
            
            return maxDepth
        
        dfs(root)
        return balanced