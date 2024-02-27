# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
            
        def fx(root, max_d):
            if root:
                rd = fx(root.right, max_d)
                ld = fx(root.left, max_d)
                res[0] = max(res[0], rd + ld)
                return 1 + max(rd, ld)
            return 0
        x = fx(root, -1)
        return res[0]
        
