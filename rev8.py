def check_inp(prompt):
    while True:
        try:
            inp = int(input(prompt))
            return inp
        except:
            print("Invalid: Enter a integer")



start = check_inp("Start: ")
end = check_inp("End: ")

count = 0
for x in range(start, end+1):
    if str(5) in str(x):
        continue
    else:
        count += 1

print(count)