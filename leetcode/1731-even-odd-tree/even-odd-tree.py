# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        from queue import Queue

        def fx(temp, i):
            # print(i, temp)
            if i & 1: # odd
                if temp[0] & 1:
                    return False
                prev = temp[0]
                for j in range(1, len(temp)):
                    if temp[j] & 1 or temp[j] >= prev:
                        return False
                    prev = temp[j]
            else: # even
                if not(temp[0] & 1):
                    return False
                prev = temp[0]
                for j in range(1, len(temp)):
                    if not(temp[j] & 1) or temp[j] <= prev:
                        return False
                    prev = temp[j]
            return True

        p = root
        q = Queue()
        levels = []
        temp = []
        i = 0
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
                    # print(temp, i)
                    x = fx(temp, i)
                    if not x:
                        return False
                    levels.append(temp)
                    i += 1
                    temp = []
                else:
                    p = None
                    # print(temp, i)
                    x = fx(temp, i)
                    if not x:
                        return False
                    levels.append(temp)
        return True
        # print(levels)
        # even = True
        # for i, l in enumerate(levels):
        #     if i % 2 == 0:
        #         # print(l)
        #         prev = l[0]
        #         if not (prev & 1):
        #             return False
        #         for j in range(1, len(l)):
        #             # print(l[j])
        #             if not (l[j] & 1) or prev >= l[j]:
        #                 return False
        #             prev = l[j]
        #     else:
        #         prev = l[0]
        #         if prev & 1:
        #             return False
        #         for j in range(1, len(l)):
        #             if l[j] & 1 or prev <= l[j]:
        #                 return False
        #             prev = l[j]
        # return True
