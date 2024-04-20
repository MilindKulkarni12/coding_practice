class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_area = 0

        def floodfill(i, j):
            if i >= 0 and i < n and j >= 0 and j < m and grid[i][j] == 1:
                # print(i, j)
                area = 1
                grid[i][j] = 0
                area += floodfill(i-1, j)
                area += floodfill(i+1, j)
                area += floodfill(i, j-1)
                area += floodfill(i, j+1)
                return area
            return 0
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    curr_area = floodfill(i, j)
                    max_area = max(max_area, curr_area)
        
        return max_area
