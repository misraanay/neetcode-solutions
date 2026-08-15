"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        hash = {}

        def dfs(node):
            if node in hash:
                return hash[node]
            cur = Node(node.val)
            hash[node] = cur
            for n in node.neighbors:
                    cur.neighbors.append(dfs(n))
            return cur
        return dfs(node) 



        


        




        
        