class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.results = []
        if not root:
            return self.results

        self.traverse(root, [str(root.val)])

        return self.results


    def traverse(self, root, path):
        if not root.left and not root.right:
            path_str = "->".join(path)
            self.results.append(path_str)
            return

        if root.left:
            path.append(str(root.left.val))
            self.traverse(root.left, path)
            path.pop()

        if root.right:
            path.append(str(root.right.val))
            self.traverse(root.right, path)
            path.pop()