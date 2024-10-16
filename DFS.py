graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    if start == goal:
        print("Goal is reached!")
        print("The path taken to reach the goal is:", visited)
        return True
    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited):
                return True
    return False

print("Depth-First Search")
if not dfs(graph, '5', '7'):
    print("Goal has not been reached")
