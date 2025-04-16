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

            if(r_index< 0 or c_index < 0 or r_index >= rows or c_index >= columns or
                word[w_index] != board[r_index][c_index] or board[r_index][c_index] == '@
                ):
                return False

            board[r_index][c_index] = '@'

            result = (
                dfs(r_index+1, c_index, w_index+1) or
                dfs(r_index-1, c_index, w_index+1) or
                dfs(r_index, c_index+1, w_index+1) or
                dfs(r_index, c_index-1, w_index+1)
            )
            board[r_index][c_index]=word[w_index]
            return result

        for r in range(rows):
            for c in range(columns):
                if dfs(r,c,0):
                    return True

        return False


