class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fact = 1
        answer = []
        for i in range(len(nums)):
            answer.append(fact)
            fact *= nums[i]
        fact = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= fact
            fact *= nums[i]
        return answer     