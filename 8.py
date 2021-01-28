F = open('27-2a.txt')
N = int(F.readline())

list_of_min = []
dMin1 = 10000001
dMin2 = 10000001

nechet_nechet = 0
nechet_chet = 0

for i in range(N):
    a, b, c = map(int, F.readline().split())
    list_abc = [a, b, c]
    list_abc.sort()
    list_of_min.append(list_abc[0])

    if list_abc[1] % 2 > 0 and list_abc[2] % 2 > 0:
        nechet_nechet += 1
    if (list_abc[1] % 2 > 0 and list_abc[2] % 2 > 0) or (list_abc[1] % 2 == 0 and list_abc[2] % 2 == 0):
        if (list_abc[0] + list_abc[1]) % 2 > 0:
            if list_abc[1] - list_abc[0] < dMin1:
                dMin2 = dMin1
                dMin1 = list_abc[1] - list_abc[0]
            elif list_abc[1] - list_abc[0] < dMin2:
                dMin2 = list_abc[1] - list_abc[0]
    elif (list_abc[1] % 2 == 0 and list_abc[2] % 2 > 0) or (list_abc[1] % 2 > 0 and list_abc[2] % 2 == 0):
        nechet_chet += 1
        if (list_abc[0] + list_abc[1]) % 2 > 0:
            if list_abc[1] - list_abc[0] < dMin1:
                dMin2 = dMin1
                dMin1 = list_abc[1] - list_abc[0]
            elif list_abc[1] - list_abc[0] < dMin2:
                dMin2 = list_abc[1] - list_abc[0]
        elif (list_abc[0] + list_abc[2]) % 2 > 0:
            if list_abc[2] - list_abc[0] < dMin1:
                dMin2 = dMin1
                dMin1 = list_abc[2] - list_abc[0]
            elif list_abc[2] - list_abc[0] < dMin2:
                dMin2 = list_abc[2] - list_abc[0]

if (nechet_nechet % 2 == 0 and nechet_chet % 2 == 0) or (nechet_nechet % 2 > 0 and nechet_chet % 2 == 0):
    print(sum(list_of_min))
elif (nechet_nechet % 2 == 0 and nechet_chet % 2 > 0) or (nechet_nechet % 2 > 0 and nechet_chet % 2 > 0):
    print(sum(list_of_min) + dMin1)
elif nechet_chet == 0:
    print(sum(list_of_min) + dMin1 + dMin2)

F = open('27-2b.txt')
N = int(F.readline())

list_of_min = []
dMin1 = 10000001
dMin2 = 10000001

nechet_nechet = 0
nechet_chet = 0

for i in range(N):
    a, b, c = map(int, F.readline().split())
    list_abc = [a, b, c]
    list_abc.sort()
    list_of_min.append(list_abc[0])

    if list_abc[1] % 2 > 0 and list_abc[2] % 2 > 0:
        nechet_nechet += 1
        if (list_abc[0] + list_abc[1]) % 2 > 0:
            if list_abc[1] - list_abc[0] < dMin1:
                dMin2 = dMin1
                dMin1 = list_abc[1] - list_abc[0]
            elif list_abc[1] - list_abc[0] < dMin2:
                dMin2 = list_abc[1] - list_abc[0]
    elif (list_abc[1] % 2 == 0 and list_abc[2] % 2 > 0) or (list_abc[1] % 2 > 0 and list_abc[2] % 2 == 0):
        nechet_chet += 1
        if (list_abc[0] + list_abc[1]) % 2 > 0:
            if list_abc[1] - list_abc[0] < dMin1:
                dMin2 = dMin1
                dMin1 = list_abc[1] - list_abc[0]
            elif list_abc[1] - list_abc[0] < dMin2:
                dMin2 = list_abc[1] - list_abc[0]
        elif (list_abc[0] + list_abc[2]) % 2 > 0:
            if list_abc[2] - list_abc[0] < dMin1:
                dMin2 = dMin1
                dMin1 = list_abc[2] - list_abc[0]
            elif list_abc[2] - list_abc[0] < dMin2:
                dMin2 = list_abc[2] - list_abc[0]

if (nechet_nechet % 2 == 0 and nechet_chet % 2 == 0) or (nechet_nechet % 2 > 0 and nechet_chet % 2 == 0):
    print(sum(list_of_min))
elif (nechet_nechet % 2 == 0 and nechet_chet % 2 > 0) or (nechet_nechet % 2 > 0 and nechet_chet % 2 > 0):
    print(sum(list_of_min) + dMin1)
elif nechet_chet == 0:
    print(sum(list_of_min) + dMin1 + dMin2)

F.close()
