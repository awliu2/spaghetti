class Solution {
    private int diameter;
    public int diameterOfBinaryTree(TreeNode root) {
        diameter = 0;
        dfs(root);
        return diameter;
    }

    public int dfs(TreeNode root)
    {
        if (root == null)
        {
            return 0;
        }
        int leftPath = dfs(root.left);
        int rightPath = dfs(root.right);
        diameter = Math.max(diameter, leftPath + rightPath);
        return 1 + Math.max(leftPath, rightPath);
        
    }
}