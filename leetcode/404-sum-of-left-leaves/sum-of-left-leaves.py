# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def preorder(p, left):
            if p:
                if p.left is None and p.right is None and left:
                    return p.val
                else:
                    return preorder(p.left, True) + preorder(p.right, False)
            return 0
        return preorder(root, False)
