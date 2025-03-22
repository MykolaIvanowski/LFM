# given two tree, check if they have the same structure
#
# Input: p = [1,2,3], q = [1,3,2]
# Output: false
#
#       4                    4
#      / \                  / \
#     2   7      !=        7   2
#    /\   /\              /\   /\
#   1  3  6 9            9  6  3 1
#
#       4                    4
#      / \                  / \
#     7   2      ==        7   2
#
#       4                    4
#      / \                  / \
#     2   7      !=        2   7
#                         /
#                         9
from collections import deque


class  TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def same_tree(self, first: TreeNode, second:TreeNode)-> bool:
        # None == None it is the same
        if not first or not second:
            return True
        # if node is exist and value the same keep checking the structure
        if first and second and second.val==first.val:
            # on the same level check if methods return True and True
            r = self.same_tree(first.right,second.right) and self.same_tree(first.left,second.left)
            return r
        else:
            return False


class SolutionDFSIterative:
    def is_same_tree(self, first, second):
        stack = [(first,second)]

        while stack:
            node1, node2 = stack.pop()

            # node are not exists ant it is true, must continue
            if not node1 and not node2:
                continue

            # structure or value not the same
            if not node1 or not node2 or node1.val != node2.val:
                return False

            # append to stack node for future checks
            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))

        return True


class SolutionBFSIterative:
    def is_same_tree(self, first, second):
        queue1 = deque([first])
        queue2 = deque([second])


        while queue1 and queue2:
            for _ in range(len(queue1)):
                node1 = queue1.popleft()
                node2 = queue2.popleft()

                # if nodes is None it is then same structure
                if node1 is None and node2 is None:
                    continue
                # is Structure or values not the same
                if node1  is None or node2 is None or node2.val != node1.val:
                    return False

                # add nodes to queue for future checks
                queue1.append(node1.left)
                queue1.append(node1.right)
                queue2.append(node2.left)
                queue2.append(node2.right)

        return True



