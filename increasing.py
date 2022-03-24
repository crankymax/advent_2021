
last_depth = 999999
count = 0
with(open('input.txt')) as depths:
    for depth in depths:
        if int(depth) > last_depth:
            count += 1
        last_depth = int(depth)

print(f'Count of greater {count}')