# given binary tree, write method serialize, deserialize
#
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
#
# Input: root = []
# Output: []
#
from collections import deque

from base.enumerate_function import index


class TreeNode:
    def __init__(self, val=0, left=None, right =None):
        self.val=val
        self.left=left
        self.right=right


class SolutionDFS:
    def serialization(self, root):
        result = []

        def dfs(root):
            if not root:
                # if it is end of tree append Nan and finish call
                result.append('Nan')
                return
            # add value to result
            result.append(str(root.val))

            dfs(root.left)
            dfs(root.right)

        # serialise and return
        return ','.join(result)

    def deserialization(self,data):
        self.data = data.split(',')
        self.i  = 0 # iterative counter

        def dfs_deserialize():
            if self.data[self.i] == 'Nan':
                self.i +=1
                return None
            node = TreeNode(int(self.data[self.i]))
            self.i += 1
            # as we use preorder traversal(left) than call for left then for right subtrees
            node.left = dfs_deserialize()
            node.right = dfs_deserialize()
            return node
        return dfs_deserialize()


class SolutionBFS:
    def serialization(self, root):
        if not root:
            return 'Nan'
        result =[]
        queue = deque([root])

        while queue:

            node = queue.popleft()
            if not node:
                result.append('Nan')# if reach the end of tree add Nan
            else:
                # save node to result array in bfs maner
                result.append(str(node.val))
                # add nodes to qeueu for future iteration
                queue.append(node.left)
                queue.append(node.right)
        return ','.join(result)

    def deserialization(self, data):
        values = data.split(',')
        if values == 'Nan':
            return None
        root = TreeNode(int(values[0]))# create root node
        queue = deque([root])
        i = 1

        # we iterate until queue is not empty,
        # but real date store in arrays and we iterate on it separately
        while queue:
            node = queue.popleft()

            # start from the left node because we add in queue left node first
            if values[i] != 'Nan':
                # if in values not  Nan that means we have node
                # create node
                node.left = TreeNode(int(values[i]))
                # add left node first to the queue
                queue.append(node.left)
            i+=1 # count iterate,
            if values[i] != 'Nan':
                # add node to left subtrees
                node.right = TreeNode(int(values[i]))
                # add second time node to right subtree
                queue.append(node.right)
            i+=1
        return root