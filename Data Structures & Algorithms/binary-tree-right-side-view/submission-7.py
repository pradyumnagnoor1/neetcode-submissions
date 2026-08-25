from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        final = []
        q = deque()

        if not root:
            return final

        else:
            q.append(root)

        while q:
            levelSize = len(q)
            for n in range(levelSize):
                curr = q.popleft()

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

                if n == levelSize - 1:
                    final.append(curr.val)

        return final





        