# given two arrays,they represent the same binary tree
# preorder store as [root,left subtree, right subtree], inorder store as [left subtree, root, right subtree]
#
# Input: preorder = [1,2,3,4], inorder = [2,1,3,4]
# Output: [1,2,3,null,null,null,4]
#
# preorder traversal is when we check (add, print) node in the first visit node
# inoreder traversal is when we check node in the second visit node
# postoreder traversal when we check third vised (it is the last time when we visit node)
#
from typing import Optional,List


class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right


class SolutionDFS:
    def build_tree(self, preorder: List[int],inorder :List[int])-> Optional[TreeNode]:
        preorder_index  = inorder_index = 0

        def dfs(parent_value):
            nonlocal  preorder_index, inorder_index
            # print('pre', preorder_index)
            # print('ino', inorder_index)
            # array are finished, no more nodes
            if preorder_index >= len(preorder):
                return None
            # limit is node value it help control recursive construction of the binary tree
            # if node value and value in array the same it means node has no leafs
            # why?    [a,b,c]
            #         [b,a,c]
            # it will check value under index and value, [0](b) == b, and then [1](a) == a
            if inorder[inorder_index] == parent_value:
                # prepare pointer for processing nodes in the next subtree
                # move pointer to next index in array inoreder
                inorder_index += 1
                return None

            root = TreeNode(preorder[preorder_index])
            # helps build nodes all nodes
            preorder_index += 1 # main counter to go through all possible nodes helps end cycle

            # use for construction left branch
            root.left = dfs(root.val)

            # construction right branch
            root.right = dfs(parent_value)
            return root

        return dfs(float('inf'))



#            6
#           /  \
#          4    8
#         / \  / \
#        1  5  7  9
#
obj = SolutionDFS()
r = obj.build_tree([6,4,1,5,8,7,9],[1,4,5,6,7,8,9])
print(r)


class Solution:
    def build_tree(self,preorder : List[int], inoreder: List[int])-> Optional[TreeNode]:
        if not preorder or not inoreder:
            return None

        # create root node
        root = TreeNode(preorder[0])
        mid  = inoreder.index(preorder[0]) # take root index in inorder array

        # preorder[1: mid+1] contains the elements for the left subtree
        # inoreder[: mid] contains the structure of the left subtree.
        root.left = self.build_tree(preorder[1: mid+1], inoreder[:mid])

        # preorder[mid+1:] contains the elements for the right subtree
        # inoreder[mid+1:] contains the structure of the right subtree.
        root.right = self.build_tree(preorder[mid+1:], inoreder[mid+1:])

        return root

pre = [3,9,20,15,7]
ino = [9,3,15,20,7]

obj = Solution()
r = obj.build_tree(pre,ino)
print(r)