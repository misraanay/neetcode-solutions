class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        starts = []

        for x in range(len(board)):
            for y in range(len(board[0])):
                if word[0] == board[x][y]:
                    starts.append((x, y))
        # O(n^2) operation
        def exists(num, i, j, visited):
            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0 or visited[i][j]:
                return False
            if word[num] != board[i][j]:
                return False
            if num == len(word) - 1:
                return True
            
            visited[i][j] = True
            if exists(num+1, i-1, j, visited) or exists(num+1, i, j-1, visited):
                return True
            if exists(num+1, i+1, j, visited) or exists(num+1, i, j+1, visited):
                return True
            visited[i][j] = False
            return False
            
        for start in starts:
            matrix = [[False for j in range(len(board[i]))] for i in range(len(board))]
            if exists(0, start[0], start[1], matrix):
                return True
        return False


            
        