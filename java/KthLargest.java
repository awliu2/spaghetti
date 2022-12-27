import java.util.*;
class KthLargest {
    private int k;
    private PriorityQueue<Integer> minHeap;
    public KthLargest(int k, int[] nums) {
        this.k = k;
        minHeap = new PriorityQueue<>();
        for (int n : nums)
        {
            minHeap.add(n);
        }
        // System.out.println(maxHeap);
        while (minHeap.size() > k)
        {
            minHeap.remove();
            // System.out.println(maxHeap);
        }
    }
    
    public int add(int val) {
        // System.out.println(minHeap);
        minHeap.add(val);
        if (minHeap.size() > k) minHeap.remove();
        return minHeap.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */