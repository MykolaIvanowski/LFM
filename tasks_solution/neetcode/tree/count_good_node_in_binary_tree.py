# given binary tree, find good nodes,
# if leaf less than root is the good node, if leaf is less than root it is bad node
# return quantity of good node
#
# Input: root = [2,1,1,3,null,1,5]
# Output: 3
#
#       2              good node is 2,3,5
#      / \              quantity 3
#     1   1
#    /   / \
#   3    1  5
#
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def good_nodes(self, root: TreeNode)-> int:

        def depth_first_search(node, max_val):
            if not node:
                return 0 # return zero if leaf is None

            # compare current node value with value maximum in a branch (max_value)
            # max_value  can be root value or some parent value
            # this mean that we find good node (if true)
            res  = 1 if node.val >= max_val else 0

            # assign max value in param max_value (check if max value cahnge)
            max_val  = max(max_val,node.val) #

            # go to leafs and summ result
            res += depth_first_search(node.left, max_val)
            res += depth_first_search(node.right, max_val)
            return res

        return depth_first_search(root,root.val)


t33 = TreeNode(3)
t31 = TreeNode(1)
t35 = TreeNode(5)
tl21 = TreeNode(1,t33)
tr21 = TreeNode(1,t31,t35)
root  = TreeNode(2,tl21,tr21)

obj = Solution()
r = obj.good_nodes(root)
print(r)


class SolutionBFS:
    def good_nodes(self, root: TreeNode)-> int:
        res  = 0
        queue = deque()

        queue.append((root,-float('inf')))

        # iterate while we have nodes in queue
        while queue:
            node, max_value = queue.popleft()

            # if current node is greater than max value (root, parent value)
            # we find good node and can add +1 to result
            if node.val >= max_value:
                res+=1

            # append left, right node to queue and check max_value for next iteration and add it
            if node.left:
                queue.append((node.left, max(max_value, node.left.val)))
            if node.right:
                queue.append((node.right,max(max_value, node.right.val)))

        return res

obj1 = SolutionBFS()
r = obj1.good_nodes(root)
print(r)