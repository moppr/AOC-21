with open("01.in") as f:
    nums = [int(x) for x in f.read().split()]
    c = 0
    for i in range(len(nums)):
        if i > 0 and nums[i] > nums[i-1]:
            c += 1
    print(c)

    c = 0
    for i in range(len(nums)-2):
        if i > 0:
            prev_win = sum(nums[i-1:i+2])
            curr_win = sum(nums[i:i+3])
            if curr_win > prev_win:
                c += 1
    print(c)
