
horiz = 0
depth = 0
with(open('directions.txt')) as directions:
    for direction in directions:
        (way, size) = direction.split()
        if way == 'forward':
            horiz += int(size)
        elif way == 'back':
            horiz -= int(size)
        if way == 'down':
            depth += int(size)
        elif way == 'up':
            depth -= int(size)

    print(f'horiz {horiz} depth {depth} multi {horiz * depth}')

