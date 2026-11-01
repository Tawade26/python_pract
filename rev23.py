n = input("Station, Roads, Closed Roads: ")
n_station = int(n.split(" ")[0])
n_road = int(n.split(" ")[1])
n_closed = int(n.split(" ")[2])

road_list = []
for x in range(n_road):
    road_list.append(int(input("Road A, Road B, Time: ").split(' ')))

closed_list = []
for x in range(n_closed):
    closed_list.append(int(input("Road A, Road B: ").split(' ')))

n = input("Start, End: ")
start = int(n.split(" ")[0])
end = int(n.split(" ")[1])


current_a = 0
time = 0
for i in road_list:
    if i[0] == start:
        time += i[2]
        current_a = i[1]

