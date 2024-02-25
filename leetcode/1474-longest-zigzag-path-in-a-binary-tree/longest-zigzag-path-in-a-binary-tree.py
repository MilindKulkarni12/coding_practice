# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        def fx(p, left, ht): # p: CurrentNode
            if p:
                if left:
                    r_ht = fx(p.right, False, ht+1)
                    l_ht = fx(p.left, True, 0)
                else:
                    r_ht = fx(p.right, False, 0)
                    l_ht = fx(p.left, True, ht+1)
                return max(l_ht, r_ht)
            return ht
        
        return max(fx(root.left, True, 0), fx(root.right, False, 0))
