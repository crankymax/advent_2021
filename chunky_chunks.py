from io import StringIO

test_data = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

#input_src = StringIO(test_data)
input_src = open('chunky.txt')

openers = ["[", "(", "{", "<"]
closers = ["]", ")", "}", ">"]

chunk_partners = {x: y for (x, y) in zip(closers, openers)}


error_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
error_total = 0

remainder_scores = {'(': 1, '[': 2, '{': 3, '<': 4}
remainder_values = []

for chunk in input_src:
    chunk_stack = []
    for input_char in chunk.strip():

        if input_char in openers:
            chunk_stack.append(input_char)
        elif chunk_partners[input_char] == chunk_stack[-1]:
            chunk_stack.pop()
        else:
            error_total += error_scores[input_char]
            break
    else:
        remainder_total = 0
        for remainder in reversed(chunk_stack):
            remainder_total *= 5
            remainder_total += remainder_scores[remainder]
        remainder_values.append(remainder_total)

print(f'File complete error_total {error_total}')
in_order = sorted(remainder_values)
median = in_order[(len(in_order)//2)]
print(f'Median score is {median}')





