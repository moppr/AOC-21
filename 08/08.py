with open("08.in") as f:
    #c = 0
    total = 0
    for line in f.readlines():
        a, b = line.strip().split('|')
        a = a.split()
        b = b.split()
        # for n in b:
        #     if len(n) in [2, 3, 4, 7]:  # one, seven, four, eight
        #         c += 1

        # find 1/7/4/8
        for item in a:
            if len(item) == 2:
                one = item
            elif len(item) == 3:
                seven = item
            elif len(item) == 4:
                four = item
            elif len(item) == 7:
                eight = item
        # 7-1 gives a
        real_a = set(seven).difference(set(one)).pop()
        # find 3 from 1
        for item in a:
            if len(item) == 5:
                if one[0] in item and one[1] in item:
                    three = item
        # find 9 from 3
        for item in a:
            if len(item) == 6:
                if all([ch in item for ch in three]):
                    nine = item
        # 9-3 gives b
        real_b = set(nine).difference(set(three)).pop()
        # 4-1-b gives d
        real_d = set(four).difference(set(one))
        real_d.remove(real_b)
        real_d = real_d.pop()
        # 9-4-a gives g
        real_g = set(nine).difference(set(four))
        real_g.remove(real_a)
        real_g = real_g.pop()
        # 8-9 gives e
        real_e = set(eight).difference(set(nine)).pop()
        # find 6 from letters
        abdeg = set([real_a, real_b, real_d, real_e, real_g])
        for item in a:
            if len(item) == 6:
                if all([ch in item for ch in abdeg]):
                    six = item
        # 6-letters gives f
        real_f = set(six).difference(abdeg).pop()
        # 1-f gives c
        real_c = set(one)
        real_c.remove(real_f)
        real_c = real_c.pop()
        # 0,2,5 from rest
        szero = real_a + real_b + real_c + real_e + real_f + real_g
        stwo = real_a + real_c + real_d + real_e + real_g
        sfive = real_a + real_b + real_d + real_f + real_g
        # print('a', 'b', 'c', 'd', 'e', 'f', 'g')
        # print(real_a, real_b, real_c, real_d, real_e, real_f, real_g)
        # print(one, three, four, six, seven, eight, nine)
        for item in a:
            if len(item) == 6:
                if set(item) == set(szero):
                    zero = item
        for item in a:
            if len(item) == 5:
                if set(item) == set(stwo):
                    two = item
                elif set(item) == set(sfive):
                    five = item
        stuff = [zero, one, two, three, four, five, six, seven, eight, nine]
        mapping = {''.join(sorted(stuff[i])):i for i in range(10)}
        b = [''.join(sorted(x)) for x in b]
        value = 1000*mapping[b[0]] + 100*mapping[b[1]] + 10*mapping[b[2]] + mapping[b[3]]
        total += value

    print(total)
    #print(c)

# 0 1 2 3 4 5 6 7 8 9
# 6 2 5 5 4 5 6 3 7 6
# 5: 2/3/5   6: 0/6/9

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
# 
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg