class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = set()
        num_islands = 0

        def bfs(i, j, visited):
            queue = deque()
            queue.append((i,j))
            visited.add((i,j))

            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()

                    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nc < 0 or nr >=  m or nc >=  n or grid[nr][nc] == "0" or (nr, nc) in visited:
                            continue
                        visited.add((nr, nc))    
                        queue.append((nr, nc))

        for r in range(m):
            for c in range(n):
                if (r,c) not in visited and grid[r][c] == "1":
                    num_islands += 1
                    bfs(r, c, visited)


        return num_islands

