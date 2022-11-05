class houseRobber {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];
        int prevPrev = 0;
        int prev = 0;
        for (int i = 0; i < n; i++) {
            int temp = prev;
            prev = Math.max(prevPrev + nums[i], prev);
            prevPrev = temp;
        }
        return prev;       
    }
}