from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1, row2, row3 = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        rv = []
        for w in words:
            wordSet = set(w.lower())
            if wordSet <= row1 or wordSet <= row2 or wordSet <= row3:
                rv.append(w)
        return rv

