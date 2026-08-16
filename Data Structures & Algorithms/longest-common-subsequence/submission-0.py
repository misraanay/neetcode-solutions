class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for j in range(n)] for i in range(m)]

        dp[m-1][n-1] = 0 + (text1[m-1] == text2[n-1])

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                res = 0
                if text1[i] == text2[j]:
                    if i + 1 < m and  j + 1 < n:
                        res = 1 + dp[i+1][j+1]
                    else:
                        res = 1
                else:
                    if i + 1 < m:
                        res = max(res, dp[i+1][j])
                    if j + 1 < n:
                        res = max(res, dp[i][j+1])
                dp[i][j] = res
        return dp[0][0]
            
                    
                    

