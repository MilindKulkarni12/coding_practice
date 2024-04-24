class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])

        def capture(r, c):
            if r < 0 or c < 0 or r == n or c == m or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        for r in range(n):
            for c in range(m):
                if board[r][c] == "O" and (r in [0, n - 1] or c in [0, m - 1]):
                    capture(r, c)

        for r in range(n):
            for c in range(m):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(n):
            for c in range(m):
                if board[r][c] == "T":
                    board[r][c] = "O"
    