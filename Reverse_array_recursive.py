__name__ = "vutsuak"

import random


def print_array(arr):
    for i in arr:
        print str(i) + " ",
    print


def reverse(arr, start, end):
    if start < end:
        arr[start], arr[end] = arr[end], arr[start]
        reverse(arr, start + 1, end - 1)


def main():
    arr = random.sample(range(1, 101), 15)
    print_array(arr)
    start = 0
    end = len(arr) - 1
    reverse(arr, start, end)
    print_array(arr)


if __name__ == 'vutsuak':
    main()
