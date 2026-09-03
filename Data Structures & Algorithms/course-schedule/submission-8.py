class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)} #intializing hash map with all courses
        visited = set() #set for keeping track of visited nodes

        for course, prereq in prerequisites: # initializing each course with specified pre reqs
            preMap[course].append(prereq) #appending the prereq to the specified course


        def dfs(course):
            if course in visited: #if the course is in the set then a cycle is detected so false
                return False

            if preMap[course] == []: #if the coures
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



        