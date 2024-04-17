# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def fx(root, targetSum):
            if root:
                if not root.left and not root.right:
                    if targetSum - root.val == 0:
                        return True
                    return False
                return fx(root.left, targetSum - root.val) or fx(root.right, targetSum - root.val)
            return False

        return fx(root, targetSum)
