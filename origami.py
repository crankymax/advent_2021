from io import StringIO
import numpy as np

test_data = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

#input_src = StringIO(test_data)
input_src = open('origami_dots.txt')

x_list = []
y_list = []
line_folds = []
for loc_xy in input_src:
    loc_xy = loc_xy.strip()
    if len(loc_xy) == 0:
        continue
    elif loc_xy[0] == 'f':
        parts = loc_xy.split(' ')
        fold_dir, line_fold = parts[2].split('=')
        line_folds.append((fold_dir, int(line_fold)))
    else:
        lx, ly = map(int, loc_xy.strip().split(','))
        x_list.append(lx)
        y_list.append(ly)

print(max(y_list), max(x_list), line_folds)

paper_dots = np.zeros((895, 1311))
for dot_x, dot_y in zip(x_list, y_list):
    paper_dots[dot_y, dot_x] = 1

result_dots = paper_dots
for line_fold in line_folds:
    if line_fold[0] == 'y':
        result_dots = np.flip(result_dots[line_fold[1]+1:, :], 0) + result_dots[:line_fold[1], :]
    else:
        result_dots = np.flip(result_dots[:, line_fold[1]+1:], 1) + result_dots[:, :line_fold[1]]

print(f'Dots visible are {np.sum(result_dots>0)}')
print(result_dots)

