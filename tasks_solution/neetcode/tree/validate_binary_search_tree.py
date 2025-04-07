# given binary tree, validate if it is  binary search tree
# in BST left values less than parent, right values grater than parent
#
# Input: root = [2,1,3]
# Output: true
#
# Input: root = [1,2,3]
# Output: false
#
# example:
#
#       4                       5
#      / \                     / \
#     2   7   <-BST           4   6    <- not BST (1 is less than 5,6; 6 is greater than 4, 5)
#    /\   /\                 /\   /\
#   1  3  6 9               3  6  9 1
#
#
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def validate_binary(self, root: Optional[TreeNode])-> bool:
        def valid_bst(node, left,right):
            if not node:
                return True
            # checking if all in the left subtree nodes are less than the node values
            # checKing if all in the right sutree nodes are greater than the node values
            if not (left < node.val < right):
                return False

            # trick is how to pass params,

            # when we go to left sutree we need pass left parent value for left param;
            # and current node value for right
            # invert fo right subtree, we need pass current node value for left param;
            # and right parent value for right param;
            #  it will help check correct range in next recursive call
            return (valid_bst(node.left, left, node.val) and                                    # for left param
                    valid_bst(node.right, node.val, right))

        return valid_bst(root, float('-inf'), float('inf'))

t1 = TreeNode(1)
t3 = TreeNode(3)
t6 = TreeNode(6)
t9 = TreeNode(9)
t2 = TreeNode(2,t1,t3)
t7 = TreeNode(7, t6, t9)
t4 = TreeNode(4, t2,t7)

obj = Solution()
r = obj.validate_binary(t4)
print(r)

class SolutionBFS:
    def is_valid_bst(self, root: Optional[TreeNode])-> bool:
        queue = deque([(root, float('-inf'),float('inf'))])

        while queue:
            node, left, right = queue.popleft()

            # check if node value in left subtree less than parents values
            # and check if node value in the right subtree greater than parents values
            if not (left < node.val < right ):
                return False

            # we add to queue left node and parent value on left position and current node value to right position
            # then we add to queue right node and current value to left position and parent value to right position
            # in future iterations it will help check correct range for left,right nodes
            if node.left:
                queue.append((node.left, left, node.val))
            if node.right:
                queue.append((node.right, node.val, right))

        return True

obj1 = SolutionBFS()
r = obj1.is_valid_bst(t4)
print(r)