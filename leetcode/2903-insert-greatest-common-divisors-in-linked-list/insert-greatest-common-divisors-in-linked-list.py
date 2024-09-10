# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        sp = head
        p = head.next

        while sp and p:
            gcd = math.gcd(sp.val, p.val)
            n = ListNode(gcd, p)
            sp.next = n

            sp = p
            p = p.next
        
        return head
