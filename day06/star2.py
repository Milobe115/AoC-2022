with open("./input.txt", 'r') as f:
    data = f.read().splitlines()[0]

    cpt = 0
    while len(set(data[cpt:cpt+14])) != 14:
        cpt += 1

    print(cpt + 14)