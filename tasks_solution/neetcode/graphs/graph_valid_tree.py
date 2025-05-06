# given numbers from 0 to n-1. and list undirected edges
# function should find if tre is valid, no cycle, no lost edges
#
# Input:
# n = 5
# edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# Output:
# true
#
# Input:
# n = 5
# edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
#
# Output:
# false
#
from array import array
from collections import deque
from typing import List


class SolutionDFS:
    def valid_tree(self, n: int, edges: List[List[int]])-> bool:
        # tree have to much edges
        if len(edges) >  (n-1):
            return False

        # made array to store edges
        array = [[] for _ in range(n)] # adjacency list
        # store edges
        # each node store in connected neighbors
        for i, j in edges:
            array[i] = j
            array[j] = i

        visit = set()

        def depth_first_search(node, previous_node):
            # if we visit node again it mean we in loop, return false
            if node in visit:
                return  False

            # go through all connected node in  node, exception parent node
            for neighbors_node in array[node]:
                if neighbors_node == previous_node:
                    continue # ignore the parent node
                # go and check all connected nodes
                if not depth_first_search(neighbors_node, node):
                    return False

            # achieve finish
            return True

        # no cycle was found and all nodes were visited
        return depth_first_search(0,-1) and len(visit) == n


class SolutionBFS:
    def valid_tree(self, n : int, edges: List[List[int]])-> bool:
        # if numbers of edges exceeds it is impossible to be a tree
        if len(edges) > n-1:
            return False
        # initialise array for  store node and its neighbors
        array_adjacency = [[] for _ in  range(n)]
        # filed neighbors
        for k,j in edges:
            array_adjacency[k] = j
            array_adjacency[j] = k


        visit = set()
        # add first node
        queue = deque([(0,-1)])
        # add first visited node
        visit.add(0)

        while queue:
            node, parent = queue.popleft()

            # go through all neighbors in current node
            for neighbors_node in array_adjacency[node]:
                if neighbors_node == parent:
                    continue # if node is parent then skip it
                if neighbors_node in visit:
                    return False # if node already visited then it is cycle then return False

                # add curent node to visit set
                visit.add(neighbors_node)
                # add neighbor to curren node position and
                # current node in parent position for future check
                queue.append((neighbors_node, node))

        # all node were visited and it should be the same as n
        return len(visit) == n
