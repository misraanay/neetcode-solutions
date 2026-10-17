class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        for i, (x, y) in enumerate(points):
            heap.append((x**2+y**2, i))
        
        heapq.heapify(heap)

        res = []
        for run in range(k):
            res.append(points[heapq.heappop(heap)[1]])
        
        return res
