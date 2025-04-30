# give binary tree, find right side deepest branch
#
#       1
#      / \         right side branch is 1-3-7
#     2   3
#    /\   /\
#   4  5  6 7
#
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,3,7]
from collections import deque
from typing import Optional,List


class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right


class SolutionBFS:
    def right_side_view(self, root: Optional[int])->List[int]:

        result  = []
        queue = deque([root])

        while queue:
            right_side = None

            # this var represent number of nodes present in the current level
            queue_length = len(queue)

            for i in range(queue_length):
                node = queue.popleft()

                if node:
                    # the last signed node would be the right node
                    right_side = node

                    # if node not None then we add to queue
                    queue.append(node.left)
                    queue.append(node.right)

            if right_side:
                result.append(right_side.val)
        return result

t7 = TreeNode(7)
t6 = TreeNode(6)
t5 = TreeNode(5)
t4 = TreeNode(4)
t3 = TreeNode(3, t6,t7)
t2 = TreeNode(2,t4,t5)
t1 = TreeNode(1,t2,t3)

obj = SolutionBFS()
r = obj.right_side_view(t1)
print(r)


class SolutionDFS:
    def right_side_view(self, root: Optional[TreeNode])-> List[int]:
        result  = []

        def depth_first_search(node, depth):
            if not node:
                return None  # if node empty return None

            # depth represent level depth, first depth increasing happen when we go on the right leaf

            if depth == len(result):
                # add right node value, at the same time we increasing length of array result
                result.append(node.val)

            # go to left then right leafs
            depth_first_search(node.right, depth + 1)
            depth_first_search(node.left, depth + 1)

        depth_first_search(root,0)
        return result


obj1 = SolutionDFS()
r = obj1.right_side_view(t1)
print(r)