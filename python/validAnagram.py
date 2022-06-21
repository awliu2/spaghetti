"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.
"""

"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for i in s:
            if i not in letters:
                letters[i] = 1
            else:
                letters[i] += 1

        for i in t:
            if i not in letters:
                return False

            else:
                letters[i] -= 1

        for letter in letters.values():
            if letter != 0:
                return False

        return True
