# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxSoFar):
            count = 0

            if node is None:
                return 0

            if node.val >= maxSoFar:
                count += 1
            else:
                count += 0

            newMax = max(node.val, maxSoFar)
            count += dfs(node.left, newMax)
            count += dfs(node.right, newMax)

            return count

        return dfs(root, root.val)

            


        
        