class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0

        def floodfill(i, j):
            if i >= 0 and i < n and j >= 0 and j < m and grid[i][j] == '1':
                # print(i, j)
                grid[i][j] = '0'
                floodfill(i-1, j)
                floodfill(i+1, j)
                floodfill(i, j-1)
                floodfill(i, j+1)
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    floodfill(i, j)
        
        return count
