"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        p, sp = head, None
        stack = []

        while p:
            if p:
                if p.child:
                    stack.append(p.next) # p = 1, p.n = 2, p.c = 3
                    p.next = p.child  # p = 1, p.n = 3, p.c = 3                    
                    p.child.prev = p # p = 1, p.c = 3
                    sp = p # p = 1, sp = 1
                    p = p.next # p = 3, sp = 1
                    sp.child = None
                    # print(p.val, p.child.prev.val, p.child.val)
                elif p.next:
                    p = p.next
                elif len(stack):
                    found = False
                    while len(stack): 
                        sp = stack.pop()
                        if sp:
                            found = True    
                            break
                    if found:
                        p.next = sp
                        sp.prev = p
                        p = sp
                    else:
                        return head
                else:
                    return head