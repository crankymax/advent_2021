from io import StringIO
import numpy as np

test_data = """16,1,2,0,4,2,7,1,2,14"""

input_src = open('crab_pos.txt')
#input_src = StringIO(test_data)

crab_pos_input = list(map(int, input_src.readline().split(',')))
pos_count = np.zeros(max(crab_pos_input)+1)

for crab in list(crab_pos_input):
    pos_count[crab] += 1

fuel_cost = np.zeros(pos_count.shape)

for target_pos in range(pos_count.shape[0]):
    for eval_cost in range(pos_count.shape[0]):
        fuel_cost[target_pos] += pos_count[eval_cost]*sum(range(abs(target_pos-eval_cost)+1))

print(f'Position {np.argmin(fuel_cost)} fuel cost {fuel_cost[np.argmin(fuel_cost)]}')


