"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        new_dict = {}
        if not node:
            return None

        def dfs(node):
            if node.val in new_dict:
                return new_dict[node.val]
            
            copy_node = Node(node.val)
            new_dict[node.val] = copy_node
            for nei in node.neighbors:
                copy_node.neighbors.append(dfs(nei))
            return copy_node
        return dfs(node)
