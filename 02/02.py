with open("02.in") as f:
    stuff = [(x.split()[0], int(x.split()[1])) for x in f.readlines()]
    horiz = 0
    depth = 0
    for i in stuff:
        dir, val = i
        if dir == "down":
            depth += val
        elif dir == "up":
            depth -= val
        elif dir == "forward":
            horiz += val
    print(horiz*depth)

    aim = 0
    horiz = 0
    depth = 0
    for i in stuff:
        dir, val = i
        if dir == "down":
            aim += val
        elif dir == "up":
            aim -= val
        elif dir == "forward":
            horiz += val
            depth += val*aim
    print(horiz*depth)
