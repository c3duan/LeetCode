# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Time Complexity: O(n)
    # Algorithm: Inorder Traversal
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root is None:
            return 0
        sum = 0
        sum += self.rangeSumBST(root.left, L, R)
        if root.val >= L and root.val <= R:
            sum += root.val
        sum += self.rangeSumBST(root.right, L, R)
        return sum