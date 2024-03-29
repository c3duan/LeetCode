/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

class Solution {
    /**
     * Time Complexity: O(n)
     * Algorithm: Preorder Traversal
     */
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        if (t1 == null && t2 == null) return null;
        if (t2 == null) return t1;
        if (t1 == null) return t2;
        
        TreeNode t = new TreeNode(t1.val + t2.val);
        t.left = mergeTrees(t1.left, t2.left);
        t.right = mergeTrees(t1.right, t2.right);
        
        return t;
    }
}