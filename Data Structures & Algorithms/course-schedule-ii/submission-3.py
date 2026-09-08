class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        prevMap = {i: [] for i in range(numCourses)}
        res = []
        visited = set()
        visiting = set()
        

        for course, prereq in prerequisites:
            prevMap[course].append(prereq)

        def dfs(course):
            if course in visiting:
                return False

            if course in visited:
                return True

            visiting.add(course)


            for prereq in prevMap[course]:
                if not dfs(prereq):
                    return False

            visiting.remove(course)
            visited.add(course)

            res.append(course)

            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return []

           
        return res

        



            



        