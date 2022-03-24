
one_counts = [0] * 12
line_count = 0
with(open('gamma_eps.txt')) as raw_log:
    for log_line in raw_log:
        line_count += 1
        for pos, numeral in enumerate(log_line.strip()):
            if numeral == '1':
                one_counts[pos] += 1

print(one_counts, line_count)
eps_val = gamma_val = 0
for count in one_counts:
    gamma_val = gamma_val << 1
    eps_val = eps_val << 1
    print(int(count > 500))
    gamma_val = gamma_val | int(count >= 500)
    eps_val = eps_val | int(count < 500)

    print(f"{gamma_val}:{gamma_val:032b}, {eps_val}:{eps_val:032b}")

print(f"Power = {gamma_val * eps_val} {0xFFF&(~gamma_val)}")



