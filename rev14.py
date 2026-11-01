def check_string(promt):
    valid = 'ABCDEFG'
    while True:
        try:
            inp = input(promt).upper().strip()
            if inp and all(x in valid for x in inp):
                return inp

            print("Invalid input")

        except:
            print("Invalid")


# inp = input("Input: ")
inp = check_string("Input: ")

# zar_digi = 'ABCDEFG'
zar_gigi = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6 }

zar_conver = []
for x in range(len(inp)):
    for key, value in zar_gigi.items():
        if inp[x] == key:
            zar_conver.append(value)
        else:
            continue

zar = ''.join(str(x) for x in zar_conver)
print(zar)

zar_decimla = int(zar, 7)
print('Deciaml: ', zar_decimla)
print(f'Binary: {zar_decimla:b}')
print(f'Ocatal: {zar_decimla:o}')
print(f'Hexa: {zar_decimla:x}')

