# given board (matrix) array , queen move like chess queen
# put on this board queen in that way when every queen do not attach each other
# if input 4 that means you have 4 queen and boar 4x4
# find all possible variety for queen position
#
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
#
# Input: n = 1
# Output: [["Q"]]
from typing import List

# nx  x  x  x       <- columns (or col in method)
#  x nx  x  x
#  x  x nx  x
#  x  x  x nx   => nx represent  negative diagonal
#
#   x  x  x  x
#   x  x  x px
#   x  x px  x
#   x px  x  x   => px represent  positive diagonal


#  calculated representation for positive diagonal
# +----+----+----+----+
# | 0  |  1 |  2 |  3 |   <-- Row 0: [0+0, 0+1, 0+2, 0+3]
# +----+----+----+----+
# | 1  |  2 |  3 |  4 |   <-- Row 1: [1+0, 1+1, 1+2, 1+3]
# +----+----+----+----+
# | 2  |  3 |  4 |  5 |   <-- Row 2: [2+0, 2+1, 2+2, 2+3]
# +----+----+----+----+
# | 3  |  4 |  5 |  6 |   <-- Row 3: [3+0, 3+1, 3+2, 3+3]
# +----+----+----+----+

# calculated representation for negative diagonal
# +-----+-----+-----+-----+
# |  0  | -1  | -2  | -3  |   <-- Row 0: [0-0, 0-1, 0-2, 0-3]
# +-----+-----+-----+-----+
# |  1  |  0  | -1  | -2  |   <-- Row 1: [1-0, 1-1, 1-2, 1-3]
# +-----+-----+-----+-----+
# |  2  |  1  |  0  | -1  |   <-- Row 2: [2-0, 2-1, 2-2, 2-3]
# +-----+-----+-----+-----+
# |  3  |  2  |  1  |  0  |   <-- Row 3: [3-0, 3-1, 3-2, 3-3]
# +-----+-----+-----+-----+

class Solution:
    def solve_n_queen(self, n : int)->List[List[str]]:
        col = set()
        # why calculate diagonal and not use it as coordinate?
        # 1. By calculating R + C for positive diagonal and R - C for negative diagonal,
        #    we can efficiently track conflicts across the entire diagonal with just a single value (the sum or difference)
        # 2. This avoids the need to manually iterate through all possible coordinates on the diagonal,
        #    and saving computational time.
        positive_diagonal = set() # represent r+c
        negative_diagonal = set() # represent r-c

        result = []
        board  = [['.']*n for i in range(n)]

        # when we call method r represent row, and in depth tree we go through row
        # that mean we for every row run loop for columns
        def backtraking(r):
            # if r equal to n it mean we achieve solution for queens
            if r == n:
                # join array to one string this ['.', 'q', '.', '.'] to this ['.q...']
                # then add it to result array
                copy = [''.join(row) for row in board]
                result.append(copy)
                return

            #  help go and check through columns
            #  in this cycle n represent base column
            for c in range(n):
                # this if helps skip putting queen on the same fild in row, colum, negative diagonal, positive diagonal
                if c  in col or (r+c) in positive_diagonal or (r-c) in negative_diagonal:
                    continue

                # add on which colum we will put queen
                # we do not need to save and check same for row  (like row.add(r)
                # because we use recursion for build a tree ant it recursively iterate through rows
                col.add(c)
                # calculate on which diagonals we will put queen
                positive_diagonal.add(r+c)
                negative_diagonal.add(r-c)

                # put queen on specific place

                board[r][c] = 'q'

                # go to next row in tree
                backtraking(r+1)

                # remove last added queen, diagonals, column for check,
                # so next iteration can check next position for queen
                col.remove(c)
                positive_diagonal.remove(r+c)
                negative_diagonal.remove(r-c)
                board[r][c] = '.'

        backtraking(0)
        return result

obj = Solution()
r = obj.solve_n_queen(4)
print(r)

# backtraking(0) [Row 0]
# └── Try placing queen in one of columns 0, 1, 2, 3
#     ├── Place queen at (0,0)  [State: col={0}, pos_diag={0}, neg_diag={0}]
#     │    └── backtraking(1) [Row 1]
#     │         ├── For row 1:
#     │         │    ├── (1,0) → invalid (same column as (0,0))
#     │         │    ├── (1,1) → invalid (diagonal conflict with (0,0))
#     │         │    ├── (1,2) → valid!
#     │         │    │      [New state: col={0,2}, pos_diag={0, 1+2=3}, neg_diag={0, 1-2=-1}]
#     │         │    │      └── backtraking(2) [Row 2]
#     │         │    │            └── (Explore valid placements; if none work, backtrack)
#     │         │    └── (1,3) → valid!
#     │         │             [New state: col={0,3}, pos_diag={0, 1+3=4}, neg_diag={0, 1-3=-2}]
#     │         │             └── backtraking(2) [Row 2]
#     │         │                   └── (Explore row 2 placements …)
#     │         └── (After trying all possibilities for row 1, backtracking occurs)
#     │
#     ├── Place queen at (0,1)  [State: col={1}, pos_diag={0+1=1}, neg_diag={0-1=-1}]
#     │    └── backtraking(1) [Row 1]
#     │          └── (Try valid placements for row 1 based on state from (0,1))
#     │
#     ├── Place queen at (0,2)  [State: col={2}, pos_diag={0+2=2}, neg_diag={0-2=-2}]
#     │    └── backtraking(1) [Row 1]
#     │          └── (Try valid placements for row 1 based on state from (0,2))
#     │
#     └── Place queen at (0,3)  [State: col={3}, pos_diag={0+3=3}, neg_diag={0-3=-3}]
#          └── backtraking(1) [Row 1]
#                └── (Try valid placements for row 1 based on state from (0,3))
