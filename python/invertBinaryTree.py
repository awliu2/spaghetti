# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

    
    def invertTreeIterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        head = root
        q = deque()
        q.append(root)

        while q:
            curr = q.popleft()
             
            if not curr:
                return

            curr.left, curr.right = curr.right, curr.left

            if curr.left:
                q.append(curr.left)
            
            if curr.right:
                q.append(curr.right)
        
        return head