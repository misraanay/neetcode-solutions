class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort() # O (n log n)
        res = 0
        n = len(people)
        l, r = 0, n-1

        while l < r:
            if people[l] + people[r] > limit:
                r -= 1
            else:
                r -= 1
                l += 1
            res += 1
        if l == r:
            return res + 1
        return res

        


        






        