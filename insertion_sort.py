__name__ = "vutsuak"


def insertion_sort(arr):
    for i in range(1, len(arr)):
        d = i
        while d > 0 and arr[d] < arr[d - 1]:
            arr[d], arr[d - 1] = arr[d - 1], arr[d]
            d -= 1
    print arr
