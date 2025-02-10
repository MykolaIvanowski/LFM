class Solution:
    def is_anagram(self,s: str,t: str)-> bool:
        if len(s) != len(t):
            return False
        count_t, count_s = {}, {}
        for i in range(len(s)):
            count_t[t[i]] = 1 + count_t.get(t[i],0)
            count_s[s[i]] = 1 + count_s.get(s[i],0)
        return count_s == count_t