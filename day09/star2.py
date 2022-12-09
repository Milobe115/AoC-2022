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

    knots = [(0, 0) for _ in range(10)]

    tail_positions = set()

    for line in lines:
        if up.match(line):
            _distance = int(up.match(line).group(1))
            for i in range(_distance):
                knots[0] = (knots[0][0], knots[0][1] + 1)
                for i in range(1, len(knots)):
                    if distance(knots[i-1], knots[i]) > 1:
                        knots[i] = move_tail_to_head(knots[i], knots[i-1])
                tail_positions.add(knots[-1])

        if down.match(line):
            _distance = int(down.match(line).group(1))
            for i in range(_distance):
                knots[0] = (knots[0][0], knots[0][1] - 1)
                for i in range(1, len(knots)):
                    if distance(knots[i-1], knots[i]) > 1:
                        knots[i] = move_tail_to_head(knots[i], knots[i-1])
                tail_positions.add(knots[-1])

        if left.match(line):
            _distance = int(left.match(line).group(1))
            for i in range(_distance):
                knots[0] = (knots[0][0] - 1, knots[0][1])
                for i in range(1, len(knots)):
                    if distance(knots[i-1], knots[i]) > 1:
                        knots[i] = move_tail_to_head(knots[i], knots[i-1])
                tail_positions.add(knots[-1])

        if right.match(line):
            _distance = int(right.match(line).group(1))
            for i in range(_distance):
                knots[0] = (knots[0][0] + 1, knots[0][1])
                for i in range(1, len(knots)):
                    if distance(knots[i-1], knots[i]) > 1:
                        knots[i] = move_tail_to_head(knots[i], knots[i-1])
                tail_positions.add(knots[-1])

    print(len(tail_positions))
