# given array with chars, and n. This chars in array  represent task
# and n represent cooldown between identical tasks.
# find minimal time required to execute all given task (do not forget about cooldown)
# array [a,b,c,a,b,c] -> optimal sequence for tasks -> a->b->c->a->b->a  (no cooldown)
#                    not optimal sequence for tasks -> a->__a->b->__b->c->__c (__ represent cooldown or
#                    Idle time refers to periods during task scheduling when the CPU isn't actively
#                    executing any tasks)
#
# Input: tasks = ["X","X","Y","Y"], n = 2
# Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.
#
#
# Input: tasks = ["A","A","A","B","C"], n = 3
# Output: 9
# Explanation: A possible sequence is: A -> B -> C -> Idle -> A -> Idle -> Idle -> Idle -> A.
#
import heapq
from collections import Counter, deque
from typing import List


class Solution:
    def least_interval(self, tasks: List[str], n : int)-> int:
        # count every task and  store as value
        # example: task = [a,a,a,b] => count={a:3, b:1}
        count_hashmap = Counter(tasks) # made hash map
        max_heap = [-c for c in count_hashmap.values()] # take ints from hashmap and make the negative
        heapq.heapify(max_heap) # turn into min heap but we will have result as a max heap
        time  = 0 # result, or time required to execute tasks
        queue = deque()

        while max_heap or queue:
            time+=1 # new iteration new time for task

            # this if means that we do not have other choice as use cooldown
            # because in pool we have only the same chars (task)
            if not max_heap:
                time = queue[0][1] # task timer increased to timer + n (n - cooldown the same idle time)

            else:
                # get max value from (actually min because it is minheap) heap
                # and decrease it (actually increase because it is minheap)
                # also crucial that we pop from heap and that means that we do not take it to task again,
                # until it pushed back to heap
                current_task_time = 1 + heapq.heappop(max_heap) # for heap pop value in log n time
                if current_task_time:
                    # put recently taken counter to queue (counter for concrete char),
                    # and general time for tasks plus cooldown time - this in future help
                    # find when we should put back value from queue to heap
                    queue.append([current_task_time, time+n])

            if queue and queue[0][1] == time:
                # add task back (char) to heap for next task checks (scheduling)
                # as we add current_task_time back in next iteration it may be checked (calculated)
                heapq.heappush(max_heap, queue.popleft()[0])

        # return result
        return time

obj = Solution()
r = obj.least_interval(["A","A","A","B","C"], n = 3)
print(r)