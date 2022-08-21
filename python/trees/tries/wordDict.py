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
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True
        

    def search(self, word: str) -> bool:
        
        def search_in_node(word, node):
            for i, c in enumerate(word):
                if c == '.':
                    for child in node.children.values():
                        if search_in_node(word[i + 1:], child):
                            return True
                    return False
                else:
                    if c not in node.children:
                        return False
                node = node.children[c]

            return node.end
        
        return search_in_node(word, self.root)
                
            

obj = WordDictionary()
obj.addWord("a")
obj.addWord("ab")
#print(obj.search("hello"))
#print(obj.search(".ello."))
#print(obj.search(".ello"))
# print(obj.search("a"))
print(obj.search('ab'))
print(obj.search('..')) 
print(obj.search('.b'))
print(obj.search('.a'))
# print(obj.search(".b"))