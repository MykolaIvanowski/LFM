# given array, and prerequisite (it is represent grapth)
#  if course you wont take a you shuold take b,c
# check if courses do not have lock,
# like if for course a you need course  b for course b you need course a
# the pair [0,1] must be taken course 1 before course 0
#
# Input: numCourses = 2, prerequisites = [[0,1]]
# Output: true
#
# Input: numCourses = 2, prerequisites = [[0,1],[1,0]]
# Output: false
#
#
from typing import List


class Solution:
    def can_finish(self, num_courses:int, prerequisites : List[List[int] ])-> bool:
        # made dictionary from 0 to num_courses as keys with empty lists as values
        prerequisites_map = {i : [] for i in range(num_courses)}

        # add to map key integer from 0 column it represent parent course
        # add to map value integer from 1 column it represent child course
        for root_course,leaf_course in prerequisites:
            prerequisites_map[root_course].append(leaf_course)

        visiting  = set()

        def depth_first_search(course):
            # cycle in parent child courses
            if course in visiting:
                return False

            # course do not have requirements (grapgh do not have leaf)
            if prerequisites_map[course] == []:
                return True
            #  add course  in visited set
            visiting.add(course)
            print(visiting)
            # go to all leaf for current node, if the is loop we will find it and check it in visited  set
            # current 1 [1,0], 0 is leaf
            # check 1 [1,0] go to 0 [0,3] then go to 3 etc
            for parent_course in prerequisites_map[course]:
                if not depth_first_search(parent_course):
                    return False
            # this prevent infinite loop
            # incorrect results
            #  some times we can have root as child in later graph and it prevet from false result
            # [[1,0],[1,3],[2,1]] without this line it give incorrect result , (because if it were not removed)
            visiting.remove(course)
            # optimization trick, if we encounter course later we will return instead checking dependency
            # because we already check all dependency in for loop previously
            prerequisites_map[course] = []
            return True

        # we should call search for every single course we  have
        for c in range(num_courses):
            # if return False then return False
            if not depth_first_search(c):
                return False
        # we finish search for every course it mean the is no cycle in graph
        return True

o = Solution()
r = o.can_finish(4,[[1,0],[1,3],[2,1]])
print(r)