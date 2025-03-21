# give binery tree, chek if it is balanced
# return true if balanced , falce if not balanced


class Solution:
    def is_balanced(self, root : Optional[TreeNode])->bool:
        def depth_for_serch(root):
            if not root:
                return [True,0]

            left, right  = depth_for_serch(root.left), depth_for_serch(root.right)
            balance = left[0] and right and depth_for_serch(left[1]-right[1]) <= 1
            return [balance, 1+ max(left[1],right[1])]

        return depth_for_serch(root)[0]
