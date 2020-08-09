def leafSum(node):
    if node == None:
        return 0
    if node.left == None and node.right == None:  # leaf
        return node.data

    total = leafSum(node.left)
    total += leafSum(node.right)
    return total
