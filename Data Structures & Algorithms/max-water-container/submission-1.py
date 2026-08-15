class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            lower = min(heights[l], heights[r])
            if (r - l) * lower > max_area:
                max_area = (r - l) * lower
            if heights[l] == lower:
                l += 1
            else:
                r -= 1
        return max_area
            