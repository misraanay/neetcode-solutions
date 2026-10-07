class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:

        matrix = []

        for row in boxGrid:
            replace = []
            stones = 0
            spaces = 0
            for i, char in enumerate(row):
                if char == ".":
                    spaces += 1
                elif char == "#":
                    stones += 1
                else:
                    replace += ["." for _ in range(spaces)] + ["#" for _ in range(stones)] + ["*"]
                    stones = 0
                    spaces = 0
            replace += ["." for _ in range(spaces)] + ["#" for _ in range(stones)]
            matrix.append(replace)

        def transpose(matrix):
            m = len(matrix)
            n = len(matrix[0])
            res = [["" for _ in range(m)] for j in range(n)]
            for i in range(m):
                for j in range(n):
                    res[j][m-1-i] = matrix[i][j]
            return res
        return transpose(matrix)
