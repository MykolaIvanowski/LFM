# given a binary tree, find depth this tree
#
#       4           depth of this tree is 3
#      / \
#     2   7
#         /\
#         6 9
#
# Input: root = [1,2,3,null,null,4]
# Output: 3
from collections import deque
from time import sleep
from typing import Optional, no_type_check_decorator


class TreeNode:
    def __init__(self, val=0, left=None, rigth=None):
        self.val=val
        self.left=left
        self.right=rigth


class SolutionDFS:
    def maximum_depth(self, root: Optional[TreeNode])->int:
        if not root:
            return 0
        # at the surfacing stage it return numbr stage and we check what is maximum
        res = 1 + max(self.maximum_depth(root.left),self.maximum_depth(root.right))

        return res

class SolutionBFS:
    def maximum_depth(self, root: Optional[TreeNode])->int:
        if not root:
            return 0
        queue = deque([root])
        level = 0


        while queue:
            # add to queue nodes
            # this cycle run on one level and add nodes from under current level
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
        return level


class SolutionDFSIterative:
    def maximum_depth(self, root:Optional[TreeNode])-> int:
        stack = [[root,1]]
        result = 0

        #firs we check right deepest leaf , go to 4->7->9,
        # because this nodes usually add last to stack and used first (pop)
        while stack:
            node, depth = stack.pop()
            if node:
                result = max(result,depth)
                # the last element added to stack is the deepest element
                # add also left None, right None element
                stack.append([node.left,depth+1])
                stack.append([node.right,depth+1])

        return result


t1 = TreeNode(1)
t3 = TreeNode(3)
t6 = TreeNode(6)
t9 = TreeNode(9)
t2 = TreeNode(2,t1,t3)
t7 = TreeNode(7,t6,t9)
t4 = TreeNode(4,t2,t7)

obj = SolutionDFSIterative()
r = obj.maximum_depth(t4)
print()