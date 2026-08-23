class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None:
            return False
        m = len(matrix)
        n = len(matrix[0])

        u = 0
        d = m-1
        row = -1
        while u <= d:
            mid = int((u+d)/2)
            if matrix[mid][0] <= target <= matrix[mid][n-1]:
                row = mid
                break
            elif matrix[mid][0] > target:
                d = mid - 1
            else:
                u = mid + 1
            
        if row < 0:
            return False
        
        l = 0
        r = n-1

        while l <= r:
            mid = int((l+r)/2)
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
            

