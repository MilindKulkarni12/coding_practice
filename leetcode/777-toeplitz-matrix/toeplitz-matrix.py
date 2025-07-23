class Solution:
    def check_toeplitz(self, i, j, m, n, mat):
        og = mat[i][j]
        while i < m and j < n:
            if mat[i][j] == og:
                i += 1
                j += 1
            else:
                i = j = -1
                break
        return i != -1

    def isToeplitzMatrix(self, mat: List[List[int]]) -> bool:
        ans = True
        m, n = len(mat), len(mat[0])
        for i in range(0, m):
            for j in range(0, n):
                if i != 0 and j > i:
                    break
                if i > 0 and j > 0 and i > j:
                    break
                ans = ans and self.check_toeplitz(i, j, m, n, mat)
        return ans