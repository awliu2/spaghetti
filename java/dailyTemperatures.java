class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
	int[] rv = new int[temperatures.length];

	Stack<Integer> stak = new Stack<>();
	for (int i = 0, n = temperatures.length; i < n; i++)
	{
	    while ((stak.size() != 0) && (temperatures[stak.peek()] < temperatures[i]))
	    {
            int prevDay = stak.pop();
            rv[prevDay] = i - prevDay;
	    }
	    stak.add(i);
	}
	return rv;
    }
}
