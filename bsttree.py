def insert(root, node):
    if node.data < root.data:
        if root.left:
            insert(root.left, node)
        else:
            root.left = node
            node.parent = root.left
    elif node.data > root.data:
        if root.right:  # Node value is greater than root node
            insert(root.right, node)
        else:
            root.right = node
            node.parent = root.right
    # If node.data == root.data, do not insert


def check_balanced(root):
    leaf_levels = find_leaf_depths(root, 1)
    return max(leaf_levels) - min(leaf_levels) < 2


def find_leaf_depths(node, level):
    results = []
    if node.left:
        results.extend(find_leaf_depths(node.left, level + 1))
    else:
        results.append(level)
    if node.right:
        results.extend(find_leaf_depths(node.right, level + 1))
    else:
        results.append(level)
    return results


class Node:
    left = None
    right = None
    parent = None
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)


rootNode = Node(5)
numbers = [3, 2, 4, 7, 6, 10]
for num in numbers:
    insert(rootNode, Node(num))

balanced = check_balanced(rootNode)
pass