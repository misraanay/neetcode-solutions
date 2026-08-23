class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        if not height:
            return None

        l, r = 0, n-1
        leftMax, rightMax = height[0], height[n-1]

        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(height[l], leftMax)
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(height[r], rightMax)
                res += rightMax - height[r]

        return res



        


