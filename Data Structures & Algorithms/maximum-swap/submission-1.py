class Solution:
    def maximumSwap(self, num: int) -> int:

        res = list(str(num))
        n = len(res)

        maxnum, maxind = res[n-1], n-1
        swp_i = swp_j = n-1

        for i in range(n-2, -1, -1):
            if res[i] > maxnum:
                maxnum, maxind = res[i], i
            if res[i] < maxnum:
                swp_i, swp_j = i, maxind

        tmp = res[swp_i]
        res[swp_i] = res[swp_j]
        res[swp_j] = tmp

        return int("".join(res))
            



