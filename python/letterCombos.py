from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        letters = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        
        def backtrack(index, path):
            if len(path) == len(digits):
                combinations.append("".join(path))
                return

            possible_letters = letters[digits[index]]
            for c in possible_letters:
                path.append(c)
                backtrack(index + 1, path)
                path.pop()

        combinations = []
        backtrack(0, [])
        return combinations 
        
print(Solution().letterCombinations("23"))