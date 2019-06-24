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

# Time Complexity: O(n)
# Algorithm: Postorder Traversal
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isSubtreeSymmetric(root.left, root.right)
    
    def isSubtreeSymmetric(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        
        left = self.isSubtreeSymmetric(p.left, q.right)
        right = self.isSubtreeSymmetric(p.right, q.left)
        
        return left and p.val == q.val and right