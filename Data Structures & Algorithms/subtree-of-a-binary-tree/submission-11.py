class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def same_tree(p, q):

            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            return same_tree(p.left, q.left) and same_tree(p.right, q.right)
        

        def dfs(node, subNode):

            if not node:
                return False

            if same_tree(node, subNode):
                return True

            return dfs(node.left, subNode) or dfs(node.right, subNode)

        return dfs(root, subRoot)