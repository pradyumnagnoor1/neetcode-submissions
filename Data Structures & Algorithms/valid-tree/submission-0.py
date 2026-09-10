class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        prevMap = {i: [] for i in range(n)}
        visited = set()


        for node1, node2 in edges:
            prevMap[node1].append(node2)
            prevMap[node2].append(node1)



        def dfs(node, prevNode):
            if node in visited:
                return False

            visited.add(node)

            for neighbor in prevMap[node]:
                if neighbor == prevNode:
                    continue

                elif not dfs(neighbor, node):
                    return False

            return True


        if dfs(0,-1) == True and len(visited) == n:
            return True

        else:
            return False
            

            
        