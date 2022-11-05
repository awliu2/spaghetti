import java.util.*;
class MinStack {
    Stack<Integer> fS = new Stack<>();
    Stack<Integer> minS = new Stack<>();
    public MinStack() {
        fS =  new Stack<>();
        minS = new Stack<>();
    }

    public void push(int val) {
        fS.push(val);
        if (minS.size() == 0 || val <= minS.peek()) minS.push(val);
    }

    public void pop() {
        int last = fS.pop();
        if (minS.peek() == last) minS.pop();
    }

    public int top() {
        return fS.peek();
    }

    public int getMin() {
        return minS.peek();
    }
}