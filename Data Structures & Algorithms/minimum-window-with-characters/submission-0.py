class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        countT = {}
        for char in t:
            countT[char] = countT.get(char, 0) + 1
        have, need = 0, len(t)
        l = 0
        res, resLen = [-1, -1], float("infinity")
        window = {}
        for r, char in enumerate(s):
            window[char] = window.get(char, 0) + 1
            if char in countT and window[char] <= countT[char]:
                have += 1
            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -=1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
        