class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        def comb(i, curSub, k):
            if len(curSub) == k:
                self.res.append(curSub.copy())
                return
            if i > n:
                return 
            for j in range(i, n + 1):
                curSub.append(j)
                comb(j + 1, curSub, k)
                curSub.pop()
        comb(1, [], k)
        return self.res