import ast

# Read graph from file
with open("GraphFile.txt") as BFS:
    graph = ast.literal_eval(BFS.read())

# List for visited nodes.
visited = []

# Initialize a queue
queue = []

# function for BFS
def bfs(graph, node):

    visited.append(node)

    queue.append(node)

    # Creating loop to visit each node
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

print("BFS : ",end="")

bfs(graph, '5')
