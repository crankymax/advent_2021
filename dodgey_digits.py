from io import StringIO
from typing import Set, Any

import numpy as np
simple_test_data = """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"""

test_data = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

input_src = open('dodgey_digits.txt')
# input_src = StringIO(test_data)
# input_src = StringIO(simple_test_data)

segment_numbers = {'abcefg': '0', 'cf': '1', 'acdeg': '2',
                   'acdfg': '3', 'bcdf': '4', 'abdfg': '5',
                   'abdefg': '6', 'acf': '7', 'abcdefg': '8',
                   'abcdfg': '9'}

segment_len_map = {2: [1], 3: [7], 4: [4], 5: [2, 3, 5], 6: [0, 6, 9], 7: [8]}

digit_count = 0

segment_map = {'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '', 'g': ''}

for raw_wire_segments in input_src:
    all_digits_line, output_digits = raw_wire_segments.split(' | ')
    output_list = output_digits.strip().split(' ')
    all_digits = all_digits_line.strip().split(' ')
    five_list = []
    six_list = []
    for candidate_digit in all_digits:
        if len(candidate_digit) == 2:
            one_segments: set[Any] = set(candidate_digit)
        elif len(candidate_digit) == 4:
            four_segments = set(candidate_digit)
        elif len(candidate_digit) == 3:
            seven_segments = set(candidate_digit)
        elif len(candidate_digit) == 7:
            eight_segments = set(candidate_digit)
        elif len(candidate_digit) == 5:
            five_list.append(set(candidate_digit))
        elif len(candidate_digit) == 6:
            six_list.append(set(candidate_digit))
    print(f'First 1={one_segments}, 4={four_segments}, 7={seven_segments}')
    segment_map['a'] = (seven_segments - one_segments).pop()
    bd_candidates = four_segments - one_segments
    print(f'Assign a = {segment_map["a"]} cf = {one_segments} bd = {bd_candidates}')
    for digit in five_list:
        if len(one_segments.difference(digit)) == 0:
            three_segments = digit
            print(f'three {three_segments}')
            break

    five_list.remove(three_segments)
    segment_map['d'] = bd_candidates.intersection(three_segments).pop()
    segment_map['b'] = bd_candidates.difference(segment_map['d']).pop()

    if segment_map['b'] in five_list[0]:
        five_segments = five_list[0]
        two_segments = five_list[1]
    else:
        five_segments = five_list[1]
        two_segments = five_list[0]

    segment_map['c'] = two_segments.intersection(one_segments).pop()
    segment_map['f'] = one_segments.difference(segment_map['c']).pop()

    for digit in six_list:
        if segment_map['d'] not in digit:
            print(f'zero {digit}')
            segment_map['e'] = (digit-five_segments-one_segments).pop()
            segment_map['g'] = (digit - seven_segments).difference(segment_map['e']).difference(segment_map['b']).pop()

    decode_segment = dict()

    for k, v in segment_map.items():
        decode_segment[v] = k

    final_number = []
    for output_digit in output_list:
        number = sorted(list(map(lambda x: decode_segment[x], output_digit)))
        final_number.append(segment_numbers["".join(number)])

    print(f'output_digit {"".join(final_number)}')
    digit_count += int("".join(final_number))


print(digit_count)