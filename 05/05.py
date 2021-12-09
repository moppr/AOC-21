with open("05.in") as f:
    lines = [','.join(x.strip().split(' -> ')) for x in f.readlines()]

    points = set()
    pointsdup = set()
    for line in lines:
        x1, y1, x2, y2 = [int(z) for z in line.split(',')]
        if x1 == x2:  # along y
            for i in range(min(y1, y2), max(y1, y2)+1):
                if (x1, i) in points:
                    pointsdup.add((x1, i))
                points.add((x1, i))
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2)+1):
                if (i, y1) in points:
                    pointsdup.add((i, y1))
                points.add((i, y1))
        else:  # diag
            d = abs(x1-x2)+1
            dx = 1 if x2 > x1 else -1
            dy = 1 if y2 > y1 else -1
            for i in range(d):
                co = (x1+i*dx, y1+i*dy)
                if co in points:
                    pointsdup.add(co)
                points.add(co)

    print(len(pointsdup))