# given two binary trees, find if they have the same nodes, structure
#
# Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]
# Output: false
#
# Input: root = [1,2,3,4,5], subRoot = [2,4,5]
# Output: true
#
#       4                       one  tree is subtree of another
#      / \
#     2   7      ==       7
#         /\             / \
#         6 9           6   9
#
#
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_subtree(self, root:Optional[TreeNode], subroot: Optional[TreeNode])->bool:
        if not subroot: # subroot (current node) is null
            return True
        if not root:
            return False # main root (main current node) is null (mean finished or not exists)

        # compare on current level roots and trees, values
        if self.same_tree(root, subroot):
            return True

        # go to comparing next left then rights leafs with subtrees
        return (self.is_subtree(root.left, subroot) or
                self.is_subtree(root.right, subroot))

    def same_tree(self, root:Optional[TreeNode], subroot: Optional[TreeNode])-> bool:
        if not root and not subroot: # root subroot is null
            return True

        # check if root and subroot (current node) are not null and they have the same values
        if  root and subroot and root.val == subroot.val:

            # if current nodes (roots) have the same value then go to next left,right leafs
            return (self.same_tree(root.left, subroot.left) and
                    self.same_tree(root.right, subroot.right))

        return False

t6 =  TreeNode(val=6)
t9 = TreeNode(val=9)
t7 =  TreeNode(val=7, left=t6,right=t9)
t2 = TreeNode(val=2)
t4 = TreeNode(val=4, left=2, right=t7)

st9 = TreeNode(val=9)
st6 = TreeNode(val=6)
st7  = TreeNode(val=7,left=st6,right=st9)

obj = Solution()
r = obj.is_subtree(t4,st7)
print(r)
