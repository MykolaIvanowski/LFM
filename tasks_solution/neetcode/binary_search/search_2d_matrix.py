from typing import List


class Solution:
    def search_2d_matrix(self, target: int, matrix: List[List[int]])-> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        top = 0
        bottom = rows-1

        # find in matrix array that might contains target value
        # check last or first element in array
        # then update top/bottom for subarray search in binary search maner
        while top<=bottom:
            row = (top+bottom)//2

            if target > matrix[row][-1]:
                top = row+1
            elif target < matrix[row][0]:
                bottom = row-1
            else:
                break

        # The loop continues until top exceeds bot,
        # indicating that all possible rows have been checked
        if not (top<=bottom):
            return False

        # as top and botton change next  line count the subarray where neet check target
        row=(top+bottom)//2
        left, right=0,columns-1

        # find in subarray target number in binary serch maner
        while left<= right:
            middle = (left-right)//2

            if target > matrix[row][middle]:
                left=middle+1
            elif target < matrix[row][middle]:
                right=middle-1
            else:
                return True

        return False