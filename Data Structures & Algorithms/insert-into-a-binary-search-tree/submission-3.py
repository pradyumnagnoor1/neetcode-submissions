class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        res = []

        def dfs(node, val):

            if not node:
                return TreeNode(val)

            if node.val > val:
                node.left = dfs(node.left, val)

            elif node.val < val:
                node.right = dfs(node.right, val)

            return node

        return dfs(root, val)