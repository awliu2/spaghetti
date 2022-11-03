import java.util.*;

public class twoSum {
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
}




