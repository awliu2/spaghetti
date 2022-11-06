import java.util.*;

class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> nums = new Stack<>();
        for (String s: tokens)
        {   
            char c = s.charAt(0);
            if (s.length() == 1 && (c == '+' || c == '-' || c == '*' || c == '/'))
            {
                int num2 = nums.pop();
                int num1 = nums.pop();
                int res;
                if (c == '+') res = num1 + num2;
                else if (c == '-') res = num1 - num2;
                else if (c == '*') res = num1 * num2;
                else res = num1 / num2;
                nums.push(res);
            }
            else
            {
                int num = Integer.parseInt(s);
                nums.push(num);
            }
        }
        int rv = nums.pop();
        System.out.printf("Result: %d\n", rv);
        return rv;
    }
}