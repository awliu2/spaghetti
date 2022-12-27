import java.util.*;
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> rv = new ArrayList<>();
        int nRows = matrix.length;
        int nCols = matrix[0].length;

        int rBegin = 0;
        int rEnd = nRows - 1;
        int cBegin = 0;
        int cEnd = nCols - 1;

        while (rBegin <= rEnd && cBegin <= cEnd)
        {
            // left
            for (int c = cBegin; c <= cEnd; c++)
            {
                rv.add(matrix[rBegin][c]);
            }
            rBegin++;
            
            // down
            for (int r = rBegin; r <= rEnd; r++)
            {
                rv.add(matrix[r][cEnd]);
            }
            cEnd--;

            // right
            if (rBegin <= rEnd)
            {
                for (int c = cEnd; c >= cBegin; c--)
                {
                    rv.add(matrix[rEnd][c]);
                }
                rEnd--;
            }
            
            
            // up
            if (cBegin <= cEnd)
            {
                for (int r = rEnd; r >= rBegin; r--)
                {
                    rv.add(matrix[r][cBegin]);
                }
                cBegin++;
            }
        }
        return rv;
    }
}