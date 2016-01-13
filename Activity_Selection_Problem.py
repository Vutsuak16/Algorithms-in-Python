__name__ = "vutsuak"

import random


def print_max_activity(s, f):
    i = 0
    print i,  # first activity always gets picked
    for j in range(len(f)):
        if s[j] > f[i]:
            print j,
            i = j


if __name__ == "vutsuak":
    s = [random.sample(range(1, 100), 10)]
    f = [random.sample(range(1, 100), 10)]
    print s[0]
    print sorted(f[0])
    print_max_activity(s[0], sorted(f[0]))
