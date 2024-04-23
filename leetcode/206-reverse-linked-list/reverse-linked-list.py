# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.head = None
        if not head:
            return None
        def fx(node):
            if node.next:
                p = fx(node.next)
                p.next = node
            else:
                self.head = node
            return node

        tail = fx(head)
        tail.next = None
        return self.head
 