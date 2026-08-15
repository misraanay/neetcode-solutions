class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adjlist = {i: [] for i in range(n)}
        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
        
        visited = set()
        def dfs(cur, prev):
            if cur in visited:
                return

            visited.add(cur)
            for neighbor in adjlist[cur]:
                if neighbor != prev:
                    dfs(neighbor, cur)

        
        num = 0
        for i in range(n):
            if i not in visited:
                num += 1
                dfs(i, -1)
        return num
