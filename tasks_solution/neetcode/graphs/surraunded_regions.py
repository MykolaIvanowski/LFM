# given matrix 2d array, x, o represent different tipe of regions
# if o region surraunded by x region change it to x
# modify existing board
#
#    x o x x x       x o x x x
#    x x o o x  =>   x x x x x
#    o o x o x       o o x x x
#    x x x x x       x x x x x
#
#
# Input: board = [
#   ["X","X","X","X"],
#   ["X","O","O","X"],
#   ["X","O","O","X"],
#   ["X","X","X","O"]]
# Output: [
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","X","X","O"]]
#
#
from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]])-> None:
        rows = len(board)
        columns = len(board[0])

        def dfs(row, column):
            # matrix index pointer should be in matrix range
            # and cell shouldn't have 'O' why because we try to find cell with 'O'
            if ( row< 0 or column< 0 or row ==rows or column == columns or
                board[row][column] != 'O'
            ):
                return # breaking depth for search

            board[row][column] = 'T' #  save cell 'O' check it and save it assign 'T'

            # navigate with step 1 through matrix
            dfs(row+1, column)
            dfs(row-1, column)
            dfs(row, column+1)
            dfs(row, column-1)

        # go left, right to find unsurraunded regions
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r,0)
            if board[r][columns-1]:
                dfs(r,columns-1)
        # go to up, bottom sides to find unsuraunded regions
        for c in range(columns):
            if board[0][c]:
                dfs(0, c)
            if board[rows-1][c]:
                dfs(rows-1,c)

        # chane board
        # saved region turn from 'T' to 'O'
        # uraunded region change from 'O' to 'X'
        for r in range(rows):
            for c in range(columns):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'

board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","O","O","X"],
  ["X","X","X","O"]
]
o =  Solution()
o.solve(board)
print(board)

class Solution:
    def solve(self, board: List[List[str]])-> None:
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        columns = len(board[0])
        rows = len(board)

        def dfs():
            queue = deque()
            # go though matrix
            for row in range(rows):
                for column in range(columns):
                    # check only left, right, up, bottom matrix lines
                    # and check cell have 'O' land if yes add to queue
                    if (
                        row  == 0 or row == rows-1 or
                        columns ==0 or columns == columns-1 and
                        board[row][column] == 'O'
                    ):
                        # add to queueu cells that can not be changed (captured)
                        queue.append((row, column))

            while queue:
                row, column = queue.popleft()
                # cell added to queue can not be captured
                if board[row][column] == 'O':
                    # assign saves sight
                    board[row][column] = 'T'
                    # go through navigation from this cell to find all non changeable cells
                    for direction_row, direction_column in direction:
                        #next cell to check
                        next_row, next_column = row + direction_row, column + direction_column
                        # if next pointer in matrix range add it to queue for future check
                        if rows > next_row >= 0 and columns > next_column >= 0:
                            queue.append((next_row, next_column))

        dfs() # entry point

        # saved cell chance to 'O' land
        # surraunded cell chant to 'X'
        for r in range(rows):
            for c in range(columns):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'


board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","X","X","O"]
]
O = Solution()
o.solve(board)
print(board)