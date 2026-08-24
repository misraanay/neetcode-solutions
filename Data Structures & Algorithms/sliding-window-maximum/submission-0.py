class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n= len(nums) 
        if nums is None or k == 0:
            return []

        l = r = 0
        dq = deque() 
        res = []              

        while r < n:
            while dq and nums[r] > nums[dq[-1]]:
                dq.pop()
            dq.append(r)

            if dq[0] < l:
                dq.popleft()

            if r + 1 >= k:
                l += 1
                res.append(nums[dq[0]])

            r += 1

        return res


        









        
        