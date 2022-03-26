from io import StringIO
from collections import defaultdict, Counter

test_data = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

# input_src = StringIO(test_data)
input_src = open('poly_grow.txt')

poly = input_src.readline().strip()
_ = input_src.readline()
pair_rules = {}

for rule in input_src:
    pair, element = rule.strip().split(' -> ')
    pair_rules[pair] = element

pair_counts = Counter()
for char in range(len(poly)-1):
    pair_counts[poly[char:char+2]] += 1

for steps in range(1, 41):
    step_counts = Counter()
    for pair in pair_counts:
        step_counts[pair[0] + pair_rules[pair]] += pair_counts[pair]
        step_counts[pair_rules[pair] + pair[1]] += pair_counts[pair]
    pair_counts = step_counts

element_count = Counter()
for pair in pair_counts:
    element_count[pair[1]] += pair_counts[pair]
element_count[poly[0]] += 1

print(f"Most common {element_count.most_common()[0]}, least common {element_count.most_common()[-1]}")
print(f"Difference {element_count.most_common()[0][1]-element_count.most_common()[-1][1]}")
