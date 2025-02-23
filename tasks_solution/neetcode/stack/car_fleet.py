from typing import List


class Solution:
    def car_fleet(self, target: int, position: List[int],speed : List[int])-> int:
        pairs = [(p, s) for p,s in zip(position,speed)]
        pairs.sort(reverse=True)

        stack =[]
        for p,s in pairs:
            ## Calculate the time to reach the target for each car and append to stack
            stack.append((target-p)/s)
            if len(stack) > 1 and stack[-1]<=stack[-2]:
            # if car is have the same speed as first car it is count as one car
            # in this case means that car is pop from the stack
                stack.pop()
        return len(stack)

car_fleet = Solution()
print(car_fleet.car_fleet(12,[10,8,5,3],[2,4,1,1]))


# Pairs: [(10, 2), (8, 4), (5, 1), (3, 1)], target is 12
#
# Calculate the time to reach the target for each car:
# Car at position 10: (12 - 10) / 2 = 1
# Car at position 8: (12 - 8) / 4 = 1
# Car at position 5: (12 - 5) / 1 = 7
# Car at position 3: (12 - 3) / 1 = 9
#
# Process the stack:
# Add 1 (car at 10), stack = [1]
# Add 1 (car at 8), stack = [1, 1] → Pop 1, stack = [1] (not a new fleet)
# Add 7 (car at 5), stack = [1, 7]
# Add 9 (car at 3), stack = [1, 7, 9] ## cars are have the different speeds