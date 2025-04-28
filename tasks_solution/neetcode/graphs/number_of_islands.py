# given matrix, with 1 or 0. i represent lend, 0 represent water
# 1 (land) connected horizontally or vertically and this form island
# count how many island in the array
#
#
# Input: grid = [
#     ["0","1","1","1","0"],
#     ["0","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
#   ]
# Output: 1
#
#
# Input: grid = [
#     ["1","1","0","0","1"],
#     ["1","1","0","0","1"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
#   ]
# Output: 4
#
#
import queue
from collections import deque
from typing import List


class SolutionBFS:
    def num_is_land(self, grid: List[List[int]])-> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]] # how can move cheker
        rows, columns = len(grid), len(grid[0]) # length for row, column
        islands = 0 # how many islands or simply result

        def dfs(row, column):

            # when we navigate through 2d array for search lend we can not got outside the matrix
            # so row, colum can not have negative index,
            # or be outside the max index for arrays colum, row
            # or have symbol of water
            if (row < 0 or column < 0 or
                row >= rows or column >= columns or
                grid[row][column] == '0'
            ):
                # finish search
                return

            # next line we mark cell as visited by set it as water
            # it is mean that we will not visit it agen
            # and no poit to revert this as it have not effect for result
            # because it already processed
            grid[row][column] = '0'

            # this loop move pointer to next cell
            for direction_row, direction_column in directions:
                dfs(direction_row + row, direction_column + column)

        # we start explore lend from x=0,y=0, then explore all possibilities if it is lend '1
        # and marc as visited asight 0 to cell
        # then go to next cell
        # one recursive cycle can find only one island
        # first to row and each column then next row each column etc
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == '1':
                    dfs(r,c)
                    islands += 1
        return islands


lands = [["1","1","0","0","1"],
                     ["1","1","0","0","1"],
                     ["0","0","1","0","0"],
                     ["0","0","0","1","1"]]
obj = SolutionBFS()
r = obj.num_is_land(lands)
print(r)


class SolutionBFS:
    def num_is_land(self, grid: List[List[int]])-> int:
        directions = [[1,0], [-1,0],[0,1],[0,-1]] # how to move to next point
        rows, columns = len(grid), len(grid[0]) # rows,columns length
        islands = 0 # result

        def bfs(row, column):
            queue = deque()
            grid[row][column] = '0' # when we first time visit the cell we should murk it as visited

            queue.append((row, column)) # add current cell to queue

            while queue:
                pop_row, pop_column = queue.popleft()

                # in loop we go through navigation to next point for find whole island, and mark as visited (0)
                #   there is order how we visit the cells:
                # 1 2 3 4 or   1 3 6 10
                # 2 3 4        2 5 9
                # 3 4          4 8
                # 4            7
                #
                # so  [0][0] it is the root and it on 0 level in the tree
                # [1][0] and [0][1] it is the leafs on level 1
                for direction_row, direction_column in directions:
                    # counting next position for pointer
                    next_row = direction_row + pop_row
                    next_column = direction_column + pop_column

                    # check if next position is not water and it is not greater then max index columns, rows
                    # and not a minus , in other case skip iteration
                    if (
                        next_column < 0 or next_row < 0 or
                        next_row >= rows or next_column >= columns or
                        grid[next_row][next_column] == '0'
                    ):
                        continue

                    # find land, add next position in queue for checking,
                    # and mark that we visit it
                    queue.append((next_row, next_column))
                    grid[next_row][next_column] = '0'

        # check on by one row then col, col, then next row col, col etc
        for r in range(rows):
            #if find land then increment result, and in bfs mark as visited
            for c in range(columns):
                if grid[r][c] =='1':
                    bfs(r,c)
                    islands +=1

        return islands

lands = [["1","1","0","0","1"],
         ["1","1","0","0","1"],
         ["0","0","1","0","0"],
         ["0","0","0","1","1"]]
obj = SolutionBFS()
r = obj.num_is_land(lands)
print(r)

