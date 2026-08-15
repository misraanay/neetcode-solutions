class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1
        outer_list = [[] for _ in range(len(nums) + 1)] # no element at zeroeth index
        for num, count in map.items():
            outer_list[count].append(num)
        most_freq = []
        for i in range(len(nums), 0, -1):
            for num in outer_list[i]:
                most_freq.append(num)
                if len (most_freq) == k:
                    return most_freq