class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows = len(matrix)
        Columns = len(matrix[0])
        top = 0
        bottom = Rows - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        

        row = (top + bottom) // 2
        L = 0
        R = len(matrix[row]) - 1
        while L <= R:
            Mid = (L + R) // 2
            if target > matrix[row][Mid]:
                L = Mid + 1
            elif target < matrix[row][Mid]:
                R = Mid - 1
            else:
                return True
        return False
            


            