Graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('E', 5), ('D', 1)],
    'D': [('C', 1), ('E', 8)],
    'E': [('J', 5), ('I', 5)],
    'F': [('G', 1), ('H', 7)],
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('J', 3), ('E', 5)],
}
Approximate_Cost = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 1,
    'J': 0
}


def Path_Cost(path):
    g_cost = 0
    # loop to find g_cost
    for (node, cost) in path:
        g_cost += cost
    # the last node in the path
    last_node = path[-1][0]
    # last node cost
    h_cost = Approximate_Cost[last_node]
    # total cost
    f_cost = g_cost + h_cost
    return f_cost, last_node


def A_star(graph, start, goal):
    # the visited list
    visited = []
    # the queue list
    queue = [[(start, 0)]]
    while queue:
        # sort the queue by the path cost
        queue.sort(key=Path_Cost)
        path = queue.pop(0)
        node = path[-1][0]
        # if the node in visited continue the loop
        # else append it to the visited list
        if node in visited:
            continue
        visited.append(node)
        # check if the node is the goal return the path
        # else add the adjacent of the node to the queue
        if node == goal:
            return path
        else:
            adj_nodes = graph[node]
            for node in adj_nodes:
                new_path = path.copy()
                new_path.append(node)
                queue.append(new_path)

# Start node -> Goal node
solution = A_star(Graph, 'A', 'J')
print("Path : ", end=" ")
for i in solution:
    print(i[0], end=" ")
print()
print("Cost = ", Path_Cost(solution)[0])
