class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        atl, pac = set(), set()


        def dfs(r, c, visited, prev):
            if min(r,c) < 0 or r >= m or c >= n or (r,c) in visited or prev > heights[r][c]:
                return
            visited.add((r,c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])

        for c in range(n):
            dfs(0, c, pac, 0)
            dfs(m-1, c, atl, 0)

        for r in range(m):
            dfs(r, 0, pac, 0)
            dfs(r, n-1, atl, 0)

        final_set = atl.intersection(pac)
        return [[r, c] for r,c in final_set]