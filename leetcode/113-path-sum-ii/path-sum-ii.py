# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def fx(root, targetSum, temp):
            if root:
                temp = temp[::]
                if not root.left and not root.right:
                    if targetSum - root.val == 0:
                        temp.append(root.val)
                        ans.append(temp)
                        return
                    return
                temp.append(root.val)
                fx(root.left, targetSum - root.val, temp) 
                fx(root.right, targetSum - root.val, temp)
        fx(root, targetSum, [])
        return ans
