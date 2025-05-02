# given 2D array
# find path from cell to ocean, left, up sides is pacific; right, down sides are atlantic ocean
# pass (water flow, river) is correct if from cell to ocean the cells have the same value or lower
# find the cell which are reaching both oceans
#
# ights = [
# Input: he  [4,2,7,3,4],
#   [7,4,6,4,7],
#   [6,3,5,3,6]
# ]
# Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]
#
# Input: heights = [[1],[1]]
# Output: [[0,0],[0,1]]
#
#
from collections import deque
from typing import List

class SolutionDFS:
    def pacific_atlantic(self, heights: List[List[int]])-> List[List[int]]:
        rows, columns = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def depth_first_search(row, column, visit, previous_height):
            # check if pointer in matrix range
            # previous_height represent point  to previous cell it
            # adn it should be less or equal to current cell for making river (pass, water flow)
            if ((row, column ) in visit or
                row < 0 or column < 0 or row == rows or column == columns or
                heights[row][column] < previous_height):
                return
            # add to visit set (pacific, atlantic)
            # also it mean that cell can reach ocean
            visit.add((row,column))
            # navigation calls up, down, right, left
            depth_first_search(row+1, column, visit, heights[row][column])
            depth_first_search(row-1, column, visit, heights[row][column])
            depth_first_search(row, column+1, visit, heights[row][column])
            depth_first_search(row, column-1, visit, heights[row][column])

        # in general we start looking and filling visited sets from up, bottom sides
        for c in range(columns):
            # start check for pacific ocean which is up in matrix
            depth_first_search(0, c, pacific, heights[0][c])
            # start check for atlantic ocean which is bottom in matrix
            depth_first_search(rows-1, c, atlantic, heights[rows-1][c])

        # in general we start looking adn filling visited sets from left, right sides
        for r in range(rows):
            # start check for left side which is pacific in matrix
            depth_first_search(r, 0, pacific, heights[r][0])
            # statr for right side which is atlantic in matrix
            depth_first_search(r,columns-1, atlantic,heights[r][columns-1])


        result = []
        # find the cell are reaching both oceans
        for r in range(rows):
            for c in range(columns):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])

        return result


class SolutionBFS:
    def pacific_atlantic(self, heights: List[List[int]])-> List[List[int]]:
        rows, columns = len(heights), len(heights[0])
        direction = [[1,0],[-1,0], [0,1],[0,-1]]
        pacific = [[False]* columns for _ in range(rows)]
        atlantic = [[False]*columns for _ in range(rows)]

        def breadth_first_search(ocean_field, ocean):
            queue = deque(ocean_field)
            while queue:
                row, column = queue.popleft()
                # cell is checked and it can pass to ocean (change False on true)
                ocean[row][column] = True
                # go trough direction for each iteration
                for direction_row, direction_column in direction:
                    next_row, next_column  = direction_row+ row, direction_column+column
                    # if point in matrix renge and  next cell is not False
                    # and cell is equal or less than current cell
                    # then we add it to queue and we know for sure the next cell can pass to ocean
                    if(
                        rows > next_row >= 0 and columns > next_column >= 0 and
                        not ocean[next_row][next_column] and
                        heights[next_row][next_column]>=heights[row][column]
                    ):
                        # add cell to queue
                        queue.append((next_row,next_column))

        pacific_field = []
        atlantic_field = []

        # filed with indexes the first lines for left, bottom sides
        # pacific scheme
        # n  e  e  e
        # n  e  e  e     e - empty poin
        # n  e  e  e     n - index number (row, column)
        # n  e  e  e
        for r in range(rows):
            pacific_field.append((r,0))
            atlantic_field.append((r,columns-1))

        # field nex linens for pacific, atlantic - right and up linex
        # atlantic scheme
        # e  e  e  e     e  e  e  n
        # e  e  e  e  => e  e  e  n
        # e  e  e  e     e  e  e  n
        # n  n  n  n     n  n  n  n
        for c in range(columns):
            pacific_field.append((0,c))
            atlantic_field.append((rows-1,c))

        breadth_first_search(pacific_field,pacific)
        breadth_first_search(atlantic_field,atlantic)

        result = [ ]
        # write a cell to result achieved pacific and atlantic oceans
        for r in range(rows):
            for c in range(columns):
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r,c])

        return result

obj = SolutionBFS()
r = obj.pacific_atlantic( [[4,2,7,3,4],
                           [7,4,6,4,7],
                           [6,3,5,3,6]])
print(r)