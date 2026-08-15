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

        
        comp = 0
        num_visited = 0
        for i in range(n):
            dfs(i, -1)
            if num_visited < len(visited):
                comp+=1
                num_visited = len(visited)
        return comp
