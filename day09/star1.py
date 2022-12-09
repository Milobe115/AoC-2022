import re


def distance(p1, p2):
    return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))


def move_tail_to_head(tail, head):
    # Axiswise moves
    if tail[0] == head[0] and tail[1] > head[1]:
        return tail[0], tail[1] - 1
    if tail[0] == head[0] and tail[1] < head[1]:
        return tail[0], tail[1] + 1
    if tail[1] == head[1] and tail[0] > head[0]:
        return tail[0] - 1, tail[1]
    if tail[1] == head[1] and tail[0] < head[0]:
        return tail[0] + 1, tail[1]

    #Diagonal moves
    if tail[0] > head[0] and tail[1] > head[1]:
        return tail[0] - 1, tail[1] - 1
    if tail[0] > head[0] and tail[1] < head[1]:
        return tail[0] - 1, tail[1] + 1
    if tail[0] < head[0] and tail[1] > head[1]:
        return tail[0] + 1, tail[1] - 1
    if tail[0] < head[0] and tail[1] < head[1]:
        return tail[0] + 1, tail[1] + 1


with open("input.txt") as f:
    lines = f.read().splitlines()

    up = re.compile(r"^U (\d+)$")
    down = re.compile(r"^D (\d+)$")
    left = re.compile(r"^L (\d+)$")
    right = re.compile(r"^R (\d+)$")

    head = (0, 0)
    tail = (0, 0)

    tail_positions = set()

    for line in lines:
        if up.match(line):
            _distance = int(up.match(line).group(1))
            for i in range(_distance):
                head = (head[0], head[1] + 1)
                if distance(head, tail) > 1:
                    tail = move_tail_to_head(tail, head)
                tail_positions.add(tail)

        if down.match(line):
            _distance = int(down.match(line).group(1))
            for i in range(_distance):
                head = (head[0], head[1] - 1)
                if distance(head, tail) > 1:
                    tail = move_tail_to_head(tail, head)
                tail_positions.add(tail)

        if left.match(line):
            _distance = int(left.match(line).group(1))
            for i in range(_distance):
                head = (head[0] - 1, head[1])
                if distance(head, tail) > 1:
                    tail = move_tail_to_head(tail, head)
                tail_positions.add(tail)

        if right.match(line):
            _distance = int(right.match(line).group(1))
            for i in range(_distance):
                head = (head[0] + 1, head[1])
                if distance(head, tail) > 1:
                    tail = move_tail_to_head(tail, head)
                tail_positions.add(tail)

    print(len(tail_positions))
