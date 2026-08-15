# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        res = [root.val]
        def pathSum(root):
            # assumes upward connection and updates the global maximum directly for the non upward connection case 
            if root is None:
                return 0
            
            left = max(0, pathSum(root.left))
            right = max(0, pathSum(root.right))

            # update the global max
            res[0] = max(res[0], root.val + left + right)

            return root.val + max(left, right)
        pathSum(root)
        return res[0]