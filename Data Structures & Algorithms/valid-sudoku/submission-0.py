class Solution:
    def isValidArray(self, array: List[str]) -> bool:
        filledArr = [x for x in array if x != '.']
        filledSet = set(filledArr)
        return len(filledSet) == len(filledArr)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows
        for row in range(len(board)):
            if not self.isValidArray(board[row]): return False

        #cols
        for col in range(len(board[0])):
            colArr = [board[row][col] for row in range(len(board))]
            if not self.isValidArray(colArr): return False

        #boxes
        box_starts = [(i, j) for i in range(0, len(board), 3) for j in range(0, len(board), 3)]
        for r, c in box_starts:
            boxArr = [board[r+i][c+j] for i in range(3) for j in range(3)]
            if not self.isValidArray(boxArr): return False

        return True