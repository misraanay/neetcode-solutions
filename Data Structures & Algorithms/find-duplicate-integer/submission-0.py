class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        temp = fast
        slow = 0
        while True:
            slow = nums[slow]
            temp = nums[temp]
            if slow == temp:
                break

        return slow
    

        




        