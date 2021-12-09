with open("03.in") as f:
    readlines = f.readlines()
    nums = [list(x) for x in readlines]
    nums = list(zip(*nums[::-1]))
    gamma = ''
    epsilon = ''
    for bit in nums:
        if max(set(bit), key=bit.count) == '1':
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print(gamma * epsilon)

    bits = len(readlines[0].strip())

    oxy = readlines.copy()
    for i in range(bits):
        bit = list(zip(*oxy))[i]
        if bit.count('1') >= bit.count('0'):
            oxy = [num for num in oxy if num[i] == '1']
        else:
            oxy = [num for num in oxy if num[i] == '0']
        if len(oxy) == 1:
            break

    co2 = readlines.copy()
    for i in range(bits):
        bit = list(zip(*co2))[i]
        if bit.count('0') <= bit.count('1'):
            co2 = [num for num in co2 if num[i] == '0']
        else:
            co2 = [num for num in co2 if num[i] == '1']
        if len(co2) == 1:
            break
    print(int(oxy[0].strip(), 2) * int(co2[0], 2))