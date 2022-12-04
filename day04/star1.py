import re

with open('./input.txt', "r") as f:
    cpt = 0
    lines = f.read().splitlines()
    regex = re.compile(r'^(\d+)-(\d+),(\d+)-(\d+)$')
    for line in lines:
        match = regex.match(line)
        x1, x2, y1, y2 = int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))
        if x1 <= y1 and x2 >= y2:
            print(f"{x1}, {x2} fully contains {y1}, {y2}")
            cpt += 1
        elif x1 >= y1 and x2 <= y2:
            print(f"{y1}, {y2} fully contains {x1}, {x2}")
            cpt += 1

    print(cpt)
