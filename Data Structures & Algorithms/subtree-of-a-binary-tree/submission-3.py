# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSametree(self, a, b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        if a.val == b.val:
            return self.isSametree(a.left, b.left) and self.isSametree(a.right, b.right)
        return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            if root is None:
                return True
            return False
        if root is None:
            return False
        res = False
        if root.val == subRoot.val:
            res = self.isSametree(root.left, subRoot.left) and self.isSametree(root.right, subRoot.right)
        return res or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)