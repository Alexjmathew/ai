def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Initialize an empty set to keep track of visited nodes

    # Mark the current node as visited
    visited.add(start)
    print(start)  # Process the current node (e.g., print it)

    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited_nodes = dfs(graph, 'A')
