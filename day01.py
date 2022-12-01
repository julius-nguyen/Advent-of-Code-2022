calories = []

with open('day01input.txt', encoding='utf-8') as f:
    cals = 0

    for line in f.read().split('\n'):

        if line == '':
            calories.append(cals)
            cals = 0
            continue

        cals += int(line)

# elf that has the most calories
print(max(calories))

# sort calories dict in descending order
calories.sort(reverse=True)

# three elfs that have the most calories
print(calories[:3])
# sum of the calories of the three elfs that have the most calories
print(sum(calories[:3]))
