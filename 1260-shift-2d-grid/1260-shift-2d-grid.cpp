class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {

        int m = grid.size();
        int n = grid[0].size();

        int total = m * n;

        k %= total;   // Avoid unnecessary full rotations

        vector<vector<int>> ans(m, vector<int>(n));

        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {

                // Convert current position to 1D index
                int oldIndex = i * n + j;

                // Find new index after shifting
                int newIndex = (oldIndex + k) % total;

                // Convert back to 2D coordinates
                int newRow = newIndex / n;
                int newCol = newIndex % n;

                ans[newRow][newCol] = grid[i][j];
            }
        }

        return ans;
    }
};