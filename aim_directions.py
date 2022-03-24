
horiz = 0
depth = 0
aim = 0
with(open('directions.txt')) as directions:
    for direction in directions:
        (way, size) = direction.split()
        if way == 'forward':
            horiz += int(size)
            depth += int(size) * aim
        elif way == 'back':
            horiz -= int(size)
            depth += int(size) * aim
        if way == 'down':
            aim += int(size)
        elif way == 'up':
            aim -= int(size)

    print(f'horiz {horiz} depth {depth} multi {horiz * depth}')

