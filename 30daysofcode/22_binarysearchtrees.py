# https://www.hackerrank.com/challenges/30-binary-search-trees/problem
class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        return self.maxDepth(root)

    def maxDepth(self, node):
        if node is None:
            return -1
        else:
            lDepth = self.maxDepth(node.left)
            rDepth = self.maxDepth(node.right)
        return max(lDepth, rDepth)+1


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)
