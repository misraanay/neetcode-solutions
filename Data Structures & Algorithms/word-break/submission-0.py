class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True

        for i in range(n-1, -1, -1):
            for word in wordDict:
                k = len(word)
                if s[i: i + k] == word:
                    dp[i] = dp[i] or dp[i+k]
        return dp[0]
        