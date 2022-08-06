# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.validate(-math.inf, math.inf, root)
    
    def validate(self, low, high, root):
            if root is None:
                return True
            if root.val <= low or root.val >= high:
                return False
            
            return self.validate(low, root.val, root.left) and self.validate(root.val, high, root.right)