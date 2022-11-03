class Solution {
    public List<List<Integer> > pacificAtlantic(int[][] heights) {
        List<List<Integer> > rv = new ArrayList<>();

        int nRows = heights.length;
        int nCols = heights[0].length;
        

        List<List<Integer> > pCoast = new ArrayList<>();
        List<List<Integer> > aCoast = new ArrayList<>();
        
        for (int r = 0; r < nRows; r++) {
            List<Integer> pCoord = new ArrayList<>();
            pCoord.add(r);
            pCoord.add(0);
            // avoid duplicate coord (top left corner)
            if (r != 0) pCoast.add(pCoord);

            List<Integer> aCoord = new ArrayList<>();
            aCoord.add(r);
            aCoord.add(nCols - 1);
            // avoid duplicate coord (bottom right corner)
            if (r != nRows - 1) aCoast.add(aCoord);
        }
        
        for (int c = 0; c < nCols; c++) {
            List<Integer> pCoord = new ArrayList<>();
            pCoord.add(0);
            pCoord.add(c);
            pCoast.add(pCoord);
            List<Integer> aCoord = new ArrayList<>();
            aCoord.add(nRows - 1);
            aCoord.add(c);
            aCoast.add(aCoord);
        }

        System.out.println("pCoast:" );
        System.out.println(pCoast);
        System.out.println(aCoast);
        // sets of points that flow into each ocean
        Set <List<Integer> > toPacific = new HashSet<>();
        Set <List<Integer> > toAtlantic = new HashSet<>();
        
        for (List<Integer> coord: pCoast)
        {
            int r = coord.get(0), c = coord.get(1);
            dfs(heights, toPacific, heights[r][c],
            r, c, nRows, nCols);
        }


        for (List<Integer> coord: aCoast)
        {
            int r = coord.get(0), c = coord.get(1);
            
            dfs(heights, toAtlantic, heights[r][c], 
                r, c, nRows, nCols);
        }
        
        toPacific.retainAll(toAtlantic);

        for (List<Integer> coord: toPacific)
        {
            rv.add(coord);
        }
        return rv;
    }

    public void dfs(int[][] heights, Set<List<Integer> > toOcean, 
                    int prevHeight, int r, int c, int nRows, int nCols) 
    {

        if ((r < 0 || r >= nRows) || (c < 0 || c >= nCols) || (heights[r][c] < prevHeight)) return; 
        List<Integer> listCoord = new ArrayList<>();
        listCoord.add(r);
        listCoord.add(c);
        if (toOcean.contains(listCoord))
        {
            return;
        }
        else
        {
            int[][] directions = {
                {-1, 0}, {1, 0}, {0, -1}, {0, 1}
            };
            toOcean.add(listCoord);
            int height = heights[r][c];
            for (int[] d : directions)
            {
                int d_r = d[0];
                int d_c = d[1];
                dfs(heights, toOcean, height, r + d_r, c + d_c, nRows, nCols);
            }
        }   
    }
}