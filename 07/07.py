with open("07.in") as f:

    def gauss(start, end):
        i = abs(start-end)
        return (i*(i+1))//2

    pos = [int(x) for x in f.read().strip().split(',')]
    d = []
    e = []
    for i in range(max(pos)):
        d.append(sum([abs(x-i) for x in pos]))
        e.append(sum([gauss(x, i) for x in pos]))
    print(min(d), min(e))