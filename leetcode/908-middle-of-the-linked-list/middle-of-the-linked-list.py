# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = sp = head

        while p:
            p = p.next
            if p:
                p = p.next
            else:
                return sp
            sp = sp.next
        return sp
