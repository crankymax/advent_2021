from io import StringIO


class LanternFish:
    def __init__(self, initial_age=8):
        self.age = initial_age

    def __repr__(self):
        return str(self.age)

    def new_day(self, school):
        self.age -= 1
        if self.age < 0:
            self.age = 6
            return LanternFish()
        else:
            return None


test_data = """3,4,3,1,2"""

input_src = open('lantern_fish.txt')
#input_src = StringIO(test_data)

first_fish = input_src.readline().split(',')
school = []

for starting_fish_age in first_fish:
    school.append(LanternFish(int(starting_fish_age)))

for each_day in range(256):
    print(each_day)
    # print(school)
    new_fish = []
    for fish in school:
        fry = fish.new_day(school)
        if fry is not None:
            new_fish.append(fry)
    school.extend(new_fish)

print(len(school))


