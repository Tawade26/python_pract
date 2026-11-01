from collections import deque

n = input("Student , Operation: ")
n_stud = int(n.split(" ")[0])
n_ope = int(n.split(" ")[1])

stud_list = []
ope_list = []
stud_list = input().split(' ')
queue = deque(stud_list)

for x in range(n_ope):
    ope_list.append(input())


for x in ope_list:
    if x[0] == 'R':
        for i in range(int(x[2])):
            temp = queue[0]
            queue.popleft()
            queue.append(temp)
            # print(queue)
    if x[0] == 'L':
        for i in range(int(x[2])):
            temp = queue[n_stud - 1]
            queue.pop()
            queue.appendleft(temp)
            # print(queue)
    if x[0] == 'F':
        # print("comapre: " , x[2])

        for y in range(len(queue)):
            # print(queue[y])

            if x[2:4] == queue[y]:
                print("Position: ", y+1 )

print('Final: ', queue)
# print(queue)





# queue = deque([0, 1, 2, 3])
#
# #R
# # temp = queue[0]
# # queue.popleft()
# # queue.append(temp)
# # print(queue)
#
# #L
# temp = queue[3]
# queue.pop()
# queue.appendleft(temp)
# print(queue)