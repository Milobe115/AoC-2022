def parse_map(lines):
    _map = []
    for line in lines:
        _map.append([int(x) for x in line])
    return _map


with open("./input.txt", "r") as f:
    data = f.read().splitlines()
    tree_map = parse_map(data)

    max_score = 0

    for i in range(len(tree_map)):
        for j in range(len(tree_map[i])):
            k = i - 1
            while k >= 0 and tree_map[k][j] < tree_map[i][j]:
                k -= 1
            left = abs(i - max(k, 0))
            k = i + 1
            while k < len(tree_map[i]) and tree_map[k][j] < tree_map[i][j]:
                k += 1
            right = abs(i - min(k, len(tree_map) - 1))
            k = j - 1
            while k >= 0 and tree_map[i][k] < tree_map[i][j]:
                k -= 1
            up = abs(j - max(k, 0))
            k = j + 1
            while k < len(tree_map) and tree_map[i][k] < tree_map[i][j]:
                k += 1
            down = abs(j - min(k, len(tree_map) - 1))
            max_score = max(max_score, left * right * up * down)

    print(max_score)
