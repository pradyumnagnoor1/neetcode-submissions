# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def find_min(curr):
            while curr.left:
                curr = curr.left
            return curr

        def dfs(node, key):
            if not node:
                return None

            if node.val < key:
                node.right = dfs(node.right, key)

            elif node.val > key:
                node.left = dfs(node.left, key)

            else:
                if not node.left and not node.right:
                    return None
                
                if node.left and not node.right:
                    return node.left

                if node.right and not node.left:
                    return node.right

                else:
                    successor = find_min(node.right)
                    node.val = successor.val
                    node.right = dfs(node.right, successor.val)

            return node

        return dfs(root, key)


                


        