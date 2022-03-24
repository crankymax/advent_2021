
from itertools import islice


window = [None,None,None]
last_window_sum = 9999
count = 0
line = 1
with(open('input.txt')) as depths:
    for depth in depths:
        if window[2] is None:
            window[line] = int(depth)
            line += 1
            print(window)
            continue
        else:
            window[0], window[1], window[2] = window[1], window[2], int(depth)

        print(window, sum(window), sum(window) > last_window_sum)

        if sum(window) > last_window_sum:
            count += 1
        last_window_sum = sum(window)

print(f'Count of greater {count}')