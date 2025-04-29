# given undirected graph, make a deep copy of this grsph
#
# Input: adjList = [[2],[1,3],[2]]
# Output: [[2],[1,3],[2]]
#
from collections import deque
from typing import Optional

class Node:
    def __init__(self, value = 0, neighbors = None):
        self.value = value
        self.neighbors = neighbors if neighbors is not None else []


class SolutionDFS:
    def clone_graph(self, node: Optional['Node']) -> Optional['Node']:
        hash_map = {} # here we store as key store old nodes as value store new nodes

        def depth_first_search(node):
            # check if node in key value if yes that mean we already copied checked node
            # if yes return copied node
            if node in hash_map:
                # return deep copy node stored as a value
                return hash_map[node]

            # coping node and store to hash map as a value
            copy = Node(node.value)
            hash_map[node] = copy

            # form list neighbors we take reference for node and append it to new copy
            # but it does not have copy, so we call dfs end in next recursive call we create this new node
            # (just before asight it to references)
            for neighbor in node.neighbors:
                # in dfs pass an old node
               copy.neighbors.append(depth_first_search(neighbor))

            # return deep copy Node
            return copy
        # pass a root node from curren graph
        return depth_first_search(node) if node else None

n4 = Node(4)
n3 = Node(3, [n4])
n2 = Node(2, [n3])
n1 = Node(1,[n2,n4])

n2.neighbors.append(n1)
n3.neighbors.append(n2)
n4.neighbors.append(n1)
n4.neighbors.append(n3)


obj = SolutionDFS()
r = obj.clone_graph(n1)
print(r.value)


class SolutionBFS:
    def clone_graph(self, node : Optional['Node'])-> Optional['Node']:
        if not node:
            return None

        hash_map = {} # for checking which node was copied
        # copy firs root node from graph
        hash_map[node]  = Node(node.value)
        queue =  deque([node]) # general attribute for breadth first search

        while queue:
            current_node  = queue.popleft()
            # go through all referenced nodes (leafs, edges)
            for neighbor in current_node.neighbors:
                # if referenced node not in list it mean we not copy this node yet
                if neighbor not in hash_map:
                    # copy next node to hash map
                    # and add it to queue for next check (nex iteration)
                    hash_map[neighbor] = Node(neighbor.value)
                    queue.append(neighbor)

                # for every current node take and asight edge (reference, branch) from next node
                # it is like we make a new edges (list neighbors)
                # it is work because current, next node is copied
                # and we iterate for each neighbor (so reference can not be missed)
                hash_map[current_node].neighbors.append(hash_map[neighbor])

        # return  value , because it contained deep copy
        return hash_map[node]

obj = SolutionBFS()
res = obj.clone_graph(n1)
print(res.value)