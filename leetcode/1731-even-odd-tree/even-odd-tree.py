# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
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
        # print(levels)
        even = True
        for i, l in enumerate(levels):
            if i % 2 == 0:
                # print(l)
                prev = l[0]
                if prev % 2 == 0:
                    return False
                for j in range(1, len(l)):
                    # print(l[j])
                    if l[j] % 2 == 0 or prev >= l[j]:
                        return False
                    prev = l[j]
            else:
                prev = l[0]
                if prev % 2 != 0:
                    return False
                for j in range(1, len(l)):
                    if l[j] % 2 != 0 or prev <= l[j]:
                        return False
                    prev = l[j]
        return True
