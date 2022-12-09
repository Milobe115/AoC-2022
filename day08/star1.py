from dataclasses import dataclass


@dataclass
class Tree:
    height: int
    visible: bool


def parse_map(lines):
    _map = []
    for line in lines:
        _map.append([Tree(height=int(x), visible=False) for x in line])
    return _map


with open("./input.txt", "r") as f:
    data = f.read().splitlines()
    tree_map = parse_map(data)

    for i in range(len(tree_map)):
        tree_map[i][0].visible = True
        tree_map[i][-1].visible = True
        threshold_direct = tree_map[i][0].height
        threshold_reverse = tree_map[i][-1].height
        for j in range(len(tree_map[i])):
            tree_map[0][j].visible = True
            tree_map[-1][j].visible = True
            if tree_map[i][j].height > threshold_direct:
                threshold_direct = tree_map[i][j].height
                tree_map[i][j].visible = True
            if tree_map[i][len(tree_map[i]) - j - 1].height > threshold_reverse:
                threshold_reverse = tree_map[i][len(tree_map[i]) - j - 1].height
                tree_map[i][len(tree_map[i]) - j - 1].visible = True

    for j in range(len(tree_map[0])):
        threshold_direct = tree_map[0][j].height
        threshold_reverse = tree_map[-1][j].height
        for i in range(len(tree_map)):
            if tree_map[i][j].height > threshold_direct:
                threshold_direct = tree_map[i][j].height
                tree_map[i][j].visible = True
            if tree_map[len(tree_map) - i - 1][j].height > threshold_reverse:
                threshold_reverse = tree_map[len(tree_map) - i - 1][j].height
                tree_map[len(tree_map) - i - 1][j].visible = True

    count = 0
    for line in tree_map:
        for tree in line:
            count += 1 if tree.visible else 0

    print(count)