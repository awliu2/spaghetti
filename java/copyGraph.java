import java.util.*;
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}


class Solution {
    Map<Integer, Node> oldToNew = new HashMap<>();

    public Node dfs(Node node)
    {
        if (oldToNew.containsKey(node.val))
        {
            return oldToNew.get(node.val);
        }
        else
        {   
            Node copy = new Node(node.val);
            oldToNew.put(node.val, copy);
            for (Node neighbor: node.neighbors)
            {
                Node neighbor_search = dfs(neighbor);
                copy.neighbors.add(dfs(neighbor_search));
            }
            return copy;
        }
    }
    public Node cloneGraph(Node node) {
        if (node == null) return null;
        return dfs(node);
    }
}