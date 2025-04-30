# given binary tree, find the maximum path sum, path can be any between one and more nodes
# find path with max sum
#
# Input: root = [1,2,3]
# Output: 6
#
# Input: root = [-15,10,20,null,null,15,5,-5]
# Output: 40
from typing import Optional


class TreeNode:
    def __init__(self,val=0, left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def max_path_sum(self,root:Optional[TreeNode])->int:
        result  = [root.val] # it is global tracker

        def depth_first_search(node):
            # if node is null return 0
            if not node:
                return 0

            # common dfs
            left_max=depth_first_search(node.left)
            right_max=depth_first_search(node.right)

            # if recursive method return negative values change it to zero
            left_max=max(left_max,0)
            right_max=max(right_max,0)

            # this line represent max path for node, left leaf, right leaf
            # and compare it with previous writed result and resign greater
            # this not return because it break path moving upward
            result[0] = max(result[0], node.val+left_max+right_max)

            # we take max from left or right because path can go through only one child
            # add with current parent node (root node)
            return node.val+max(left_max,right_max)

        depth_first_search(root)
        return result[0]


ta = TreeNode(-1)
tb = TreeNode(-3)
td = TreeNode(5)
te = TreeNode(8)
tc = TreeNode(4, ta, tb)
tf = TreeNode(10, td, te)
tg = TreeNode(8, tc, tf)

obj = Solution()
r = obj.max_path_sum(tg)
print(r)