# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        p = sp = head
        l = []
        while p:
            p = p.next
            if p:
                p = p.next
            else:
                break
            l.append(sp.val)
            sp = sp.next
        # print(l)
        i = len(l) - 1
        while sp:
            l[i] += sp.val
            i -= 1
            sp = sp.next
        # print(l)
        return max(l)
