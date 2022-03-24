from io import StringIO
import numpy as np

test_data = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


input_src = open('vent_data.txt')
#input_src = StringIO(test_data)

flat_mat = np.zeros((1000,1000))
diagonal = True

with input_src as data:
    for data_line in data:
        vent_line = []
        start_point, end_point = data_line.strip().split(' -> ')
        vent_line.append(tuple(map(int, start_point.split(','))))
        vent_line.append(tuple(map(int, end_point.split(','))))
        x_step = -1 if vent_line[0][0] > vent_line[1][0] else 1
        y_step = -1 if vent_line[0][1] > vent_line[1][1] else 1
        x_list = list(range(vent_line[0][0], vent_line[1][0] + x_step, x_step))
        y_list = list(range(vent_line[0][1], vent_line[1][1] + y_step, y_step))
        if (vent_line[0][0] == vent_line[1][0]) or (vent_line[0][1] == vent_line[1][1]):
            for x in x_list:
                for y in y_list:
                    flat_mat[x][y] += 1
        elif diagonal:
            for x, y in zip(x_list, y_list):
                flat_mat[x][y] += 1

    print(len(np.where(flat_mat > 1)[0]))


