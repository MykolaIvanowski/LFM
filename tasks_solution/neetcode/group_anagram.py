from collections import defaultdict
from typing import List


class Solution:
    def group_anagram(self,s_arr:List[str])->List[List[str]]:
        r = defaultdict(list)
        for s in s_arr:
            count =[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            r[tuple(count)].append(s)
        return list(r.values())