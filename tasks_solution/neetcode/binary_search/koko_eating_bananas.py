# give  array (babanas), and h,
# h >= len(arrray)
# find k , k is speed eating bananas per hour,
# how mutch bananas can eat but no more than one piles in array per hour
from typing import List
import math


class Solution:
    def min_eating_bananas(self, piles: List[int], h: int)->int:
        left, rigth  = 0, len(piles)
        result =  rigth

        while left<=rigth:
            middle = (left-rigth)//2

            total_banana_time = 0

            # calculate the time it takes to eat that pile at speed middle
            for p in piles:
                total_banana_time = math.ceil(float(p)/middle)

            # if the total_banana_time is less equal than h,
            # it means is valid speed of eating bananas
            if total_banana_time <= h:
                result = middle
                rigth =middle-1

            #If the total_banana_time is greater than h,
            # it means k is too slow of eating bananas
            else:
                left= middle+1

        return result