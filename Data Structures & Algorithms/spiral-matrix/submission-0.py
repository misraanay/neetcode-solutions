class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #right, down, left, up (spiral shape)
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        m = len(matrix)
        n = len(matrix[0])
        pos = [-1, 0]
        cur_dir = 0

        def find_next(pos:List[int], di:List[int]) -> Tuple[int]:
            x, y = (a+b for a, b in zip(pos, di))
            return (x, y)

        def next_bounded(pos:List[int], di:List[int]) -> bool:
            x, y = find_next(pos, di)
            if min(x, y) < 0 or x >= n or y >= m:
                return False
            return True

        res = []
        visited = set()
        while len(res) != m * n:
            x, y = nxt = find_next(pos, directions[cur_dir])
            if next_bounded(pos, directions[cur_dir]) and nxt not in visited:
                visited.add(nxt)
                res.append(matrix[y][x])
                pos = list(nxt)
            else:
                cur_dir = (cur_dir + 1) % 4
        
        return res
            
        



            

    











        