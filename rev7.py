def check_inp(prompt):
    while True:
        try:
            inp = input(prompt).strip().lower()
            cleaned = ''.join(x for x in inp if x.isalpha())
            return cleaned
        except:
            print("Invalid: Please enter a one whole string")

inputsss = check_inp("Enter string: ")
in_list = list(x for x in inputsss)

odd = [in_list[x] for x in range(len(in_list)) if x%2 == 0]
even = [in_list[x] for x in range(len(in_list)) if x%2 > 0]

# print("Odd: ", odd)
# print("Even: ", even)

odd_count = 1
even_count = 1
for x in range(len(odd) - 1):
    if odd[x] == odd[x+1]:
        odd_count += 1
for x in range(len(even) - 1):
    if even[x] == even[x+1]:
        even_count += 1

# print(odd_count)
# print(even_count)
print(min(odd_count, even_count) * 2)


# gjsngngTgls
# g s g g g s = 3
#  j n n T l = 2
#
# ABBAABABBBAB
# A B A A B A  = 2
#  B A B B B B = 4
# 2
