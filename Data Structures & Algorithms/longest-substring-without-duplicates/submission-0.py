class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        L, window = 0, set(s[0])
        longest = 1
        for R in range(1, len(s)):
            if s[R] not in window:
                window.add(s[R])
                longest = max(longest, len(window))
            else:
                while s[R] in window and L < R:
                    window.remove(s[L])
                    L+=1
                window.add(s[R])
        return longest