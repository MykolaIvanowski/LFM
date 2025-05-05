# given an array it is prerequisite, and number of courses
#  array represent the dependence between courses
#  number of courses we are required to take
# return a valid ordering of courses you can take to finish all courses
#
# [[1, 0]]- in order to take course 1 we have to take finish course 0
# [[0,1],[1,0]] for finish course 0 we have to take course 1, and for course 1 we have to take 0 (it is loop)
#
#
# Input: numCourses = 3, prerequisites = [[1,0]]
# Output: [0,1,2]
#
# Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]
# Output: []
#
#
from typing import List


class Solution:
    def can_order(self, num_courses: int, prerequisite: List[List[int]] )-> List[int]:
        # create map for curses and requirements
        prerequisite_dictionary = {c:[] for c in range(num_courses)}

        # filed in hash map, to course add all required courses
        for current_course, course_required in prerequisite:
            prerequisite_dictionary[current_course].append(course_required)

        # we need hash set to track, visited courses and trek cycle
        visit, cycle = set(), set()
        result = []

        # course node have three states:
        # visited - has been added to result
        # visiting  -  not added to result but added to cycle hashset
        # unvisited - course node not added to cycle or result
        def depth_first_search(course):
            # detect cycle , because visited twice, so return False
            if course in cycle:
                print('f')
                return False
            # if course was visited no need visit again, so return true skip rest of graph search
            if course in visit:
                return True

            # add course to visit hash set, for detecting cycle
            cycle.add(course)

            # recursive loop for searching graph
            # [0,1],[1,3] - first take 0 and find 1, next recursive call take 1 find 3 (pass as parameter), next etc
            for p in prerequisite_dictionary[course]:
                print(p)
                if depth_first_search(p) == False:
                    return False
            # after recursive call we reach the end of graph if no cycle then
            # remove current course from cycle because no cycle
            cycle.remove(course)
            # as we visited course node and check it no need to do the same, so add to visit hash set
            visit.add(course)
            # current node is part of result

            result.append(course)
            return True

        # run every possible course to check if it have required courses
        for c in range(num_courses):
            # if return False it is mean the is cycle in graph
            if depth_first_search(c) == False:
                return []

        return result



obj = Solution()
r = obj.can_order(5,[[1,0],[1,3],[2,1]])
print(r)
