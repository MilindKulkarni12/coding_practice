# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorder_list = []

        def inorder(root):
            if root:
                inorder(root.left)
                self.inorder_list.append(root.val)
                inorder(root.right)
        # print(self.inorder_list)
        inorder(root)
        return self.inorder_list[k-1]
