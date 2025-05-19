# gives string and given array of string
# find if string contains word from array
# the match must be complete return bool
# [ q, b, c] 'qbc'  match
# [ a, b, c] 'abcd' not mach
#
# Input: s = "neetcode", wordDict = ["neet","code"]
# Output: true
#
# Input: s = "applepenapple", wordDict = ["apple","pen","ape"]
# Output: true
#
# Input: s = "catsincars", wordDict = ["cats","cat","sin","in","car"]
# Output: false
#
#
from typing import List


class SolutionTopDown:
    def word_break(self, s: str, word_dict: List[str])-> bool:
        cache = {len(s): True}

        def dfs(i):
            # if index in cache that means e check word then return value from cache
            if i in cache:
                return cache[i]

            # run through every word in array
            for w in word_dict:
                # check if we in range of checked s word if ((i + len(w)) <= len(s)
                # segment in checked s word is equal to word from array
                if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
                    # if segment equal to word from array then pass index to check next segment in next recursive call
                    if dfs(i + len(w)):
                        # if dfs method returned true then we add it to cache
                        # we add match segment in cache, as we use dfs we check from last word till first
                        # cache looks like {14: true, 10: True, 5:True, 0: True}
                        # if 0: True then entire s have words from array
                        cache[i] = True

                        return True
            # we finish all words and not achieved complete matches, so return false
            cache[i] = False
            return False
        # entry point
        return dfs(0)


obj = SolutionTopDown()
obj.word_break('newwordsandcar',['words', 'car','cats', 'new', 'and'])


class SolutionBottomUp:
    def word_break(self, s: str, word_dict:List[str])->bool:
        dp_cache = [False] * (len(s)+1) # array were we store results of mutch
        dp_cache[len(s)] = True # it is corresponds to the empty substring which is always valid segmentation

        # go through loop from last till first element
        for i in range(len(s)-1,-1,-1):
            # run for every word in the array
            for w in word_dict:
                # check if we in s word range (i+ len(e)) <= len(s)
                # and check if specific segment match with current word s[i:i+len(w)]==w
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    # segment match with a word from array
                    # write True to dp_cache, if previous match also True -
                    # True is moving forward for every next match

                    # why it can set false, because we iterate for every index each word and it means then we can have
                    # match in s[i: i + len(w)] == w, but sequence not completed
                    # example [cat,car] 'catvcar' s[i: i + len(cat)] == cat ->True but we need word catv, so set False
                    dp_cache[i] = dp_cache[i+len(w)]

                # when it true we found valid word , so break the loop, go to next  higher loop for next check
                # it prevent unnecessary computation
                if dp_cache[i]:
                    break

        return dp_cache[0]


obj = SolutionBottomUp()
print(obj.word_break('newwordsandscar',['words', 'car','cats', 'new', 'and']))

