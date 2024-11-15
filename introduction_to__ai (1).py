# -*- coding: utf-8 -*-
"""INTRODUCTION_TO _AI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZZ32LcUeYCoVhVIEn4bnPhUsycoI6blE

**Vaccum Problem**
"""

def main():
    rooms = {'a': 0, 'b': 0}
    cost = 0
    for room in rooms:
        rooms[room] = int(input("Enter the status (1 for available, 0 for not available): "))

    for i in rooms:
        if rooms[i] == 1:
            print(f"Room {i} is available")
            rooms[i] = 0
            cost += 1
        else:
            print(f"Room {i} is not available")

    print("Total cost is", cost)

main()

"""**BREADTH FIRST SEARCH**"""

vistied = []
queue = []

def bfs(graph, start_node, goal_node):
    vistied.append(start_node)
    queue.append(start_node)
    while queue:
        node = queue.pop(0)
        for neighbour in graph[node]:
            if neighbour not in vistied:
                if node == goal_node:
                    print("Goal node found")
                    return vistied
                else:
                    print("Goal node not found")
                    vistied.append(neighbour)
                    queue.append(neighbour)
                    cost = len(vistied)
    return vistied

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

A = bfs(graph, start_node, goal_node)
print(A)

"""**DFS**"""

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

"""**BEST FS**"""

SuccList = {
    'Kochi': [['Thrissur', 200], ['Kottayam', 80], ['Alappuzha', 90]],
    'Thrissur': [['Palakkad', 110], ['Kochi', 200], ['Malappuram', 170], ['Guruvayur', 45]],
    'Palakkad': [['Thrissur', 110], ['Kozhikode', 150]],
    'Kozhikode': [['Kannur', 90], ['Palakkad', 150], ['Kasargod', 300]],
    'Kottayam': [['Kochi', 80], ['Idukki', 160]],
    'Alappuzha': [['Kochi', 90], ['Pathanamthitta', 130]],
    'Kannur': [['Kozhikode', 90], ['Kasargod', 100]]
}
Start = 'Kochi'
Goal = 'Kasargod'
Explored = []
SUCCESS = True
FAILURE = False
State = FAILURE
def GENCHILD(N):
    if N in SuccList.keys():
        return SuccList[N]
    return []
def GOALTEST(N):
    return N == Goal
def APPEND(L1, L2):
    return list(L1) + list(L2)
def SORT(L):
    L.sort(key=lambda x: x[1])
    return L
def BestFirstSearch():
    Frontier = [[Start, 0]]
    global State
    global Explored
    while Frontier and State != SUCCESS:
        print("\nCurrent Frontier:", Frontier)
        SORT(Frontier)
        N = Frontier.pop(0)
        print("N =", N)
        if GOALTEST(N[0]):
            State = SUCCESS
            Explored = APPEND(Explored, [N])
            print("EXPLORED =", Explored)
        else:
            Explored = APPEND(Explored, [N])
            print("EXPLORED =", Explored)

            CHILD = GENCHILD(N[0])
            print("CHILD =", CHILD)

            CHILD = [child for child in CHILD if child[0] not in [exp[0] for exp in Explored]]
            CHILD = [child for child in CHILD if child not in Frontier]

            Frontier = APPEND(Frontier, CHILD)

            print("Unsorted Frontier =", Frontier)

    return State

result = BestFirstSearch()
print("Explored nodes:", Explored, "Result:", result)

"""**A* Algorithm(8_PUZZLE)**"""

import numpy as np
from copy import deepcopy

def star_loop(step, idx1, idx2, closed):
    val = []
    swapped = []
    ind_list = []
    for i in range(idx1 - 1, idx1 + 2):
        for j in range(idx2 - 1, idx2 + 2):
            if [i, j] != closed and i >= 0 and j >= 0 and i <= 2 and j <= 2:
                if [i, j] != [idx1, idx2] and abs(i - idx1) != abs(j - idx2):
                    step2 = deepcopy(step)
                    step2[idx1, idx2], step2[i, j] = step2[i, j], step2[idx1, idx2]
                    swapped.append(step2)
                    ind_list.append([i, j])
    return swapped, ind_list

initial = np.array([[2, 8, 3],
                    [1, 6, 4],
                    [7, 0, 5]])

step = deepcopy(initial)
final = np.array([[1, 2, 3],
                  [8, 0, 4],
                  [7, 6, 5]])

init = np.where(initial == 0)
idx1 = int(init[0])
idx2 = int(init[1])

g = 1
closed = [idx1, idx2]

while g < 10:
    print("Current position of 0:", idx1, idx2)
    swapped, ind_list = star_loop(step, idx1, idx2, closed)
    closed = [idx1, idx2]

    h_list = []
    for k in range(len(swapped)):
        h = len(np.where(swapped[k] != final)[0])
        h_list.append(g + h)

    print("Heuristic list:", h_list)

    if h_list:
        min_index = h_list.index(min(h_list))
        step = swapped[min_index]
        idx1 = ind_list[min_index][0]
        idx2 = ind_list[min_index][1]

        print("Next step:\n", step, "\nClosed:", closed)

        if (step == final).all():
            print("Reached final state!")
            break

    g += 1

"""**BACKTRACKING**"""

domain_colors = ['Red', 'Blue', 'Green']
variable_states = ['wa', 'nt', 'sa', 'q', 'nsw', 'v', 't']
neighbors = {
    'wa': ['nt', 'sa'],
    'nt': ['wa', 'sa', 'q'],
    'sa': ['wa', 'nt', 'q', 'nsw', 'v'],
    'q': ['nt', 'sa', 'nsw'],
    'nsw': ['q', 'sa', 'v'],
    'v': ['sa', 'nsw'],
    't': []
}
finalstateswithcolor = {}
def getthecolor(state):
    for color in domain_colors:
        if assigncolor(state, color):
            return color
def assigncolor(state, color):
    for neighbor in neighbors.get(state, []):
        color_of_neighbor = finalstateswithcolor.get(neighbor)
        if color_of_neighbor == color:
            return False
    return True
def main():
    sorted_states = sorted(neighbors.keys(), key=lambda state: len(neighbors[state]), reverse=True)
    for state in sorted_states:
        finalstateswithcolor[state] = getthecolor(state)
    print("The states with colors are:", finalstateswithcolor)
main()

"""### LOCAL SEARCH GRAPH COLORING

"""

def isSafe(graph, color):
    for i in range(4):
        for j in range(i + 1, 4):
            if graph[i][j] == 1 and color[i] == color[j]:
                return False
    return True
def graphColoring(graph, m, i, color):
    if i == 4:
        if isSafe(graph, color):
            printSolution(color)
            return True
        return False
    for j in range(1, m + 1):
        color[i] = j
        if graphColoring(graph, m, i + 1, color):
            return True
        color[i] = 0
    return False
def printSolution(color):
    print("Solution Exists: Following are the assigned colors:")
    for i in range(4):
        print(color[i], end=" ")
    print()
if __name__ == "__main__":
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    m = 3
    color = [0 for i in range(4)]
    if not graphColoring(graph, m, 0, color):
        print("Solution does not exist.")

"""**KNOWLEDGE REPRESENTATION**"""

def measles(a, b, c, d, e):
    if a == 'y' and b == 'y' and c == 'y' and d == 'y' and e == 'y':
        return "measles"
    else:
        return None

def flu(a, b, c, d, e, f, g, h):
    if a == 'y' and b == 'y' and c == 'y' and d == 'y' and e == 'y' and f == 'y' and g == 'y' and h == 'y':
        return "flu"
    else:
        return None

def cold(c, j, k, d, h):
    if c == 'y' and j == 'y' and k == 'y' and d == 'y' and h == 'y':
        return "cold"
    else:
        return None

def chickenpox(a, h, g, b):
    if a == 'y' and h == 'y' and g == 'y' and b == 'y':
        return "chickenpox"
    else:
        return None

def run_diagnosis():
    name = input("Please enter your name: ")
    a = input("Do you have fever? (y/n): ").lower()
    b = input("Do you have rashes? (y/n): ").lower()
    c = input("Do you have headache? (y/n): ").lower()
    d = input("Do you have running nose? (y/n): ").lower()
    e = input("Do you have conjunctivitis? (y/n): ").lower()
    f = input("Do you have cough? (y/n): ").lower()
    g = input("Do you have ache? (y/n): ").lower()
    h = input("Do you have chills? (y/n): ").lower()
    i = input("Do you have swollen glands? (y/n): ").lower()
    j = input("Do you have sneezing? (y/n): ").lower()
    k = input("Do you have sore throat? (y/n): ").lower()

    diagnosis = []

    result = measles(a, f, e, d, b)
    if result:
        diagnosis.append(result)

    result = flu(a, c, g, e, h, k, f, d)
    if result:
        diagnosis.append(result)

    result = cold(c, j, k, d, h)
    if result:
        diagnosis.append(result)

    result = chickenpox(a, h, g, b)
    if result:
        diagnosis.append(result)

    if len(diagnosis) > 0:
        print(f"{name}, based on the symptoms provided, you may have: {', '.join(diagnosis)}.")
    else:
        print("No diagnosis could be made based on the given symptoms.")

run_diagnosis()

"""**TRAVELLING SALES MAN PROBLEM**"""

from sys import maxsize
from itertools import permutations
V = 4
graph = [[0, 10, 15, 20],
         [10, 0, 35, 25],
         [15, 35, 0, 30],
         [20, 25, 30, 0]]
s = 0
def travellingSalesmanProblem(graph, s):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
    min_path = maxsize
    best_tour = None
    next_permutation = permutations(vertex)
    for perm in next_permutation:
        current_pathweight = 0
        k = s
        for j in perm:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
        if current_pathweight < min_path:
            min_path = current_pathweight
            best_tour = [s] + list(perm) + [s]
    return min_path, best_tour
min_path, best_tour = travellingSalesmanProblem(graph, s)
print('min_path =', min_path)
print('best_tour =', best_tour)