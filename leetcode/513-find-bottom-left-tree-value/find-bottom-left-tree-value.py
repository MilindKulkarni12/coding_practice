# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        from queue import Queue
        p = root
        q = Queue()
        levels = []
        temp = []
        
        q.put(root)
        while p:
            temp.append(p.val)
            if p.left:
                q.put(p.left)
            if p.right:
                q.put(p.right)
            
            p = q.get()
            
            if p == root:
                if not q.empty():
                    p = q.get()
                    q.put(root)
                    levels.append(temp)
                    temp = []
                else:
                    p = None
                    levels.append(temp)
        return levels[-1][0]; 
