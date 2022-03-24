from io import StringIO
from functools import reduce
import numpy as np

test_data = """2199943210
3987894921
9856789892
8767896789
9899965678"""

input_src = open('smoke_levels.txt')
# input_src = StringIO(test_data)

lava_level_list = []
for lava_low_row in input_src:
    lava_level_list.append([int(x) for x in lava_low_row.strip()])

# Create array
smoke_levels = np.asarray(lava_level_list)
x_max = smoke_levels.shape[0]
y_max = smoke_levels.shape[1]

top_three = [0.0, 0.0, 0.0]

for x_arg in range(x_max):
    for y_arg in range(y_max):
        # print(x_arg, y_arg)
        bigger = 0
        if (x_arg-1) < 0 or (smoke_levels[x_arg, y_arg] < smoke_levels[x_arg-1, y_arg]):
            bigger += 1

        if (x_arg+1) >= x_max or (smoke_levels[x_arg, y_arg] < smoke_levels[x_arg+1, y_arg]):
            bigger += 1

        if (y_arg-1) < 0 or (smoke_levels[x_arg, y_arg] < smoke_levels[x_arg, y_arg-1]):
            bigger += 1

        if (y_arg+1) >= y_max or (smoke_levels[x_arg, y_arg] < smoke_levels[x_arg, y_arg+1]):
            bigger += 1

        if bigger == 4:
            print(f'Chicken dinner {x_arg}, {y_arg} {smoke_levels[x_arg,y_arg]}')
            basin_list = []
            check_list = [(x_arg, y_arg)]
            while len(check_list) > 0:
                check_point = check_list.pop()
                if smoke_levels[check_point] < 9 and check_point not in basin_list:
                    basin_list.append(check_point)
                if check_point[0]-1 >= 0 and smoke_levels[check_point[0]-1, check_point[1]] < 9:
                    if (check_point[0]-1, check_point[1]) not in basin_list:
                        basin_list.append((check_point[0]-1, check_point[1]))
                        check_list.append((check_point[0]-1, check_point[1]))
                if check_point[0]+1 < x_max and smoke_levels[check_point[0]+1, check_point[1]] < 9:
                    if (check_point[0]+1, check_point[1]) not in basin_list:
                        basin_list.append((check_point[0]+1, check_point[1]))
                        check_list.append((check_point[0]+1, check_point[1]))
                if check_point[1]-1 >= 0 and smoke_levels[check_point[0], check_point[1]-1] < 9:
                    if (check_point[0], check_point[1]-1) not in basin_list:
                        basin_list.append((check_point[0], check_point[1]-1))
                        check_list.append((check_point[0], check_point[1]-1))
                if check_point[1]+1 < y_max and smoke_levels[check_point[0], check_point[1]+1] < 9:
                    if (check_point[0], check_point[1]+1) not in basin_list:
                        basin_list.append((check_point[0], check_point[1]+1))
                        check_list.append((check_point[0], check_point[1]+1))

            basin_size = len(basin_list)
            print(f'Basin mapped length {basin_size} ')
            if basin_size > min(top_three):
                old_min = top_three.index(min(top_three))
                top_three[old_min] = basin_size

print(f'Cumulative risk is {reduce(lambda x,y: x*y, top_three, 1)}')

