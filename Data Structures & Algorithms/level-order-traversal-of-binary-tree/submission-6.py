# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        final = []
        q = deque()


        if not root:
            return final

        else:
            q.append(root)

        while q:
            levelSize = len(q)
            level = []

            for n in range(levelSize):
                curr = q.popleft()
                level.append(curr.val)


                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

            final.append(level)

               


        return final
        