# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = float(inf)

        def fx(root, depth):
            if root:
                if not root.left and not root.right:
                    self.depth = min(self.depth, depth)
                else:
                    fx(root.left, depth + 1)
                    fx(root.right, depth + 1)
            return
        if not root:
            return 0
        fx(root, 1)
        return self.depth