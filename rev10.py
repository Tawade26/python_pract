def armstrong(n, digit):
    n_list = list(map(int, str(n)))
    sum = 0
    for x in n_list:
        sum += x ** digit

    if int(n) == sum:
        return True
    else:
        return False




choice = input("Mode: ")

if choice == '1':
    n = input("Enter a number: ")

    digit = len(n)

    if armstrong(n ,digit):
        print("True")
    else:
        print("False")

else:
    start = int(input("Enter Start of Range: "))
    end = int(input("Enter End of Range: "))+1

    arms = []
    for i in range(start, end):
        digit = len(str(i))
        if armstrong(i, digit):
            arms.append(i)
        else:
            continue

    if len(arms) >= 0:
        print(arms)
    else:
        print("was")
