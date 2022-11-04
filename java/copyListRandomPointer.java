import java.util.*;

// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}


class Solution {
    HashMap<Node, Node> visited = new HashMap<>();

    public Node copyRandomList(Node head) {
        if (head == null) return null;
        if (this.visited.containsKey(head)) return this.visited.get(head);

        Node head_copy = new Node(head.val);
        visited.put(head, head_copy);
        head_copy.next = copyRandomList(head.next);
        head_copy.random = copyRandomList(head.random);
        return head_copy;
    }
}