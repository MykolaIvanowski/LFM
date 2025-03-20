# given tree, find a diameter
# two max height conjunct through the same node
#
# Input: root = [1,null,2,3,4,5]
#
# Output: 3

#       4 - c          ca + cb = diameter or(cd+cb)
#      / \
#  b- 2   7
#         /\
#      d- 6 9 - a
from typing import Optional


class TreeNode:
    def __init__(self,val, left, right):
        self.val =val
        self.left = left
        self.right= right


class Solution:
    def diameter_of_binary_tree(self,root: Optional[TreeNode])-> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root :
                return 0
            left  = dfs(root.left)
            right  = dfs(root.right)
            res = max(res, left+right)

            return 1 + max(left, right)
        dfs(root)

        return res
