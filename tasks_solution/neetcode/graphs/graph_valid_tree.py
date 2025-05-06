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
from typing import List


class Solution:
    def valid_tree(self, n: int, edges: List[List[int]])-> int:
        # tree have to much edges
        if len(edges) >  (n-1):
            return False

        # made array to store edges
        array = [[] for _ in range(n)]
        # store edges
        for i, j in edges:
            array[i] = j
            array[j] = i

        visit = set()

        def depth_first_search(node, p):
            if node in visit:
                return  False

            for n in array[node]:
                if n == p:
                    continue
                if not depth_first_search(n, node):
                    return False

            return True

        return depth_first_search(0,-1) and len(visit) == n
