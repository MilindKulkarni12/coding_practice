# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def fx(root):
            if root:
                pref = str(root.val)
                left = fx(root.left)
                right = fx(root.right)
                
                if left and right:
                    left = [pref + i for i in left] if left else [pref]
                    right = [pref + i for i in right] if right else [pref]
                    return left + right
                elif left:
                    left = [pref + i for i in left] if left else [pref]
                    return left
                elif right:
                    right = [pref + i for i in right] if right else [pref]
                    return right
                # print(pref, left, right)
                return [pref]
            return ''
        return sum([int(i) for i in fx(root)])
