f = open(".\input.txt", "r")
lines = f.readlines()
values = []
inner_values = []

for line in lines:
    if len(line.strip()) > 0:
        inner_values.append(int(line.strip()))
    else:
        values.append(inner_values)
        inner_values = []

caloriesByElf = list(map(sum, values))
topCalories = []
for i in range(3):
    topCalories.append(max(caloriesByElf))
    caloriesByElf.remove(max(caloriesByElf))

print(sum(topCalories))
