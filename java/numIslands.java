class Solution {
    int [][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public int numIslands(char[][] grid) {
        int rv = 0;
        int num_rows = grid.length;
        int num_cols = grid[0].length;
        boolean[][] checked_grid = new boolean[num_rows][num_cols];
        for (int r = 0; r < num_rows; r++)
        {
            for (int c = 0; c < num_cols; c++)
            {
                checked_grid[r][c] = false;
            }
        }

        for (int r = 0; r < num_rows; r++)
        {
            for (int c = 0; c < num_cols; c++)
            {
                if (checked_grid[r][c]) continue;
                
                checked_grid[r][c] = true;
                if (grid[r][c] == '0') continue;
                else
                {
                    rv++;
                    grid[r][c] = '1';
                    dfs(grid, r, c, num_rows, num_cols);
                }
            }
        }
        return rv;
    }

    public void dfs(char[][] grid, int r, int c, int nr, int nc)
    {
        if ((r < 0) || (r >= nr) || (c < 0) || (c >= nc)) return;
        if (grid[r][c] == '0') return;
        grid[r][c] = '0';
        for (int[] d: directions)
        {
            dfs(grid, r + d[0], c + d[1], nr, nc);
        }
    }
}