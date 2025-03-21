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
from typing import Optional, no_type_check_decorator


class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameter_of_binary_tree(self,root: Optional[TreeNode])-> int:
        res = 0 # use variable to store the result from recursion, mark as non local variable

        def depth_for_search(root):
            nonlocal res
            if not root :
                return 0

            left  = depth_for_search(root.left)
            right  = depth_for_search(root.right)
            # save result for left, right , res value to global variable
            res = max(res, left+right) # diameter is  left + right

            # trick, to count max depht and get from left or right
            return 1 + max(left, right)

        depth_for_search(root)

        return res


t6 = TreeNode(6)
t9 = TreeNode(9)
t2 = TreeNode(2)
t7 = TreeNode(7, t6, t9)
t4  = TreeNode(4 , t2, t7)

obj = Solution()
r = obj.diameter_of_binary_tree(t4)
print(r)


class SolutionIterativeDFS:
    def diameter_of_binary_tree(self, root:Optional[TreeNode])-> int:
        stack = [root] # neet use stack instead of recursion
        hash_result = {None: (0, 0)} # hashmap for store results

        while stack:
            node = stack[-1]

            # add nodes to stack from head to leaf
            if node.left and node.left not in hash_result:
                stack.append(node.left)
            elif node.right and node.right not in hash_result :
                stack.append(node.right)
            else:
                node =  stack.pop() # take a leaf
                # for added nodes we take diameter, and hight
                left_height, left_diameter = hash_result[node.left]
                right_height, right_diameter = hash_result[node.right]

                # calculate and check max height level, max diamete for parent node
                # if node not in hashe then add it
                hash_result[node] = ( 1 + max(left_height, right_height),
                                max(left_height+right_height, left_diameter, right_diameter)
                            )

        return hash_result[root][-1]


obj = SolutionIterativeDFS()
r = obj.diameter_of_binary_tree(t4)
print(r)
