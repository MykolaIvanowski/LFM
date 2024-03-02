# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False

    return (same_tree(p.left,q.left) and same_tree(p.right, q.right))
