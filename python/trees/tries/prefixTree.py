class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children.keys():
                return False
            node = node.children[c]
        
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children.keys():
                return False
            node = node.children[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

obj = Trie()
# print(obj)
# print(obj.root.children)

obj.insert("hello")
# print(obj.root.children)
obj.insert("h")
# print(obj.root.children['h'].end)

print(obj.search("hell"))
print(obj.startsWith("hell"))

