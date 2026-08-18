class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        m = len(s1)
        n = len(s2)

        if m > n:
            return False
        hash1 = {chr(x): 0 for x in range(ord('a'), ord('z') + 1)}
        hash2 = {chr(x): 0 for x in range(ord('a'), ord('z') + 1)}

        for index in range(m):
            hash1[s1[index]] += 1
            hash2[s2[index]] += 1

        if hash1 == hash2:
            return True

        for l in range(m, n):
            hash2[s2[l]] += 1
            hash2[s2[l - m]] -= 1
            if hash1 == hash2:
                return True
        return False

            



