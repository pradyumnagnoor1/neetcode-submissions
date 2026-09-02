class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        visited = set()

        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        def dfs(course):
            # Cycle found
            if course in visited:
                return False

            # Already checked / no prerequisites
            if not preMap[course]:
                return True

            visited.add(course)

            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False

            # Remove from current DFS path
            visited.remove(course)

            # Mark course as fully processed / safe
            preMap[course] = []

            return True

        # Check every course
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
        