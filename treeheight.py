# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/
# Height of binary tree starting from zero
def height(root):
    return maxDepth(root)


def maxDepth(node):
    if node is None:
        return -1
    else:
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

    return max(lDepth, rDepth)+1


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print(height(root))
