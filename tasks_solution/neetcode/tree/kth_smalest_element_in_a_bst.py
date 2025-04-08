# given binary search tree and k, find smallest value in this tree in k position (index)
#
# Input: root = [2,1,3], k = 1
# Output: 1
#
# Input: root = [4,3,5,2,null], k = 4
# Output: 5
#
# tip solutions
#
#
#              6  (4)                 this is a binary search tree
#            /   \                    in parentheses represent indexes of binary search tree
#     (2)  4      8  (5)              array representation:
#         /\      / \                 1 2 3 4 5 6 7  - index
#   (1)  1  5    7   9  (7)           1 4 5 6 8 7 9  - value
#          (3)  (6)
#
#
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right


class SolutionDFSRecursive:
    def kth_smallest(self, root:Optional[int], k: int)-> int:
        index_representation = k
        result = root.val

        def depth_for_search(node):
            nonlocal index_representation,result  # use nonlocal to have the same variable in any dfs recursive call
            if not node:
                return

            depth_for_search(node.left)
            # this line plays crucial role in finding k-th element
            # it will -1 to variable every time when you move to next index (array representation of bst)
            index_representation -= 1

            # update result when index representation is 0
            # it means we find a solution  but we still traverse all tree
            if index_representation == 0:
                result = node.val
                return
            # why it is work for right tree, because we still have left nodes as None
            # and it count -1 when nodes are None
            depth_for_search(node.right)

        depth_for_search(root)

        return result

t3 = TreeNode(val=3)
t1 = TreeNode(val=1)
t6 = TreeNode(val=6)
t9 = TreeNode(val=9)
t7 = TreeNode(val=7, left=t6,right=t9)
t2 = TreeNode(val=2, left=t1, right=t3)
t4 = TreeNode(val=4, left=t2, right=t7)

obj = SolutionDFSRecursive()
r = obj.kth_smallest(t4, 7)
print(r)

class SolutionDFSIterative:
    def kth_smallest(self, root: Optional[int], k: int)-> int:
        stack = []
        current = root

        while stack or current:
            # adding nodes from left branches
            # it actually add elements in descending order
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            print(current.val)
            # after pop element we count down counter
            # it help reach k-th element in bst, as we have bst
            # we pop elements in growing sequence
            k -= 1

            if k  == 0:
                return current.val
            # adding right element not contaminate descending order
            current = current.right



obj  = SolutionDFSIterative()
r = obj.kth_smallest(t4, 3)
print(r)