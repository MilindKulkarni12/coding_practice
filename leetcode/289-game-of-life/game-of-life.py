class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows = len(board)
        cols = len(board[0])
        new_board = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for i in range(max(0, row-1), min(rows, row+2)):
                    for j in range(max(0, col-1), min(cols, col+2)):
                        if i == row and j == col:
                            continue  # same cell
                        live_neighbors += 1 if board[i][j] == 1 else 0
                if board[row][col] == 1 and live_neighbors in [2, 3]:
                    new_board[row][col] = 1
                if live_neighbors == 3:
                    new_board[row][col] = 1
                
        # print(new_board)
        for i in range(rows):
            for j in range(cols):
                board[i][j] = new_board[i][j]
