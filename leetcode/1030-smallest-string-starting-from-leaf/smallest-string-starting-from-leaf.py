# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # def fx(root):
        #     if root:
        #         suff = chr(97 + root.val)
        #         left = fx(root.left)
        #         right = fx(root.right)
                
        #         if left and right:
        #             return left + suff if left + suff < right +suff else right + suff
        #         elif left:
        #             return left + suff
        #         elif right:
        #             return right + suff
        #         return suff
        #     return ''
        # return fx(root)
        ans = []
        def fx(root, s):
            if root:
                pref = chr(97 + root.val)
                if root.left is None and root.right is None:
                    ans.append(pref + s)
                    return
                elif root.right is None:
                    fx(root.left, pref + s)
                elif root.left is None:
                    fx(root.right, pref + s)
                else:
                    fx(root.left, pref + s)
                    fx(root.right, pref + s)
            else:
                return
        
        fx(root, '')
        print(ans)
        ans.sort()
        print(ans)
        return ans[0]
