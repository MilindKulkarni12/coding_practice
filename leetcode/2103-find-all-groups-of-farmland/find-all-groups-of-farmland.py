class Solution:
    def findFarmland(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        count = 0

        def floodfill(i, j):
            if i >= 0 and i < n and j >= 0 and j < m and grid[i][j] == 1:
                # print(i, j)
                grid[i][j] = 0
                i1, j1 = floodfill(i-1, j)
                i2, j2 = floodfill(i+1, j)
                i3, j3 = floodfill(i, j-1)
                i4, j4 = floodfill(i, j+1)
                return (max(i, i1, i2, i3, i4), max(j, j1, j2, j3, j4))
            return (-1, -1)
        
        res = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    min_x, min_y = i, j
                    max_x, max_y = floodfill(i, j)
                    max_x = max(min_x, max_x)
                    max_y = max(min_y, max_y)

                    res.append([min_x, min_y, max_x, max_y])
        
        return res
