number = '123'

for i in range(1001):
    length = str(len(str(i)))

    if length in number:

        if i and all(x in number for x in str(i)):
            print(i)
        else:
            continue

