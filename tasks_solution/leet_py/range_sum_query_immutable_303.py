import itertools
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.numbers = [0] + list(itertools.accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.numbers[right+1] + self.numbers[left]




obj = NumArray([1,2,3,4,5])
print(obj.numbers)