class TrieNode {
    private TrieNode[] children;
    private final int size = 26;
    private boolean isEnd;

    public TrieNode() {
        children = new TrieNode[size];
    }

    public boolean containsKey(char ch) {
        return !(children[ch - 'a'] == null);
    }

    public TrieNode get(char ch) {
        return children[ch - 'a'];
    }
    
    public void put(char ch, TrieNode child) {
        children[ch - 'a'] = child;
    }

    public boolean isEnd() {
        return isEnd;
    }

    public void setEnd() {
        isEnd = true;
    }
}

class WordDictionary {
    private TrieNode root;
    public WordDictionary() {
        root = new TrieNode();
    }
    
    public void addWord(String word) {
        TrieNode curr = root;
        for (int i = 0, n = word.length(); i < n; i++)
        {
            char ch = word.charAt(i);
            if (!curr.containsKey(ch))
            {
                curr.put(ch, new TrieNode());
            }
            curr = curr.get(ch);
        }
        curr.setEnd();
    }
    
    public boolean search(String word) {
        TrieNode curr = root; 
        return dfs(word, curr);
    }

    public boolean dfs(String word, TrieNode root)
    {
        TrieNode curr = root;
        for (int i = 0, n = word.length(); i < n; i++)
        {
            char ch = word.charAt(i);
            if (ch == '.')
            {
                for (char c = 'a'; c <= 'z'; c++)
                {
                    if (curr.containsKey(c))
                    {
                        if (dfs(word.substring(i + 1), curr.get(c))) return true;
                    }
                }
                return false;
            }
            else
            {
                if (curr.containsKey(ch))
                {
                    curr = curr.get(ch);
                }
                else return false;

            }
        }
        return curr.isEnd();
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */