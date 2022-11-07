class TrieNode {
    private TrieNode[] links;
    private int size = 26;
    private boolean isEnd;

    public TrieNode() {
        links = new TrieNode[size];
    }

    public boolean containsKey(char ch) {
        return links[ch - 'a'] != null;
    }
    
    public TrieNode get(char ch)
    {
        return links[ch - 'a'];
    }

    public void put(char ch, TrieNode node) {
        links[ch - 'a'] = node;
    }

    public void setEnd()
    {
        isEnd = true;
    }
    public boolean isEnd() {
        return isEnd;
    }

}

class Trie {
    private TrieNode root;
        
    public Trie() {
        root = new TrieNode();    
    }
    

    public void insert(String word) {
        TrieNode curr = root;
        for (int i = 0, n = word.length(); i < n; i++)
        {
            char ch = word.charAt(i);
            if (!curr.containsKey(ch))
            {
               curr.put(ch, new TrieNode());
            }
            // set new curr_node to the next layer in the trie
            curr = curr.get(ch);
        }
        // set current node as end of word
        curr.setEnd();
    }
    

    public boolean search(String word) {
        TrieNode curr = root;
        for (int i = 0, n = word.length(); i < n; i++)
        {
            char ch = word.charAt(i);
            if (!curr.containsKey(ch)) return false;
            curr = curr.get(ch);
        }
        return curr.isEnd();
    }
    
    public boolean startsWith(String prefix) {
        TrieNode curr = root;
        for (int i = 0, n = prefix.length(); i < n; i++)
        {
            char ch = prefix.charAt(i);
            if (!curr.containsKey(ch)) return false;
            curr = curr.get(ch);
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */