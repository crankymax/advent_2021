from io import StringIO
from collections import defaultdict, Counter


def search_path(all_caves, current_path, path_cave, complete_paths):
    if path_cave == 'end':
        current_path.append(path_cave)
        complete_paths.append(current_path)
    elif path_cave == 'start':
        return
    elif path_cave.isupper() or current_path.count(path_cave) == 0 or not two_small_cave_visits(current_path):
        current_path.append(path_cave)
        next_caves = all_caves[path_cave]
        for new_cave in next_caves:
            search_path(all_caves, current_path.copy(), new_cave, complete_paths)


def two_small_cave_visits(check_path):
    check_counts = Counter(check_path)
    for cave_check, entries_check in check_counts.items():
        if cave_check.islower() and entries_check > 1:
            return True

    return False


test_data_s = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

test_data_m = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

test_data_l ="""fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

#input_src = StringIO(test_data_m)
input_src = open('map_caves.txt')

cave_dict = defaultdict(list)

for caves in input_src:
    cave_1, cave_2 = caves.strip().split('-')
    cave_dict[cave_1].append(cave_2)
    if cave_1 != 'start':
        cave_dict[cave_2].append(cave_1)

completed_paths = []
for cave in cave_dict['start']:
    path = ['start']
    search_path(cave_dict, path.copy(), cave, completed_paths)

print(f'Completed paths {len(completed_paths)}')

one_small_cave = 0
for path in completed_paths:
    cave_counts = Counter(path)
    for cave, entries in cave_counts.items():
        if cave.islower() and entries > 1:
            break
    else:
        one_small_cave += 1

print(f'Paths with one small cave visit ={one_small_cave}')