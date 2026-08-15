# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1 or len(inorder) == 1:
            return root
        mid = inorder.index(preorder[0])
        inorder_sub = [inorder[0:mid], inorder[mid+1:]]

        preorder_sub = [preorder[1:mid+1], preorder[mid+1:]]

        root.left = self.buildTree(preorder_sub[0], inorder_sub[0])
        root.right = self.buildTree(preorder_sub[1], inorder_sub[1])
        return root

        