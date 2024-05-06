# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        stack = []

        while p:
            if stack:
                while stack and stack[-1].val < p.val:
                    stack.pop()
                if stack:
                    stack[-1].next = p
                stack.append(p)
            else:
                stack.append(p)
            p = p.next
        return stack[0]
