# given binary tree, return array (matrix) with values separated by level.
#
# example:
#
#       1               # first level [1].
#      / \
#     2   3             # second level [2,3]
#    /\   / \
#   4  5  6  7          # third level [4,5,6,7]
#
# Input: root = [1,2,3,4,5,6,7]
# Output: [[1],[2,3],[4,5,6,7]]
#
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_order(self, root : Optional[TreeNode])->List[List[int]]:
        result = []

        def depth_first_search(node, depth):
            if not node: # empty root or finished level
               return None
            if len(result) == depth: # add level in matrix only 1 per level
                                    # why it is work? because level start from 0 but depth start from 0
                                    # len(matrix)is +1 than depth
                result.append([])

            # add value based on level structure matrix[level] = add node value
            result[depth].append(node.val)

            # when we go deper add +1 for depth (to check correct level in  len(m) == depth)
            depth_first_search(node.left, depth+1)
            depth_first_search(node.right, depth+1)

        depth_first_search(root,0) # entry point
        return result

t7 = TreeNode(7)
t6 = TreeNode(6)
t5 = TreeNode(5)
t4 = TreeNode(4)
t3 = TreeNode(3, t6,t7)
t2 = TreeNode(2, t4,t5)
t1 = TreeNode(1, t2,t3)

obj = Solution()
r = obj.level_order(t1)
print(r)


class SolutionBFS:
    def breath_first_search(self, root : Optional[TreeNode])-> List[List[int]]:
        result = []
        queue = deque()
        queue.append(root)

        while queue:
            queue_len = len(queue) # it have the same number as level
            level = []

            # run cycle the same amount of iteration as possible nodes on level
            # example on level 1 only root node; on  level 3 we can have 4 nodes
            for i in range(queue_len):
                # on each iteration have pop node
                node = queue.popleft()
                if node:
                    level.append(node.val) # to level object add value from nodes

                    # save to queue left, right nodes
                    queue.append(node.left)
                    queue.append(node.right)

            if level:
                # add level array object with updated values from nodes
                result.append(level)

        return result

obj1 = SolutionBFS()
r = obj1.breath_first_search(t1)
print(r)