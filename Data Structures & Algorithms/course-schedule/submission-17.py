class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prevMap = {i: [] for i in range(numCourses)}
        visited = set()

        for prereq, course in prerequisites:
            prevMap[course].append(prereq)

        def dfs(course):
            if course in visited:
                return False

            if not prevMap[course]:
                return True

            visited.add(course)

            for prereq in prevMap[course]:
                if dfs(prereq) == False:
                    return False

            visited.remove(course)
            prevMap[course] = []

            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return False

        return True