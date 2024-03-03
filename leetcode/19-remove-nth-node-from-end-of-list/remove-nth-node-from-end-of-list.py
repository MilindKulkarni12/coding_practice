# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        p = head
        while p:
            l += 1
            p = p.next
        # print(l)
        # 1, 2, 3, 4, 5
        # n = 2, l = 5
        # 5 - 2: 3
        # 1
        tgt = l - n
        i = 0
        p, sp = head, head
        while i < tgt:
            sp = p
            p = p.next
            i += 1
        print("sp:", sp.val, "p:", p.val)
        if sp == p:
            if p == head:
                head = head.next
            else:
                p = None
        else:
            sp.next = p.next
        return head

