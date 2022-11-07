class Solution {
    public int orangesRotting(int[][] grid) {
        int nRows = grid.length;
        int nCols = grid[0].length;

        Queue<int[]> qu = new LinkedList<>();
        int nFresh = 0;
        int[] delimit = new int[]{-1, -1};
        for (int r = 0; r < nRows; r++)
        {
            for (int c = 0; c < nCols; c++)
            {
                if (grid[r][c] == 1) nFresh++; 
                else if (grid[r][c] == 2)
                {
                    int[] pos = new int[]{r,c};
                    qu.add(pos);
                };
            }
        }
        qu.add(delimit);
        
        int rv = 0;
        int[][] directions = {{-1, 0},{1, 0},{0, -1},{0, 1}};
        while (!qu.isEmpty())
        {
            int[] pos = qu.poll();
            if (pos[0] == -1)
            {
                rv++;
                if (!qu.isEmpty()) qu.add(pos);
            }
            else
            {
                for (int[] d: directions)
                {
                    int rNew = pos[0] + d[0], cNew = pos[1] + d[1];
                    
                    if (!((0 <= rNew && rNew < nRows) &&  
                        (0 <= cNew && cNew < nCols))) continue;
                    else 
                    {
                        if (grid[rNew][cNew] == 1)
                        {
                            grid[rNew][cNew] = 2;
                            nFresh--;
                            int[] newPos = {rNew, cNew};
                            qu.add(newPos);
                        }
                    }
                }
            } 
        }
        if (nFresh == 0) return rv - 1;
        return -1; 
    }
}