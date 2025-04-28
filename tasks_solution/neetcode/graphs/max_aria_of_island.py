# given an 2d array, 0 represenr water 1 represent land
# land can be connected vertically or horizontally
# find how much cell in island and return number of cells from the biggest numbers
#
# Input: grid = [
#   [0,1,1,0,1],
#   [1,0,1,0,1],
#   [0,1,1,0,1],
#   [0,1,0,0,1]
# ]
# Output: 6
#
#
from typing import List


class SolutionDFS:
    def max_aria_of_island(self, grid: List[List[int]])-> int:
        rows, columns = len(grid), len(grid[0])
        visit = set()

        def depth_first_search(row, column):
            print(row, column)
            # check if pointer do not point outside from matrix
            # and if current cell not water
            # and check if it is visited
            if(
                row < 0 or column < 0 or
                row == rows or column == columns or
                grid[row][column] == 0 or
                (row,column) in visit
            ):
                # interrupt recursion, we will count later
                return 0
            # add visited cell to set
            visit.add((row, column))

            # 1 + dfs(), ... - is crucial it counts the current cell in the island
            return (1 + depth_first_search(row + 1, column) +
                    depth_first_search(row - 1, column) +
                    depth_first_search(row, column + 1) +
                    depth_first_search(row, column - 1))

        area = 0
        # in this loop we step by step go through all cell in matrix
        for r in range(rows):
            for c in range(columns):
                # find island and calculate how much cell in it, then take max island
                area = max(depth_first_search(r,c), area)

        return area

matrix = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

obj = SolutionDFS()
r = obj.max_aria_of_island(matrix)
print(r)