class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # dp = {}
        # n = len(matrix)
        
        # def fx(r, c):
        #     print(r, c)
        #     if (r, c) in dp:
        #         return dp[(r, c)]

        #     dp[(r, c)] = matrix[r][c]
        #     if r+1 < n:
        #         dp[(r, c)] += min([fx(r+1, j) for j in range(max(0, c-1), min(n, c+1))])
        #     return dp[(r, c)]

        # l = [fx(0, i) for i in range(len(matrix[0]))]
        # print(l)
        # return min(l)
        size = len(matrix)
        prev_row = [0] * size
        for row in matrix:
            curr_row = [0] * size
            for i, n in enumerate(row):
                l = max(0, i-1)
                r = min(size, i+2)
                curr_row[i] = min(prev_row[l:r]) + n
            prev_row = curr_row
        return min(prev_row)
