# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Given the roots of two binary trees root and subRoot
        return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
        """

        def dfs(node,subnode):
            if not node and not subnode:
                return True
            elif node and subnode and node.val!=subnode.val:
                return False
            elif not node or not subnode:
                return False
            
            return dfs(node.left,subnode.left) and dfs(node.right,subnode.right)

        def checkSubtrees(node,subnode):
            if not node:
                return False
            if dfs(node,subnode)==True:
                return True
            
            
            return checkSubtrees(node.right,subnode) or checkSubtrees(node.left,subnode)
            
            #if any are true then you return true

        return checkSubtrees(root,subRoot)
            