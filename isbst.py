def isBSTUtil(node, mini, maxi):

    # An empty tree is BST
    if node is None:
        return True

    # False if this node violates min/max constraint
    if node.data < mini or node.data > maxi:
        return False

    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (isBSTUtil(node.left, mini, node.data - 1) and
            isBSTUtil(node.right, node.data+1, maxi))


def check_binary_search_tree_(root):
    return (isBSTUtil(root, -100000000, 100000000))

# A binary tree node


class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

if (check_binary_search_tree_(root)):
    print "Is BST"
else:
    print "Not a BST"
