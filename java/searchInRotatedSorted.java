class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;
        // int counter = 0;
        while (l <= r) {
            if (nums[l] == target) return l;
            if (nums[r] == target) return r;
            // counter += 1;
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) return mid;

            // mid > start, pivot is after mid
            if (nums[l] <= nums[mid]) {
                if (target >= nums[l] && target < nums[mid]) r = mid - 1;
                else l = mid + 1;
            }
            else {
                if (target <= nums[r] && target > nums[mid]) l = mid + 1;
                else r =  mid - 1;
            }
        }
        return -1;
    }
}