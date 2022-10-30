class Solution {
    public int climbStairs(int n) {
        if (n == 0 || n == 1) return n;
        int prevPrev = 1;
        int prev = 2;
        
        for (int i = 2; i < n; i++) {
            int temp = prevPrev + prev;
            prevPrev = prev;
            prev = temp;
        }
        return prev;
    
    }
}
