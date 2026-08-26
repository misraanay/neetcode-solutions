class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adj = collections.defaultdict(list)

        for i, pair in enumerate(equations):
            a, b = pair
            # for a, b store both edge weights forward and back
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))


        def bfs(a, z):

            if a not in adj or z not in adj:
                return -1.0

            if a == z:
                return 1.0
            
            q, visited = collections.deque(), set()
            q.append((a, 1))

            while q:
                for i in range(len(q)):
                    node, prod = q.popleft()
                    visited.add(a)
                    for neigh, val in adj[node]:
                        if neigh not in visited:
                            if neigh == z:
                                return val * prod
                            q.append((neigh, val * prod))
            return -1.0

        return [bfs(a, z) for a , z in queries]



        