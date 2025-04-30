# given array 2D, and this array have a cell as a wall
# and it have a gate (possible to have more than one), so matrix as some labyrinth
# calculate path how many cell from each cell to gate
#
# -1  - A water cell that can not be traversed (wall)
#  0  - A treasure chest (gate)
# inf - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent infinity (from cell impossible to get the gate)
#
# Input: [
#   [2147483647,-1,0,2147483647],
#   [2147483647,2147483647,2147483647,-1],
#   [2147483647,-1,2147483647,-1],
#   [0,-1,2147483647,2147483647]
# ]
# Output: [
#   [3,-1,0,1],
#   [2,2,1,-1],
#   [1,-1,2,-1],
#   [0,-1,3,4]
# ]
#
#
# Input: [
#   [0,-1],
#   [2147483647,2147483647]
# ]
#
# Output: [
#   [0,-1],
#   [1,2]
# ]
#
#
from collections import deque
from typing import List


class SolutionBFS:
    def is_land_and_treasure(self, grid: List[List[int]])-> None:
        rows, columns = len(grid), len(grid[0])
        queue = deque()
        visit = set()

        def add_cell(row, column):
            # row,column should be in matrix range
            # grig shouldn't be a wall
            # and also not visited
            if (min(row,column) < 0 or row == rows or column == columns or
                grid[row][column]== -1 or
                    (row, column) in visit
            ):
                return
            visit.add((row, column))
            queue.append([row, column])

        # go through rows, columns  to find a chest,gate (represented as 0)
        # add to queue and to visit
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 0:
                    queue.append([r,c])
                    visit.add((r,c))

        distance = 0
        print(grid)
        # in this lop we calculate cell distance to gates (chests)
        # gates are represent root node so we start bfs from them
        while queue:
            # is queue have two gates then we should start search bfs for each root
            for i in range(len(queue)):
                row , column = queue.popleft()
                # root have 0 and it will reassign, closest assign as 1, next 2 etc
                grid[row][column] = distance
                # call dfs with navigation row up, row down, column right, columnleft
                add_cell(row+1,column)
                add_cell(row-1, column)
                add_cell(row, column+1)
                add_cell(row, column-1)
            # after navigate though layer then distance should increment
            distance+=1

m = [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
obj = SolutionBFS()
obj.is_land_and_treasure(m)
print(m)