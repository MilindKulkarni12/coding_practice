class Solution(object):
    def exist(self, board, word):
        self.N = len(board)
        self.M = len(board[0])
        self.board = board

        for row in range(self.N):
            for col in range(self.M):
                if self.backtrack(row, col, word):
                    return True
        return False


    def backtrack(self, row, col, suffix):
        if len(suffix) == 0:
            return True

        if row < 0 or row == self.N or col < 0 or col == self.M \
                or self.board[row][col] != suffix[0]:
            return False

        ret = False
        self.board[row][col] = '#'
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ret = self.backtrack(row + rowOffset, col + colOffset, suffix[1:])
            if ret: 
                break
        self.board[row][col] = suffix[0]

        return ret
