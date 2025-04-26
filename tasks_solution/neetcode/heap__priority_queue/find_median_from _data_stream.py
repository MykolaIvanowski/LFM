# given an sorted array (or actually stream), find a median in this stream
# median it is value in middle example [1,2,3] - median is 2
# or [1,3,4,5] median is (3+4)/2 = 3.5
#
# implement the method for class:
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far.
#
#
# Input:
# ["MedianFinder", "addNum", "1", "findMedian", "addNum", "3" "findMedian", "addNum", "2", "findMedian"]
# Output:
# [null, null, 1.0, null, 2.0, null, 2.0]
#
# Explanation:
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.findMedian(); // return 1.0
# medianFinder.addNum(3);    // arr = [1, 3]
# medianFinder.findMedian(); // return 2.0
# medianFinder.addNum(2);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
#
import heapq


class Solution:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def add_num(self, num: int)-> None:
        # in next if section number adds to max heap in case max heap not empty
        # and number is greater than first element
        if self.max_heap and num > self.max_heap[0]:
            heapq.heappush(self.max_heap,num)
        else:
            # if max heap is empty or first element less than number then add to min heap
            heapq.heappush(self.min_heap, -1 * num)

        # now time to balance min and max heaps

        #if min heap greater than max heap on 2 indexes then pop value and put it in max heap
        # as result we have equal heaps
        if len(self.min_heap) > len(self.max_heap)+1:
            value = -1 * heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, value)
        # in case we have max heap greater on 2 indexes than min heap (example len(4) > len(2) )
        #  then remove element from max heap and add it to min heap
        # as result we have two equal heaps
        if len(self.max_heap) > len(self.min_heap)+1:
            value = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -1 * value)

    def find_median(self)-> float:
        #return first value in min heap because min heap larger, it have median number
        if len(self.min_heap) > len(self.max_heap):
            return -1 * self.min_heap[0]
        # max heap greater than min heap it contain median value
        elif len(self.max_heap) > len(self.min_heap):
            return  self.max_heap[0]
        # if min_heap == max_heap we should return median number on formula (a+b)/2
        return (-1*self.min_heap[0] + self.max_heap[0]) / 2.0   # use 2.0 instead 2 because we want return decimal(float)
