# given binary tree where all nodes are unique, given two nodes p,q
# find lowes parent (ancestor) for this nodes p and q ,
#
# Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8
# Output: 5
#
# example
#
#       4                   p=2,q=7
#      / \                  lowes ancestor is 4
#     2   7
#    /\   /\                p=6,q=9 lowes ancestor is 7
#   1  3  6 9
#
#


class TreeNode:
    def __init__(self, val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowes_common_ancestor(self, root:TreeNode, p: TreeNode,q:TreeNode):
        # if root is None, it means no children
        if not root or not q or not p:
            return None

        # check if range between q,p is less than root go to right leafs
        if max(p.val,q.val) < root.val:
            return self.lowes_common_ancestor(root.left, p,q)

        # check if range between q,p is more than root go to right leafs
        elif min(p.val, q.val) > root.val:
            return self.lowes_common_ancestor(root.right,p,q)

        # if root is between p,q that mean we find lowest common ancestor
        else:
            return root

t1 = TreeNode(1)
t3 = TreeNode(3)
t6 = TreeNode(6)
t9 = TreeNode(9)
t2 = TreeNode(2,t1,t3)
t7 = TreeNode(7,t6,t9)
t4 = TreeNode(4,t2,t7)

obj = Solution()
r = obj.lowes_common_ancestor(t4,t6,t9)
print(r.val)


class SolutionIteration:
    def lowes_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
        current  = root

        while current:
            # if p,q range grater than root go to right leaf
            if p.val > current.val and q.val > current.val:
                current = current.right
            # if q,p range lower than root go to left
            elif p.val < current.val and q.val < root.val:
                current = current.left
            # if root value is between range p q then it is a lower common ancestor
            else:
                return current