# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # self.inorder_list = []
        self.ans = 0
        self.k = k
        def inorder(root, k):
            if root:
                inorder(root.left, self.k)
                self.k -= 1
                if self.k == 0:
                    self.ans = root.val
                    return
                # self.inorder_list.append(root.val)
                inorder(root.right, self.k)
        # print(self.inorder_list)
        inorder(root, self.k)
        return self.ans # self.inorder_list[k-1]
