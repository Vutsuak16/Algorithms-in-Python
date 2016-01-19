__name__ = "vutsuak"

import random


def gap_insertion_sort(alist, start, gap):
    for c in range(start + gap, len(alist), gap):
        d = c
        while d > 0 and alist[d] < alist[d - 1]:
            alist[d], alist[d - 1] = alist[d - 1], alist[d]
            d -= 1


def shell_sort(alist):
    sublist_count = len(alist) // 2
    while sublist_count > 0:
        for startposition in range(sublist_count):
            gap_insertion_sort(alist, startposition, sublist_count)
        sublist_count //= 2
    print alist


def main():
    alist = [random.randrange(1, 100) for i in range(10)]
    print alist
    shell_sort(alist)


if __name__ == "vutsuak":
    main()
