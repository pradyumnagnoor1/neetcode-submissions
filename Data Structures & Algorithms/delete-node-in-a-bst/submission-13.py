class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        #so deleting node first involves searching for node
        #then it involves deleting node and handling its children
        #There are 3 cases for handling child nodes
        #1 is no children, 2 is left or right child and 3 is both children 
        #3rd case involves finding the in order successor and setting the parent node val to the successor node val
        #finding the successor node involves finding the min value in the right child subtree

        def find_min(curr):
            while curr.left:
                curr = curr.left
            return curr

        def dfs(node, key):

            if not node:
                return None

            elif node.val > key:
                node.left = dfs(node.left, key)

            elif node.val < key:
                node.right = dfs(node.right, key)

            else:
                if not node.left and not node.right:
                    return None

                if not node.right and node.left:
                    return node.left

                if not node.left and node.right:
                    return node.right

                else:
                    successor = find_min(node.right)
                    node.val = successor.val
                    node.right = dfs(node.right, successor.val)

            return node

        return dfs(root, key)