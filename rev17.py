def encypt(lett, count):

    if 'A' <= lett <= 'Z':
        position = ord(lett) - ord('A')
        return chr(ord('A') + (position + count) % 26)
    if 'a' <= lett <= 'z':
        position = ord(lett) - ord('a')
        return chr(ord('a') + (position - count) % 26)
    if '0' <= lett <= '9':
        position = int(lett)
        return str((position + count) % 10)

    return lett

def decypt(lett, count):

    if 'A' <= lett <= 'Z':
        position = ord(lett) - ord('A')
        return chr(ord('A') + (position - count) % 26)
    if 'a' <= lett <= 'z':
        position = ord(lett) - ord('a')
        return chr(ord('a') + (position + count) % 26)
    if '0' <= lett <= '9':
        position = int(lett)
        return str((position - count) % 10)

    return lett




while True:
    metho = input("Method: ").lower()

    with open('input.txt', 'r') as file:
        text = file.read()
    output = ''

    if metho == 'encrypt' or metho == 'e':
        count = 1
        for x in text:
            temp = encypt(x, count)
            if temp == x:
                output += temp
                continue
            else:
                output += temp
                count += 1
        print("Emcrypted!")

        with open('output.txt', 'w') as file:
            file.write(output)
        break

    elif metho == 'decrypt' or metho == 'd':
        count = 1
        for x in text:
            temp = decypt(x, count)
            if temp == x:
                output += temp
                continue
            else:
                output += temp
                count += 1
        print("Decypted!")

        with open('output.txt', 'w') as file:
            file.write(output)
        break

    else:
        print("Invalid input")

