class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        
        adj = {i: [] for i in range(n)}

        for source, dest, w in edges:
            adj[source].append((dest, w))

        pq = [[0, src]]
        path = {}

        while pq:
            weight, node = heapq.heappop(pq)

            if node in path:
                continue

            path[node] = weight
            for ni, wi in adj[node]:
                heapq.heappush(pq, [weight + wi, ni])


        for i in range(n):
            if i not in path:
                path[i] = -1
        return path 
