class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        visited = set()
        
        for prereq, course in prerequisites:
            preMap[course].append(prereq)

        def dfs(course):

            if course in visited:
                return False

            if preMap[course] == []:
                return True

            visited.add(course)

            for prereq in preMap[course]:
                if dfs(prereq) == False:
                    return False

            visited.remove(course)
            preMap[course] = []
            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return False

        return True