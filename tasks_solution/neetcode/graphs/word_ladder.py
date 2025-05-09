# given list of words (array), and begin word (str), end word (str)
# all word in list, begin word, end word have the same length
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
import collections
from typing import List
from collections import deque

class Solution:
    def ladder_length(self, begin_word: str, end_word: str, word_list: List[str])-> int:
        if end_word not in word_list:
            return 0

        neighbor = collections.defaultdict(list)
        word_list.append(begin_word) # add begin word to word list

        # run through  words in list
        for word in word_list:
            # run through all letters in current word
            for i in range(len(word)):
                pattern = word[: i ] + '#' + word[i+1:] # #ord-> w#rd ->wo#d ->wor#
                # (word without one letter) add pattern as key  and  as a value add word close to this pattern
                #  example { #at: [bat, tat, cat, ...]}
                # its add though several iteration
                neighbor[pattern].append(word)

        # add startign word to visit, because its already checked
        visit = set([begin_word])
        # add starting word to queue because we building graph from that word
        queue = deque([begin_word])
        # result 1 because we have in queue word for graph, (one one node it is also graph)
        result = 1
        print(neighbor)
        while queue:
             # run for loop as much as elements in queue
            for i in range(len(queue)):
                word  = queue.popleft()
                # if current word and end word is the same, that means we build graph
                if word == end_word:
                    return result
                # iterate through the each letter in the word
                for j in range(len(word)):
                    # made pattern for words from queue
                    pattern = word[: j]+ '#' + word[j+1:]#   #ord->w#rd->wo#d->wor#

                    # take pattern from the queue and iterate through dictionary values for this pattern
                    # find words match the same pattern
                    for neighbor_word in neighbor[pattern]:
                        print(neighbor_word)
                        # if values for key (pattern queue) not in visit lists to avoid cycles
                        # then add values (word from list) to visit list and add to queue
                        # so in next iteration we check if its match to end word for result
                        if neighbor_word not in visit:
                            visit.add(neighbor_word)
                            queue.append(neighbor_word)
            # finished check queue word and its patters
            # result go further (incremented)
            result+=1
            # in case no words we will have empty queue and its finished while loop then return 0 (no result)
        return 0


o = Solution()
o.ladder_length("cat",'sag',["bat",'tat',"bag","sag","dag","dot"])