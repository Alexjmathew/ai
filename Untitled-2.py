def dfs(visit, graph, start, goal):
    flag = 0
    visit.append(start)
    stack.append(start)
    while stack:
        m = stack.pop()  # pop the last element (LIFO)
        for neighbour in graph[m]:
            if flag == 0:
                if neighbour not in visit:
                    visit.append(neighbour)
                    stack.append(neighbour)
                    print(f"VISITED: {visit}")

                    if neighbour == goal:
                        print("GOAL REACHED")
                        print(f"THE PATH TAKEN IS {visit}")
                        flag = 1
    if flag == 0:
        print("GOAL IS NOT REACHED")
                    
goal_node = input("Enter the goal node: ")

stack = [] 
visit = []
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['A', 'B']
}

print("DFS DEPTH FIRST SEARCH ALGORITHM")

print("Author ALEX J MATHEW")

dfs(visit, graph, 'A', goal_node)
