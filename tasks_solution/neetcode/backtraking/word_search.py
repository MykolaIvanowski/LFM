# given 2 -D grid (matrix) with chars, given word
# find a word in this bord
#
# Input:
# board = [
#   ["A","B","C","D"],
#   ["S","A","A","T"],
#   ["A","C","A","E"]
# ],
# word = "CAT"
# # Output: true
#
#
# Input:
# board = [
#   ["A","B","C","D"],
#   ["S","A","A","T"],
#   ["A","C","A","E"]
# ],
# word = "BAT"
# Output: false
from typing import List


class Solution:
    def exists(self, board: List[List[str]], word: str)-> bool:
        rows, columns = len(board), len(board[0])

        def dfs(r_index,c_index,w_index):
            # find max matches for letters,
            if w_index == len(word):
                return True

            # in this if check current letter from worth match for boars letter, if not then false
            if(     # row, column indexes should not be less than 0 or greater equal than max lenth
                    r_index < 0 or c_index < 0 or r_index >= rows or c_index >= columns or

                    # also word symbol should be equal to letter in given bord
                    word[w_index] != board[r_index][c_index] or

                    # give board symbol can not be equal to symbol @
                    board[r_index][c_index] == '@'
                ):
                return False

            # assign to specific letter position special character
            # we find matches and assign ti this special character
            # this is for not check the same character twice
            board[r_index][c_index] = '@'

            result = (
                # check down row the same colum
                dfs(r_index+1, c_index, w_index+1) or
                # check up row the same column
                dfs(r_index-1, c_index, w_index+1) or
                # check the same row right column
                dfs(r_index, c_index+1, w_index+1) or
                # check the same row left colum
                dfs(r_index, c_index-1, w_index+1)
            )
            # revert assined special character, in case next checks
            board[r_index][c_index] = word[w_index]
            return

        # start checkin matrix from left to right from up to down
        # [ first  [first] [second] [n]
        #   second [first] [second] [n]
        #   n      [first] [second] [n]]
        for r in range(rows):
            for c in range(columns):
                print(r,c)
                if dfs(r,c,0):
                    return True

        return False


obj = Solution()
r = obj.exists( [
  ["A","B","C","D"],
  ["S","A","c","T"],
  ["A","C","A","E"]], 'CAT')
print(r)