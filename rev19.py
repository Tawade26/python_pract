# def deposit(amount):
#     # amount = transact.split(' ')
#     # print(amount)
#     return amount

def withdraw(initial_b, amount):
    # amount = transact.split(' ')
    # print(amount)
    if int(amount) > initial_b:
        print("Insuficeint Balance")
        return 0
    else:
        return int(amount)

initial_b = int(input("Initial Balance: "))
n_transact = input("Nimber of transaction: ")


transact_record = []
for x in range(int(n_transact)):
    transact = input() # D 500
    transact_record.append(transact)
    print(transact_record)

success = 0
reject = 0
for x in transact_record:
    amount = x.split(' ')
    if amount[0] == 'D':
        print("D true")
        initial_b += int(amount[1])
        success += 1

    elif amount[0] == 'W':
        print('W true')
        temp = withdraw(initial_b, amount[1])
        if temp > 0:
            initial_b -= temp
            success += 1
        else:
            reject += 1
            continue


print(initial_b)
print(success)
print(reject)