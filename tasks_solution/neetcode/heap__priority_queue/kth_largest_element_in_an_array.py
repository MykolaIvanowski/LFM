# give an unsorted array, return k-th largest element in array
#
# Input: nums = [2,3,1,5,4], k = 2
# Output: 4
#
# Input: nums = [2,3,1,1,5,5,4], k = 3
# Output: 4
#
import heapq
from typing import List

# in python we use min heap
class SolutionHaep:
    def find_kth_largest(self, nums: List[int], k: int)-> int:
        # nlargest method return of list k-th largest elements
        return heapq.nlargest(k, nums)[-1] # turn array to heap and then with method nLarges return  k-th element



obj = SolutionHaep()
r = obj.find_kth_largest([1,2,4,2,1,4,6],3)
print(r)


# hole idea that we moved k-th largest element in index_k position
class SolutionQuickSelect:
    def find_kth_largest(self, nums: List[int], k : int)-> int:
        # index_k is variable which contains k index if array ware sorted
        # example: nums = [1,2,3,4,5,6], k = 2, index_k = 4
        index_k = len(nums)-k

        def quick_select(left, right):
            # pivot it is a element used for dividing array into two parts
            # point it is element or index and it progres when choosing smallest element
            # it help maintain the partitioning logic
            pivot , point = nums[right], left

            # iteration by iteration choose smallest element
            for i in range(left,right):
                if nums[i] <= pivot:
                    # if current element is less or equal to pivot element
                    # then switch index and point elements, then update point
                    nums[point], nums[i] = nums[i], nums[point]
                    point +=1

            # switch pivot element with first element in second partition;  it is mean:
            # we have on the left array side values less or equal to point value
            # on the right array side we have values greater or equal to point value
            nums[point], nums[right] = nums[right], nums[point]

            if point > index_k:
                # k-th largest in left partition, pass parameters for left partition
                return quick_select(left, point-1)
            elif point < index_k:
                # k-th largest in rigth partition, pas parameters for right partiton
                return quick_select(point+1, right)
            else:
                # point = index_k
                return nums[point] # we find result
        # entry point
        return quick_select(0, len(nums)-1)


obj = SolutionQuickSelect()
r = obj.find_kth_largest([1,2,43,4,5,3,2,2,4],2)
print(r)