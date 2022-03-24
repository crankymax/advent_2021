from io import StringIO

import numpy as np

test_data = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

#input_src = StringIO(test_data)
input_src = open('octo_flashy.txt')


def add_flash(all_octopuses, processed, flasher):
    triggered = []
    if flasher[0] > 0:
        all_octopuses[flasher[0]-1][flasher[1]] += 1
        if all_octopuses[flasher[0]-1][flasher[1]] > 9:
            triggered.append([flasher[0]-1, flasher[1]])

    if flasher[0] < all_octopuses.shape[0]-1:
        all_octopuses[flasher[0]+1][flasher[1]] += 1
        if all_octopuses[flasher[0]+1][flasher[1]] > 9:
            triggered.append([flasher[0]+1, flasher[1]])

    if flasher[1] > 0:
        all_octopuses[flasher[0]][flasher[1]-1] += 1
        if all_octopuses[flasher[0]][flasher[1]-1] > 9:
            triggered.append([flasher[0], flasher[1]-1])

    if flasher[1] < all_octopuses.shape[1]-1:
        all_octopuses[flasher[0]][flasher[1]+1] += 1
        if all_octopuses[flasher[0]][flasher[1]+1] > 9:
            triggered.append([flasher[0], flasher[1]+1])

    if flasher[0] > 0 and flasher[1] > 0:
        all_octopuses[flasher[0]-1][flasher[1]-1] += 1
        if all_octopuses[flasher[0]-1][flasher[1]-1] > 9:
            triggered.append([flasher[0]-1, flasher[1]-1])

    if flasher[0] > 0 and flasher[1] < all_octopuses.shape[1]-1:
        all_octopuses[flasher[0]-1][flasher[1]+1] += 1
        if all_octopuses[flasher[0]-1][flasher[1]+1] > 9:
            triggered.append([flasher[0]-1, flasher[1]+1])

    if flasher[0] < all_octopuses.shape[0]-1 and flasher[1] > 0:
        all_octopuses[flasher[0]+1][flasher[1]-1] += 1
        if all_octopuses[flasher[0]+1][flasher[1]-1] > 9:
            triggered.append([flasher[0]+1, flasher[1]-1])

    if flasher[0] < all_octopuses.shape[0]-1 and flasher[1] < all_octopuses.shape[1]-1:
        all_octopuses[flasher[0]+1][flasher[1]+1] += 1
        if all_octopuses[flasher[0]+1][flasher[1]+1] > 9:
            triggered.append([flasher[0]+1, flasher[1]+1])

    for new_flash in triggered:
        if new_flash not in processed:
            processed.append(new_flash)
            add_flash(all_octopuses, processed, new_flash)


octopus_location_list = []
for octopus_location_row in input_src:
    octopus_location_list.append([int(x) for x in octopus_location_row.strip()])

# Create array
octopus_locations = np.array(octopus_location_list)
print(f"octopus locations {octopus_locations.shape}")
total_flashes = 0

for run_id in range(1000):
    octopus_locations = np.add(octopus_locations, 1)
    flashing_octopuses = np.argwhere(octopus_locations > 9).tolist()
    all_processed = []
    for flashing_octopus in flashing_octopuses:
        if flashing_octopus not in all_processed:
            all_processed.append(flashing_octopus)
            add_flash(octopus_locations, all_processed, flashing_octopus)

    flashers = list(zip(*np.argwhere(octopus_locations > 9)))
    number_flashing = len(flashers[0]) if len(flashers) > 0 else 0
    # print(f"Number flashing {number_flashing}")
    if number_flashing == octopus_locations.size:
        print(f"All flashed at step {run_id+1}")

    if number_flashing > 0:
        total_flashes += number_flashing
        octopus_locations[flashers[0], flashers[1]] = 0

print(f"Completed {run_id+1} steps total flashes {total_flashes}")