# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        p = sp = head
        while p:
            p = p.next
            if p:
                p = p.next
            else:
                return False
            sp = sp.next

            if p == sp:
                return True
        return False
