n = input("Prod , Transact: ")
n_prod = int(n.split(" ")[0])
n_transact = int(n.split(" ")[1])

prod_list = []
transact_list = []
for x in range(n_prod):
    prod_list.append(input())

for x in range(n_transact):
    transact_list.append(input())

for transact in transact_list:
    for prod in prod_list:
        if transact[1] == prod[0]:
            print("kita")

    # if transact[0] == 'SELL'
    #     if transact[1] in