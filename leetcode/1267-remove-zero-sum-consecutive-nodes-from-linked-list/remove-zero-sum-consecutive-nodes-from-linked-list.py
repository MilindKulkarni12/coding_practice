# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefix_sum = {}
        p = head
        s = 0
        while p:
            s += p.val
            # print(s)
            if s == 0:
                p = p.next
                head = p
                prefix_sum = {}
            elif prefix_sum.get(s, -1) == -1:
                prefix_sum[s] = p
                p = p.next
            else:
                # found 
                # 1 3 2 -3 -2 5 5 -5 1
                # 1 4 6  3  1 6 11 6 7

                start = prefix_sum[s] # 2 -> s = 3
                curr = start.next # 3 -> 6
                end = p
                s_atp = s
                print(s, start.val, end.val, s_atp, curr.val)
                # print(s_atp, end.val)
                # print(prefix_sum)
                while curr != end:
                    # print(s_atp)
                    s_atp += curr.val
                    prefix_sum.pop(s_atp)
                    curr = curr.next
                    # print(prefix_sum)

                p = end.next
                start.next = p
                
        return head
