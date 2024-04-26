class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # size = len(matrix)
        # prev_row = [0] * size
        # for row in matrix:
        #     curr_row = [0] * size
        #     for i, n in enumerate(row):
        #         l = max(0, i-1)
        #         r = min(size, i+2)
        #         curr_row[i] = min(prev_row[l:r]) + n
        #     prev_row = curr_row
        # return min(prev_row)
        
        size = len(grid)
        if size == 1:
            return grid[0][0]

        prev_row = [0] * size
        for row in grid:
            curr_row = [0] * size
            for i, n in enumerate(row):
                curr_row[i] = n + min(prev_row[0:i] + prev_row[i+1:size])
            prev_row = curr_row
        return min(prev_row)
