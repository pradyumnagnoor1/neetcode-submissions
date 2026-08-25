class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def same_tree(p, q):
            if not p and not q:
                return True

            if p and not q or not p and q:
                return False

            if p.val != q.val:
                return False

            return same_tree(p.left, q.left) and same_tree(p.right, q.right)

        if root is None:
            return False

        if same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)