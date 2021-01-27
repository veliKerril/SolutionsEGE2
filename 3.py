def check(x, r, step):
    if (x > r) or (step > 8):
        return False
    if x == r:
        return True
    a1 = check(x + 1, r, step + 1)
    a2 = check(x + 5, r, step + 1)
    a3 = check(x * 3, r, step + 1)
    return a1 or a2 or a3


res = 0
for i in range(1000, 1025):
    if check(1, i, 0):
        res += 1

print(res)
