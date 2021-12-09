with open("06.in") as f:
    ages = [int(x) for x in f.read().strip().split(',')]
    ages = {age: ages.count(age) for age in ages}

    days = 256
    for i in range(days):
        new_ages = {age-1: ages[age] for age in ages}
        if -1 in new_ages:
            births = new_ages.pop(-1)
            if 6 in new_ages:
                new_ages[6] += births
            else:
                new_ages[6] = births
            if 8 in new_ages:
                new_ages[8] += births
            else:
                new_ages[8] = births
        #print(new_ages)
        ages = new_ages
    print(sum(ages.values()))