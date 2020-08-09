# https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/

class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None


def lca(root, v1, v2):
 # Base Case
    if root is None:
        return None

    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if(root.info > v1 and root.info > v2):
        return lca(root.left, v1, v2)

    # If both n1 and n2 are greater than root, then LCA
    # lies in right
    if(root.info < v1 and root.info < v2):
        return lca(root.right, v1, v2)

    return root


# Let us construct the BST shown in the figure
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

n1 = 10
n2 = 14
t = lca(root, n1, n2)
print "LCA of %d and %d is %d" % (n1, n2, t.info)
