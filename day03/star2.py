import string

f = open("./input.txt", "r")
lines = f.readlines()
group_size = 3
groups = [lines[n:n+group_size] for n in range(0, len(lines), group_size)]


def alpha_score(char):
    if char.isupper():
        return 27 + string.ascii_uppercase.index(char)
    else:
        return 1 + string.ascii_lowercase.index(char)

def process(group):
    set1 = set(list(group[0].strip()))
    set2 = set(list(group[1].strip()))
    set3 = set(list(group[2].strip()))
    return sum(map(lambda x: alpha_score(x) ,set1.intersection(set2).intersection(set3)))


print(sum(map(lambda x : process(x), groups)))
