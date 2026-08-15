class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj_list = {i : [] for i in range(n)}

        for u,v in edges:

            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()

        def dfs(cur, prev):
            if cur in visited:
                return False
            visited.add(cur)
            for child in adj_list[cur]:
                if child != prev:
                    if not dfs(child, cur):
                        return False
            return True


        if not dfs(0, -1):
            return False

        return len(visited) == n