import java.util.*;

class Solution {
    public int rob(int[] nums) {
        int[] arr2 = Arrays.copyOfRange(nums, 1, nums.length);
        System.out.println(Arrays.toString(arr2));
        return Math.max(rob1(nums), rob1(arr2));
    }
    public int rob1(int[] nums) {
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