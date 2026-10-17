class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        lst = [-1 * num for num in nums]
        heapq.heapify(lst)

        for i in range(k-1):
            heapq.heappop(lst)
        
        return -1 * heapq.heappop(lst)
        