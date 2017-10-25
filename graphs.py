# Create cyclic graph
# Iterate through graph, summing all values


class GraphNode:
    def __init__(self, val, children = None):
        self.val = val
        self.children = children if children else list()


vals = [6, 4, 4, 12, 3, 8, 2, 18]

a = GraphNode(vals[0])
b = GraphNode(vals[1])
c = GraphNode(vals[2])
d = GraphNode(vals[3])
e = GraphNode(vals[4])
f = GraphNode(vals[5])
g = GraphNode(vals[6])
h = GraphNode(vals[7])

adjacencies = {
    a: [b, d, e],
    b: [a, c, e],
    c: [b, e],
    d: [a, g],
    e: [a, b, c, g, f],
    f: [e, h],
    g: [e, h],
    h: [g, f],
}

visited_nodes = []


# For each node in list:
#   Add value to sum
#   Add each child to second list
# Repeat for any nodes in second list
# Return sum

def bfs_sum(node_list):

    children = list()
    total = 0

    for node in node_list:
        if node not in visited_nodes:
            total += node.val
            visited_nodes.append(node)
            children.extend(adjacencies[node])

    if len(children) > 0:
        total += bfs_sum(children)

    return total


print(bfs_sum([a]))
print(sum(vals))
