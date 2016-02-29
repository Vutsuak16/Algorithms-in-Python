__name__ = "vutsuak"

import random
from itertools import permutations


def largest(l):
    if 0 not in l:
        return 0
    else:
        sum = 0
        l.pop(l.index(0))
        for i in l:
            sum += i
        if sum % 3 == 0:
            max = 0
            for i in permutations(l):
                if i > max:
                    max = i
        else:
            return 0
        return max


def main():
    l = [random.randrange(0, 10) for i in range(10)]
    x = largest(l)
    if x == 0:
        print "number cant be formed"
    else:
        print "the max number is " + str(x)


if __name__ == "vutsuak":
    main()
