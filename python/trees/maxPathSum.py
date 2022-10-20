# Definition for a binary tree node.
# from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root) -> int:
        rv = [(root.val)]
        def dfs(subroot):
            if not subroot:
                return 0
            left_max = max(dfs(subroot.left), 0)
            right_max = max(dfs(subroot.right), 0)

            rv[0] = max(rv[0], subroot.val + left_max + right_max)
            return subroot.val + max(left_max, right_max)
                
        dfs(root)
        return rv[0]
