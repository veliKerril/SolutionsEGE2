sup = int(23175821.0 ** (1./4))
inf = int(12034679.0 ** (1./4))
numbers = list(range(2, sup + 1))
for number in numbers:
    if number != 0:
        for candidate in range(2 * number, sup+1, number):
            numbers[candidate-2] = 0    

for number in numbers:
    if number != 0 and number ** 4 > 12034679:
        print(number ** 4, number ** 3)
