def poss_expre(n, target):
    # n_list = n.split() # 1, 2, 3
    # print(n_list)
    current = n[0] #1+2, 1-2, 1*2

    for x in n[1:]: #loop for every other digit
        temp_list = []

        for y in current: # loop for every current

            for z in '+-*': # loop for every operators
                temp_list.append(y+z+x) # 1+2+3, 1+2-3, 1+2*3, 1-2+3, 1-2-3, 1-2*3, 1*2+3, 1*2-3, 1*2*3

        current = temp_list

    result = []
    for x in current:
        if eval(x) == target:
            result.append(x)
        else:
            continue

    return result


n = input('stringnumber: ')
target = int(input('target: '))

result = poss_expre(n, target)

for x in result:
    print(x)