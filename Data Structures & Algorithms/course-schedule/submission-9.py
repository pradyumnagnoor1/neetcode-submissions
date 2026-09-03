class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)} #intializing hash map with all courses
        visited = set() #set for keeping track of visited nodes

        for course, prereq in prerequisites: # initializing each course with specified pre reqs
            preMap[course].append(prereq) #appending the prereq to the specified course


        def dfs(course):
            if course in visited: #if the course is in the set then a cycle is detected so false
                return False

            if preMap[course] == []: #if the course has no prereqs then return True for that dfs call
                return True

            visited.add(course) #adds the course to the set after base case checks dont execute

            for prereq in preMap[course]: #this investigates the prereqs for the current course
                if dfs(prereq) == False: #if the dfs call for the prereq returns false then its false
                    return False

            visited.remove(course) #once all prereqs explored then remove the course from the set 

            preMap[course] = [] #then set the course prereq list to empty since all been explored

            return True #returns True by default if none of the false ones execute

        for course in range(numCourses): #explore course by course now
            if dfs(course) == False: # run dfs on the course and if any returns false then false
                return False

        return True #returns true by default



        