__name__ = "vutsuak"

import random


def print_array(arr):
    for i in arr:
        print str(i) + " ",
    print


def reverse(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def main():
    arr = random.sample(range(1, 101), 15)
    print_array(arr)
    reverse(arr)
    print_array(arr)


if __name__ == 'vutsuak':
    main()
