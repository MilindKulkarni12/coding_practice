# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        head = None
        p = head
        curr_min_idx = 0
        while curr_min_idx != -1:
            curr_min = float("inf")
            curr_min_idx = -1
            for i in range(len(lists)):
                if lists[i] and lists[i].val <= curr_min:
                    curr_min = lists[i].val
                    curr_min_idx = i
            
            if not head and curr_min_idx != -1:
                head = lists[curr_min_idx]
                lists[curr_min_idx] = lists[curr_min_idx].next
                p = head
            elif curr_min_idx != -1:
                p.next = lists[curr_min_idx]
                lists[curr_min_idx] = lists[curr_min_idx].next
                p = p.next
            
        p = None
        return head



