class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0 for i in range(n)] for j in range(m)]
        dp[m-1][n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if j + 1 < n:
                    dp[i][j] += dp[i][j+1]
                if i + 1 < m:
                    dp[i][j] += dp[i+1][j]

        return dp[0][0]

        