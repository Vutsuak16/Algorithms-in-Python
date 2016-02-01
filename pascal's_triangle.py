__name__ = "vutsuak"

import numpy as np

n = int(raw_input("enter no"))

a = [0] * (n ** 2)
a = np.array(a, int)
a = a.reshape((n, n))

for line in range(n):
    for i in range(line + 1):
        if i == 0 or i == line:
            a[line][i] = 1
        else:
            a[line][i] = a[line - 1][i] + a[line - 1][i - 1]
        print a[line][i],
    print
