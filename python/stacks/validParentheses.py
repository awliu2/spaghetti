"""
Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        left = {'(','{','['}
        pairings = {
                    ')' : '(',
                    '}' : '{',
                    ']' : '[',
                    }
        stack = []
        for c in s:
            if c in left:
                stack.append(c)
            else:
                if not stack:
                    return False
                if pairings[c] != stack.pop():
                    return False
        return not stack
