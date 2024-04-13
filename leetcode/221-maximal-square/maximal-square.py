class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        squares = defaultdict(int)
        
        def fx(r, c):
            if r >= rows or c >= cols:
                return 0

            if not squares.get((r, c), False):
                bottom = fx(r+1, c)
                diag = fx(r+1, c+1)
                right = fx(r, c+1)

                if matrix[r][c] == '1':
                    squares[(r, c)] = 1 + min(bottom, diag, right)
                else:
                    squares[(r, c)] = 0
            return squares[(r, c)]
        
        fx(0, 0)
        max_side = max(list(squares.values()))
        return max_side ** 2
