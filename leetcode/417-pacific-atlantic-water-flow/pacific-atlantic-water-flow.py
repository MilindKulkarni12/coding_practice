class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, vis, prev_height):
            if r < 0 or r >= n or c < 0 or c >= m or \
                ((r, c) in vis) or heights[r][c] < prev_height:
                return
            vis.add((r, c))
            dfs(r + 1, c, vis, heights[r][c])
            dfs(r - 1, c, vis, heights[r][c])
            dfs(r, c + 1, vis, heights[r][c])
            dfs(r, c - 1, vis, heights[r][c])

        for r in range(n):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, m-1, atl, heights[r][m-1])
        
        for c in range(m):
            dfs(0, c, pac, heights[0][c])
            dfs(n-1, c, atl, heights[n-1][c])

        return [list(i) for i in pac.intersection(atl)]
