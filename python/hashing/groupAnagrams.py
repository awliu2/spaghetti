"""
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

Examples:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    Input: strs = [""]
    Output: [[""]]

    Input: strs = ["a"]
    Output: [["a"]]
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rv = []
        index_map = {}

        for i, s in enumerate(strs):
            sorted_str = "".join(sorted(s))
            if sorted_str not in index_map:
                singleton = [i]
                index_map[sorted_str] = singleton

            else:
                index_map[sorted_str].append(i)

        for key in index_map:
            lst = []
            for i in index_map[key]:
                lst.append(strs[i])
            rv.append(lst)
        return rv
