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
    swapped, indlist = star_loop(step, idx1, idx2, closed)
    closed = [idx1, idx2]
    h_list = []

    for k in range(len(swapped)):
        h = len(np.where(swapped[k] != final)[0])
        h_list.append(g + h)

    if h_list:
        step = swapped[h_list.index(min(h_list))]
        idx1 = indlist[h_list.index(min(h_list))][0]
        idx2 = indlist[h_list.index(min(h_list))][1]

    print(f"Step {g}:\n", step, "\nClosed:", closed)

    if (step == final).all():
        print("Reached the final state.")
        break

    g += 1

if g == 10:
    print("Did not reach the final state within 10 steps.")
