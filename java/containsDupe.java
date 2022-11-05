import java.util.*;

class containsDupe {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Boolean> count = new HashMap<>();
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (count.containsKey(nums[i])) {
                if (count.get(nums[i])) {
                    return true;
                }
            }
            else {
                count.put(nums[i], true);
            }
        }   
        return false;
    }
}
