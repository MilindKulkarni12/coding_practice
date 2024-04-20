class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n = len(grid1)
        m = len(grid1[0])
        count = 0

        def floodfill(i, j):
            if i >= 0 and i < n and j >= 0 and j < m and grid2[i][j] == 1:
                # print(i, j)
                grid2[i][j] = 0
                floodfill(i-1, j)
                floodfill(i+1, j)
                floodfill(i, j-1)
                floodfill(i, j+1)
            
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    floodfill(i, j)
        
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1:
                    count += 1
                    floodfill(i, j)
        
        return count