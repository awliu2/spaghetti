class Solution {
    public int trap(int[] height) {
        int n = height.length;
        int maxLeft = height[0];
        int maxRight = height[n - 1];
        int l = 0, r = n - 1;
        int rv = 0;
        while (l < r)
        {
            if (height[l] < height[r])
            {
                if (height[l] > maxLeft)
                {
                    maxLeft = height[l];
                }
                else
                {
                    rv += maxLeft - height[l];
                }
                l++;
            }
            else
            {
                if (height[r] > maxRight)
                {
                    maxRight = height[r];
                }
                else
                {
                    rv += maxRight - height[r];
                }
                r--;
            }
        }
        return rv;
    }
}   