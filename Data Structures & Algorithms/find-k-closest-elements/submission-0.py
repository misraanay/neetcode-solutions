class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        newarr = [(abs(num - x), i) for i, num in enumerate(arr)]

        heapq.heapify(newarr)
        res = []

        count = 0
        while count < k:

            diff, idx = heapq.heappop(newarr)
            res.append(arr[idx])

            count += 1
        
        return sorted(res)
