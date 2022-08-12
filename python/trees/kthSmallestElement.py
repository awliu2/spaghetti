# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallestBFS(self, root: Optional[TreeNode], k: int) -> int:
        if k == 1:
            while root.left:
                root = root.left
            return root.val
        
        
        vals = []
        
        q = deque()
        q.append(root)
        
        while q:
            node = q.popleft()
            if node:
                vals.append(node.val)
                q.append(node.left)
                q.append(node.right)
        vals.sort()
        return vals[k - 1]
    
    
    def DFSSolution(self, root: Optional[TreeNode], k: int) -> int:
        if k == 1:
            while root.left:
                root = root.left
            return root.val
        
        vals = []
        def valsDFS(self, root: Optional[TreeNode], arr: List):
            if root is None:
                return
            
            valsDFS(root.left, arr)

            vals.append(root.val)

            valsDFS(root.right, arr)
        
        valsDFS(root, vals)

        return vals[k - 1]

            