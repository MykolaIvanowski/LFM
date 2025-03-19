# given an binary tree, invert this tree
#
# Input: root = [3,2,1]
# Output: [3,1,2]
#
#       4                    4
#      / \                  / \
#     2   7      =>        7   2
#    /\   /\              /\   /\
#   1  3  6 9            9  6  3 1
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val = 0 , left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class SolutionDFS:
    def invert_binary_tree(self,root: Optional[TreeNode])-> Optional[TreeNode]:
        if not root:
            return None
        # swipe the left, right node
        temp_right = root.right
        root.right = root.left
        root.left = temp_right

        # go to another node for swipe
        self.invert_binary_tree(root.left)
        self.invert_binary_tree(root.right)

        return root


class SolutionBFS:
    def invert_binary_tree(self, root: Optional[TreeNode])-> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])
        # it will added to queue and swipe nodes like:
        # in t4 swipe t2 and t7; next add t7 and t2; next in t7 swipe t6 and t9 etc
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left # swipe leaf nodes
            if node.left:
                queue.append(node.left) # add leaf left t7
            if node.right:
                queue.append(node.right) # add leaf right t2

        return root

t1 = TreeNode(1)
t3 = TreeNode(3)
t6 = TreeNode(6)
t9 = TreeNode(9)
t2 = TreeNode(2,t1,t3)
t7 = TreeNode(7,t6,t9)
t4 = TreeNode(4,t2,t7)

obj = SolutionBFS()
t = obj.invert_binary_tree(t4)
print()
