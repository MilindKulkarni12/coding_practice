# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        def fx(root, d):
            if root and (depth - d == 1):
                n1 = TreeNode(val)
                n2 = TreeNode(val)
                n1.left = root.left
                root.left = n1
                n2.right = root.right
                root.right = n2
                return
            elif root:
                fx(root.left, d+1)
                fx(root.right, d+1)
            else:
                return
        if depth == 1:
            n = TreeNode(val)
            n.left = root
            root = n
            return root
        fx(root, 1)
        return root



