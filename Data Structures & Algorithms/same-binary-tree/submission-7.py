# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(p,q):

            if not p and not q:
                return True
            if p and q and p.val==q.val:
                pass
            else:
                return False

            return dfs(p.left,q.left) and dfs(p.right,q.right)

        final=dfs(p,q)
        return final