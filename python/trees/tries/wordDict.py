class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}
    

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if not c in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True
        

    def search(self, word: str) -> bool:
        def search_in_node(word, node):
            for i, c in enumerate(word):
                if c == '.':

            return 


        node = self.root
        return search_in_node(word, node)
                
            

obj = WordDictionary()
obj.addWord("a")
obj.addWord("ab")
#print(obj.search("hello"))
#print(obj.search(".ello."))
#print(obj.search(".ello"))
# print(obj.search("a"))
print(obj.search(".b"))
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)