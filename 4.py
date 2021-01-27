F = open('26.txt')
N = int(F.readline())

list = []
for i in range(N):
    list.append(int(F.readline()))

list.sort()

sup = 0.9 * sum(list)
inf = 0.8 * sum(list)

i = 0
while inf <= sup:
    inf += 0.2 * list[i]
    i += 1

i -= 1
count = i

inf -= 0.2 * list[i]
inf -= 0.2 * list[i - 1]

while i < len(list) and inf + 0.2 * list[i] <= sup:
    i += 1

print(count, list[i - 1])

F.close()
