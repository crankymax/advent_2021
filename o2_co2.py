
test_lines = ['00100',
'11110',
'10110',
'10111',
'10101',
'01111',
'00111',
'11100',
'10000',
'11001',
'00010',
'01010']

def more_ones(one_lines, pos):
    one_count = 0
    for one_line in one_lines:
        one_count += 1 if one_line[pos] == '1' else 0
    #print(f'one_count={one_count} lines={len(one_lines)}')
    return one_count >= len(one_lines)/2


def list_val_positions(all_lines, val, pos):
    list_positions = []
    for line_number, line in enumerate(all_lines):
        if line[pos] == val:
            list_positions.append(line_number)
    return list_positions


log_lines = []
with(open('gamma_eps.txt')) as raw_log:
    for log_line in raw_log:
        log_lines.append(log_line.strip())

#log_lines = test_lines
# find O2
flag = '1' if more_ones(log_lines, 0) else '0'
flagged_positions = list_val_positions(log_lines, flag, 0)
flagged_values = log_lines
pos = 0
while len(flagged_positions) > 1:
    flagged_values = [flagged_values[x] for x in flagged_positions]
    pos += 1
    if pos > 11:
        break

    flag = '1' if more_ones(flagged_values, pos) else '0'
    flagged_positions = list_val_positions(flagged_values, flag, pos)

O2 = int(flagged_values[flagged_positions[0]], 2)

# find CO2
flag = '0' if more_ones(log_lines, 0) else '1'
flagged_positions = list_val_positions(log_lines, flag, 0)
flagged_values = log_lines
pos = 0
while len(flagged_positions) > 1:
    flagged_values = [flagged_values[x] for x in flagged_positions]
    pos += 1
    if pos > 11:
        break

    flag = '0' if more_ones(flagged_values, pos) else '1'
    flagged_positions = list_val_positions(flagged_values, flag, pos)
CO2 = int(flagged_values[flagged_positions[0]], 2)

print(f"Final values O2={O2} CO2={CO2} life_support={O2*CO2}")






