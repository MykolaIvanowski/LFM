# give binary tree, check if it is balanced
# return true if balanced , false if not balanced
#
#   a   4                         a  4
#      / \                          /
#  b  2   7     <-balanced         7           <- not balanced
#         /\                      /\
#         6 9   c            b   9  6     c
#
#  height ab-1, ac-2          ab-2, ac-0
#  |ab - ac| <= 1 (True)    |ab-ac| <=1 (False)
#  it is balanced           it is not balanced
# node(subtrees) in balanced tree (left and right) should not have  differ in height more then 1
from lib2to3.fixes.fix_asserts import FixAsserts
from typing import Optional


class TreeNode:
    def __init__(self, val =0, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_balanced(self, root : Optional[TreeNode])->bool:
        def depth_for_search(root):
            if not root:
                return [True,0]
            # go recursively first to left leafs then to right trees
            left, right  = depth_for_search(root.left), depth_for_search(root.right)

            # abs function return number without minus,
            # check if leftand right is true and then
            # compare if left and right different height is less or equal to 1
            balance = left[0] and right[0] and abs(left[1]-right[1]) <= 1

            # return result for comparison left and right heights, and
            # return max height for left or right node
            return [balance, 1 + max(left[1],right[1])]

        return depth_for_search(root)[0]


t6 = TreeNode(6)
t9 = TreeNode(9)
t2 = TreeNode(2)
t7 = TreeNode(7, t6, t9)
t4  = TreeNode(4 , t2, t7)

obj = Solution()
r = obj.is_balanced(t4)
print(r)


class SolutionDFSIteration:
    def is_balanced(self, root: Optional[TreeNode])-> bool:
        stack = []
        node  = root
        last = None # help understand if node was processed
        depths = {}

        while stack or node:
            if node: # go first to left subtree
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    stack.pop()
                    # get value stored in hash for left and right node
                    left = depths.get(node.left,0)
                    right = depths.get(node.right,0)

                    if abs(left-right) > 1:
                        return False
                    # count max height for current node
                    depths[node] = 1 + max(right, left)
                    last = node
                    node = None
                else:
                    node = node.right # last we go to right sub trees


        return True

obj = SolutionDFSIteration()
r = obj.is_balanced(t4)
print()
