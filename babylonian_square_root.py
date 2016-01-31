__name__ = "vutsuak"

# r=(R+(N/R))/2

r = 0
N = 7
R = 2
ct = 0
while ct < 10 ** 2:
    r = (R + float(N / R)) / 2.0
    print r
    if r ** 2 == N:
        break
    R = r
    ct += 1
print r
