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
    # Algorithm: Postorder Traversal
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        height = 1
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        
        return height + max(left_height, right_height)
            