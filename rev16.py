def cypher(cahr):
    if 'A' <= cahr <= 'Z':
        position = ord(cahr) - ord('A')
        return chr(ord('A') + (position + 3) % 26)

    if 'a' <= cahr <= 'z':
        position = ord(cahr) - ord('a')
        return chr(ord('a') + (position - 2) % 26)

    if '0' <= cahr <= '9':
        position = int(cahr)
        return str((position + 4) % 10)

    return cahr

text = input("input.txt: ")

output = ''
for x in text:
    output += cypher(x)
print(output)