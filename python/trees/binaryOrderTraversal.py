# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        rv = []
        
        head = root
        q = deque()
        q.append(root)
        level = []
        while len(q):
            curr = q.popleft()
            level.append[curr.val]
            
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            rv.append(level)
            level = []
        return rv
        
        

