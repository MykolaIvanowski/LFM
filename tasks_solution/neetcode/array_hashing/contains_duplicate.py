from typing import List


class Solution:
        def has_duplicate(self, nums: List[int]) -> bool:
            visited = set()
            for num in nums:
                if num in visited:
                    return True
                visited.add(num)
            return False