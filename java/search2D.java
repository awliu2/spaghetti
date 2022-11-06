class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int numRows = matrix.length;
        int numCols = matrix[0].length;
        // System.out.printf("%d, %d\n",numRows, numCols);
        int target_row = 0;
        while (matrix[target_row][numCols - 1] < target)
        {
            target_row++;
            if (target_row > numRows - 1) return false;
        }
        
        // System.out.println(target_row);
        int l = 0;
        int r = numCols;
        while (l < r)
        {
            int mid = (l + r) / 2;
            //System.out.println(matrix[target_row][mid]);
            if (matrix[target_row][mid] == target) return true;
            else if (matrix[target_row][mid] < target) l = mid + 1;
            else r = mid;
        }

        return false;

    }
}
