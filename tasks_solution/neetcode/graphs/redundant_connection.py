# given a connected undirected graph with n nodes. Initially it contained no cycles
# in this graph add one additional edge creating a cycle in the graph
# remove additional edge from graph to restore a tree
#
#
# Input: edges = [[1,2],[1,3],[3,4],[2,4]]
# Output: [2,4]
#
# Input: edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
# Output: [3,4]
#
# input: edges  = edges = [[1,2], [1,3], [2,3]]     =>    1
# output : [2,3]                                         / \
#                                                       2 - 3
#
#
from typing import List


class Solution_DisjointSetUnion:
    def find_redundant_connection(self,edges: List[List[int]])-> List[int]:
        array_parent = [i for i in range(len(edges)+1)] # create list of nodes
        # represent rank for every node in graph,
        # if node without edges it have rank 1, if node have one leaf it rank 2
        #  for start all nodes have rank 1
        rank = [1] * (len(edges)+1)


        def find(n):

            parent  = array_parent[n] #  get parent cor current node

            # this will true if some nodes are parent not for themselves
            while parent != array_parent[n]: # if parent not the root
                # The hierarchy flattens, reducing the depth
                array_parent[parent] = array_parent[array_parent[parent]] # Path compression: update parent
                # closer to the root so that it keeps following the path compression logic
                parent = array_parent[parent]

            return parent


        def union(node1, node2):
            # find the root parents
            parent1, parent2 = find(node1), find(node2)

            # if root parents the same number this is a cycle, so return false
            if parent1 == parent2:
                return False

            # attached smaller tree under larger tree
            if rank[parent1] > rank[parent2]:
                array_parent[parent2] = parent1  # maked p1 perent of p2
                rank[parent1] += rank[parent2] # update rank for root (root rank + child rank )
            else:
                array_parent[parent1] = parent2 # makes p2 parent of p1
                rank[parent2] += rank[parent1] # update rank for root (root rank + child rank)

            return True

        # iterate through all edges
        for n1, n2 in edges:
            # check every union for redundancy
            if not union(n1, n2):
                # return redundant edge
                return [n1,n2]

obj = Solution_DisjointSetUnion()
r = obj.find_redundant_connection([[1,2],[1,3],[1,4],[3,4],[4,5]])
print(r)