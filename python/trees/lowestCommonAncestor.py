class Solution:
    def findPath(self, root, target, path: List):
        if root is None:
            return False
        
        path.append(root)
        
        if root == target:
            return True

        
        
        if ((root.left != None and self.findPath(root.left, target, path) or
            root.right != None and self.findPath(root.right, target, path))):
            return True
        
        path.pop()
        return False
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = []
        path2 = []

        self.findPath(root, p, path1)
        self.findPath(root, q, path2)
        print(path1)

        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                break
            
            i += 1
            
        return path1[i-1]

        
    
    def singleTraversal(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None

        if root == p or root == q:
            return root
        
        left_traversal = self.singleTraversal(root.left, p, q)
        right_traversal = self.singleTraversal(root.right, p, q)

        # if both traversals find a target, this root must be lowest common ancestor
        if left_traversal and right_traversal:
            return root
        
        # if only one traversal finds the target, then the LCA must be in that traversal
        
        return left_traversal if left_traversal not None else right_traversal 
            