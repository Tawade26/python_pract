from os import fork


def check_inp(prompt):
    while True:
        try:
            inpp = input(prompt)
            if int(inpp) > 0:
                return inpp
            else:
                print("Enter a Positive integer")
        except:
            print("Invalid: Enter a integer")


n = int(check_inp("Enter a positive integer: "))

count = 0
target = 1
temp = 0
print("\n")
while True:

    if n % 2 == 0:
        temp = n/2
        count += 1
    else:
        temp = (n * 3) + 1
        count += 1

    print(f"Step {count}: {int(temp)}")
    n = temp
    if temp == target:
        print(f"Total steps to reach 1: {count}")
        break
    else:
        continue

