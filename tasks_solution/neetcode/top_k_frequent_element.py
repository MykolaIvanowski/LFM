from typing import List


class Solution:
    def top_k_frequent(self, nums: List[int], k, int)->List[int]:
        count = {}
        freq = [[]  for i in range(len(nums)+1)]

        for num  in nums:
            count[num] = 1 + count.get(num, 0)
        for num, ctn in count.items():
            freq[ctn].append(num)

        res=[]
        for i in range(len(freq)-1,0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
