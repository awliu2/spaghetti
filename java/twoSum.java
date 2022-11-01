import java.util.*;

public class twoSum {
    int[] nums;
    int target;
    
    public twoSum(int[] n, int t) {
        nums = n;
        target = target;
    }

    static int[] soln() {
        int n = nums.length;
        Map<Integer,Integer> map=new HashMap<>();
        int[] rv = new int[2];
        for (int i = 0; i < n; i++) {
            if (map.containsKey(target - nums[i])) {
                rv[0] = i;
                rv[1] = map.get(target - nums[i]);
                return rv;
            }
            else {
                map.put(nums[i], i);
            }
        }
        return rv;
    }

    // playing around with static and non-static attributes and methods
    public static void main(String[] args) {
        int[] nums1 = [1, 2, 4, 7, 8];
        int[] nums2 = [5, 3, 2, 6, 7];

        twoSum s = new twoSum(nums1, 6);
        

        int[] rv1 = s.soln();
        System.out.println(Arrays.toString(rv1));
        // System.out.println(Arrays.toString(rv2));
    }
}


