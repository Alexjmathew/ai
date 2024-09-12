def isSafe(graph, v, color, c):
    for i in range(4):
        if graph[v][i] and color[i] == c:
            return False
    return True

def graphColoring(graph, m, i, color):
    if i == 4:
        return True

    for j in range(1, m + 1):
        if isSafe(graph, i, color, j):
            color[i] = j
            if graphColoring(graph, m, i + 1, color):
                return True
            color[i] = 0
    return False

def printSolution(color):
    print("Solution Exists: Following are the assigned colors")
    for i in range(4):
        print(color[i], end=" ")
    print()

if __name__ == '__main__':
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0],
    ]
    m = 3
    color = [0 for i in range(4)]

    if graphColoring(graph, m, 0, color):
        printSolution(color)
    else:
        print("Solution does not exist")
