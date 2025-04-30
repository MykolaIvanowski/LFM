# given array 2D
# it have rotten and fresh orange, after 1 minutes fresh orange became rotten (become rotten only horizontal or vertical)
# in case cell are close to each other (rotten and fresh)
# find how mani minutes take to turn all orange rotten
# in case the are orange not have a connection to orange return -1
#
# 0 - represent empty cell
# 1 - representing fresh fruit
# 2 - represent rotten orange
#
# Input: grid = [[1,1,0],[0,1,1],[0,1,2]]
# Output: 4
#
# Input: grid = [[1,0,1],[0,2,0],[1,0,1]]
# Output: -1
#
#
from collections import deque
from typing import List


class SolutionBFS:
    def oranges_rotting(self, grid: List[List[int]])-> int:
        queue = deque()
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        fresh = 0
        time = 0

        # in matrix we count how many fresh fruits we have
        # and how manu rotten fruits we have
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1:
                    fresh +=1
                if grid[row][column] == 2:
                    queue.append((row,column))

        # general lop for breath first search
        while fresh > 0 and queue:
            # check if queue have a several rotten fruits
            # run for it iteration, rotten fruit represent root node
            for i in range(len(queue)):
                row, column = queue.popleft()
                # in cycle manage directions: down , up, right, left
                # for checking if in this cell stored fruit
                for direction_row, direction_column in direction:
                    # calculation for next cell direction
                    next_row, next_column = row+direction_row, column + direction_column
                    # check if pointer in 2d array range, and inside of cell is a fresh fruit  (grid[][]==1)
                    if(next_row in range(len(grid)) and next_column in range(len(grid[0])) and
                        grid[next_row][next_column] == 1):

                        # make a fresh fruit rotten, on next iteration it help not check it again
                        grid[next_row][next_column] = 2
                        # add this point to queue, it became in next iteration as a root (turn into parent)
                        queue.append((next_row,next_column))
                        # decrement count of fresh fruit, help understand in future is still left saved fruits
                        #
                        fresh -= 1
            # timer is simply counter for BFS levels (it is result value)
            # represent how many minutes need to rotting all fruits
            time+=1
        # return result or -1 if the are place with fresh fruit in matrix
        return time if fresh==0 else -1


sol = SolutionBFS()
r = sol.oranges_rotting([[1,1,0],[0,1,1],[0,1,2]])
print(r)