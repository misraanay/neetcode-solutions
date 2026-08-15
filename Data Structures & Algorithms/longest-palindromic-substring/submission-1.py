class Solution:
    def longestPalindrome(self, s: str) -> str:

        dp = [[None for i in range(len(s))] for j in range(len(s))]
        
        def maxPalindrome(i, j):
            if i > j:
                return ""
            if i == j:
                return s[i]
            if dp[i][j] is not None:
                return dp[i][j]
            if s[i] == s[j]:
                inner = maxPalindrome(i+1, j-1)
                if len(inner) == j - i - 1:
                    dp[i][j] = s[i] + inner + s[j]
                    return dp[i][j]
            dp[i][j] = max(maxPalindrome(i+1, j), maxPalindrome(i, j-1), key = len)
            return dp[i][j]
        
        return maxPalindrome(0, len(s) -1)

