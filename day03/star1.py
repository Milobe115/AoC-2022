import string

f = open("./input.txt", "r")
lines = f.readlines()


def alpha_score(char):
    if char.isupper():
        return 27 + string.ascii_uppercase.index(char)
    else:
        return 1 + string.ascii_lowercase.index(char)

def process(line):
    line = line.strip()
    n = len(line)
    set1 = set(list(line[:n//2]))
    set2 = set(list(line[n//2:]))
    return sum(map(lambda x: alpha_score(x) ,set1.intersection(set2)))


print(sum(map(lambda x : process(x), lines)))
