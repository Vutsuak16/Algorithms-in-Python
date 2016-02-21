__name__ = "vutsuak"
import random

n = []  # stream of numbers
k = []  # reservoir

# let the length of n be  N=25
N = 25
for i in range(N):
    n.append(random.randrange(1, 101))

# let the length of k be K= 5

K = 5

for i in range(K):
    k.append(n[i])

for i in range(K + 1, N):
    r = random.randrange(0, i + 1)
    if r < K:  # if randomly picked index is less than K
        k[r] = n[i]

print n
print k
