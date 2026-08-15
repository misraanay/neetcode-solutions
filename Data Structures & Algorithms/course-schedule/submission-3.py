class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hash = {i: [] for i in range(numCourses)} # adj list

        for cur, pre in prerequisites:
            hash[cur].append(pre)

        visited = set()
        def dfs(cur):
            if cur in visited:
                return False
            visited.add(cur)
            for neigh in hash[cur]:
                if not dfs(neigh):
                    return False
            visited.remove(cur)
            hash[cur] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

            
