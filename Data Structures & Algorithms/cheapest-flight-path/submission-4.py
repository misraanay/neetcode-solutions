class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        distance = {i: float("inf") for i in range(n)}
        distance[src] = 0

        for i in range(k+1):
            new_dist = distance.copy()
            for source, destination, cost in flights:
                if distance[source] == float("inf"):
                    continue
                new_dist[destination] = min(new_dist[destination], distance[source] + cost)
            distance = new_dist
        if distance[dst] == float("inf"):
            return -1
        return distance[dst]