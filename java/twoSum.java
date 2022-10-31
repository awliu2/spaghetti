import java.util.*;

public class twoSum {
    int[] nums1 = {1, 2, 3, 4, 5};
    int[] nums2 = {4, 1, 3, 5, 8};

    static int[] soln(int[] nums, int target) {
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
        twoSum s = new twoSum();

        int[] rv1 = soln(s.nums1, 8);
        int[] rv2 = soln(s.nums2, 6);
        System.out.println(Arrays.toString(rv1));
        System.out.println(Arrays.toString(rv2));
    }
}


