from collections import Counter

def check_int(promtp):
    while True:
        try:
            inpp = input(promtp)
            if inpp.isnumeric():
                return int(inpp)
        except:
            print("Invalid: Enter an integer")

def check_n(prompt, n):
    while True:
        flag = True
        inp = input(prompt)
        in_list = inp.split()
        # print(len(in_list))

        if len(in_list) == n:
            for x in in_list:
                if x.isnumeric():
                    continue
                else:
                    flag = False
            if flag:
                return in_list
            else:
                print("Invalid: String in seq")
        else:
            print(f"Error: Please enter a {n} digit number sequence")



n = check_int("Enter number of integers: ")
seq = check_n("Enter integers: ", n)
total = 0

counts = Counter(seq)

for x, y in counts.items():
    if y == 1:
        total += int(x)

print(total)