with open("09.in") as f:
    grid = [[int(x) for x in line.strip()] for line in f.readlines()]
    maxlen = len(grid[0])-1
    maxhei = len(grid)-1
    lows = 0
    rls = 0
    points = []
    for i,row in enumerate(grid):
        for j,num in enumerate(row):
            lp = True
            try:
                lp = lp and grid[i-1][j] > num
            except:
                pass
            try:
                lp = lp and grid[i+1][j] > num
            except:
                pass
            try:
                lp = lp and grid[i][j-1] > num
            except:
                pass
            try:
                lp = lp and grid[i][j+1] > num
            except:
                pass
            if lp:
                points.append([i, j])
                lows += 1
                rls += num + 1
    basin_sizes = []
    for point in points:
        bad = []
        explored = []
        fringe = [point]
        while fringe:
            p = fringe.pop(0)
            explored.append(p)
            i,j = p
            p2s = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
            for p2 in p2s:
                a,b = p2
                if a < 0 or a > maxhei or b < 0 or b > maxlen:
                    continue
                #print(a, b)
                if grid[a][b] == 9:
                    bad.append(p2)
                    continue
                if p2 not in bad and p2 not in explored and p2 not in fringe:
                    fringe.append(p2)
        basin_sizes.append(len(explored))
    top3 = sorted(basin_sizes)[-3:]
    print(top3[0]*top3[1]*top3[2])
    #print(rls)