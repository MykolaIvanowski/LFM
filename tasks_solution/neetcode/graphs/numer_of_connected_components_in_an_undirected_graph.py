# given an n nodes  and edges array represent connection between root and child
# return the total numbers of connected componetns in graph
# [[parent, child],[parent, child]]
#
# Input:
# n=3
# edges=[[0,1], [0,2]]
# Output:
# 1
#
# Input:
# n=6
# edges=[[0,1], [1,2], [2,3], [4,5]]
# Output:
# 2
#
#
from collections import deque
from typing import List


class SolutionDFS:
    def count_components(self, n: int,edges: List[List[int]])-> int:
        node_naighbors = [[] for _ in range(n)] # adjacency list, contain node and its neighbors
        visit  = [False] * n   # list visited node

        # # filed adjacency list with node - neighbors
        for i,j in edges:
            node_naighbors[i].append(j)
            node_naighbors[j].append(i)

        # go through all neighbors of given node
        def depth_first_search(node):
            for neighbor in node_naighbors[node]:
                if not visit[neighbor]:
                    visit[neighbor] = True       # if node in not visited mark it as visited
                    # and check all its neighbors for this node (maybe they are not visited yet)
                    depth_first_search(neighbor)

        result = 0
        # go though all nodes and after recursive calls increment result
        # because it check edges
        # in case there are no edges then result == n
        # if all node have edges then result == 1
        for node in range(n):
            if not visit[node]:
                depth_first_search(node)
                result += 1

        return result

o = SolutionDFS()
r = o.count_components(5,[])
print(r)


class SolutionBFS:
    def count_components(self, n: int, edges: List[List[int]])-> int:
        node_neighbor = [[] for _ in range(n)] # adjacency list
        visit = [False] * n # track visited nodes
        # fill in adjacency list
        for i, k in edges:
            node_neighbor[i].append(k)
            node_neighbor[k].append(i)

        # go and check every neighbor for node
        def breadth_first_search(node):
            queue = deque([node])
            visit[node] = True  # mark this node as visited

            while queue:
                current_node = queue.popleft()

                # check every neighbors for currrent not
                for neighbor in node_neighbor[current_node]:
                    if not visit[neighbor]:
                        # in neighbor is not visited, mark as visited and it to queue for checking
                        visit[neighbor] = True
                        queue.append(neighbor)

        result = 0
        # go and visit every node
        for node in range(n):
            if not visit[node]:
                breadth_first_search(node)
                # increment result
                #  example result == 2 (1-2, and 3-4-5), there are two graph
                result+=1
        return result