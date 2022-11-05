import java.util.*;
class Solution {
    public boolean isValid(String s) {
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        char[] open = {'(', '{', '['};
        char[] close = {')', '}', ']'};

        for (int i = 0, n = s.length(); i < n; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (s.charAt(i) == open[j])
                {
                    stack.push(j);
                    continue;
                }
                
                if (s.charAt(i) == close[j])
                {
                    if (stack.size() == 0) return false;
                    if (stack.pop() != j) return false;
                    continue;
                }
            }
        }
        return (stack.size() == 0);
    }
}