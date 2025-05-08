import collections  # given list of words (array), and begin word (str), end word (str)
from collections import deque
# all word in list, bbegin word, end word have the same length
 # build a graph like : begin_word -> [words from list] -> end_word
 # this word_nodes can change only for one latter
 # example => als - begin, bek - end :   als -> all -> bll -> bel - bek
 #
# Input: beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sag","dag","dot"]
# Output: 4
#
# Input: beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sat","dag","dot"]
# Output: 0
#
from typing import List


class Solution:
    def ladder_length(self, begin_word: str, end_word: str, word_list: List[str])-> int:
        if end_word not in word_list:
            return 0

        neighbor = collections.defaultdict(list)
        word_list.append(begin_word)

        for word in word_list:
            for i in range(len(word)):
                pattern =word[: i ] + '#' + word[i+1:]
                neighbor[pattern].append(word)

        visit = set([begin_word])
        queue = deque([begin_word])
        result = 1
        while queue:
            for i in range(len(queue)):
                word  = queue.popleft()
                if word == end_word:
                    return result
                for j in range(len(word)):
                    pattern =word[: j]+ '#' + word[j+1:]
                    for neighbor_word in neighbor[pattern]:
                        if neighbor_word not in visit:
                            visit.add(neighbor_word)
                            queue.append(neighbor_word)

            result+=1
        return 0
