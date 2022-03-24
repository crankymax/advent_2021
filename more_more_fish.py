from io import StringIO


test_data = """3,4,3,1,2"""

input_src = open('lantern_fish.txt')
# input_src = StringIO(test_data)

first_fish = input_src.readline().split(',')
ages = [0] * 9

for starting_fish_age in first_fish:
    ages[int(starting_fish_age)] += 1

for each_day in range(256):
    print(each_day)
    generation = [0] * 9
    for age in range(9):
        if age == 0:
            generation[8] = ages[0]
            generation[6] = ages[0]
        else:
            generation[age-1] += ages[age]
    print(generation)
    ages = generation


print(sum(ages))


