"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        new_head = Node(head.val)
        new_head.next = head.next

        node = head # 7
        new_head = Node(head.val) # 7
        n_map = {head: new_head}
        new_head1 = new_head
        node = node.next # 13
        while node:
            new_head.next = Node(node.val) # 13
            new_head = new_head.next # 13
            n_map[node] = new_head
            node = node.next
        new_head.next = None

        n1 = head
        n2 = new_head1

        while n2:
            n2.random = n_map[n1.random] if n1.random else None
            n1 = n1.next
            n2 = n2.next

        return new_head1
