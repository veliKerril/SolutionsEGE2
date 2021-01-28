def check(num, fin, step):
    if (num > fin) or (step > 8):
        return False
    if num == fin:
        return True
    a1 = check(num + 1, fin, step + 1)
    a2 = check(num + 5, fin, step + 1)
    a3 = check(num * 3, fin, step + 1)
    return a1 or a2 or a3


res = 0
for i in range(1000, 1025):
    if check(1, i, 0):
        res += 1

print(res)
