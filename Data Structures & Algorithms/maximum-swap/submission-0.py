class Solution:
    def maximumSwap(self, num: int) -> int:

        lst = list(str(num))
        n = len(lst)
        for i, char in enumerate(str(num)):
            maxval, maxind = char, i
            # find rightmost max value
            for j in range(n-1, i, -1):
                if lst[j] > maxval:
                    maxval = lst[j]
                    maxind = j

            if maxind == i:
                continue
            else:
                lst[i] = lst[maxind]
                lst[maxind] = char
                break

        return int("".join(lst))
            



