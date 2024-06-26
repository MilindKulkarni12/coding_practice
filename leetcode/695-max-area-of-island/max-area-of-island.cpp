class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int area, max_area = 0, curr_area = 0;
        
        for(int i =0; i < grid.size(); ++i)
            for(int j =0; j < grid[0].size(); ++j) {
                area = 0;
                curr_area = dfs(grid, i, j);
                max_area = max(max_area, curr_area);
            }//for
        return max_area;
    }
    
    int dfs(vector<vector<int>> &grid, int i, int j) {
        if(i < 0 || i >= grid.size() || j < 0 || j >= grid[0].size())
            return 0;
        if(!grid[i][j])
            return 0;
        
        grid[i][j] = 0;
        int area = 1;
        area += dfs(grid, i, j+1);
        area += dfs(grid, i+1, j);
        area += dfs(grid, i, j-1);
        area += dfs(grid, i-1, j);
        return area;
    }//dfs
};