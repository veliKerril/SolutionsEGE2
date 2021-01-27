F = open('27-1a.txt')
N = int(F.readline())

list_of_min = []
dMin = 0

for i in range(N):
    a, b = map(int, F.readline().split())
    cur_min = min(a, b)
    cur_max = max(a, b)
    list_of_min.append(cur_min)
    if (cur_max - cur_min) % 8 > 0:
        dMin = cur_max - cur_min

if sum(list_of_min) % 8 != 2:
    print(sum(list_of_min))
else:
    print(sum(list_of_min) + dMin)

F = open('27-1b.txt')
N = int(F.readline())

list_of_min = []
dMin = 0

for i in range(N):
    a, b = map(int, F.readline().split())
    cur_min = min(a, b)
    cur_max = max(a, b)
    list_of_min.append(cur_min)
    if (cur_max - cur_min) % 8 > 0:
        dMin = cur_max - cur_min

if sum(list_of_min) % 8 != 2:
    print(sum(list_of_min))
else:
    print(sum(list_of_min) + dMin)

F.close()
