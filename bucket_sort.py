__name__ = "vutsuak"
import random


# bucket sort is useful when input is  uniformly distributed over a range

def insertion_sort(arr):
    for i in range(1, len(arr)):
        d = i
        while d > 0 and arr[d] < arr[d - 1]:
            arr[d], arr[d - 1] = arr[d - 1], arr[d]
            d -= 1


def bucket_sort(arr, n):
    bucket = [[] for i in range(n)]  # creating n buckets

    for i in range(n):
        bucket[int(10 * arr[i])].append(arr[i])  # assigning indexes to suitable buckets
    for i in range(n):
        insertion_sort(bucket[i])  # sorting each bucket
    ct = 0
    for i in bucket:  # concatenating buckets into a single bucket(list)
        for j in i:
            arr[ct] = j
            ct += 1
    print arr


def main():
    bucket_sort([random.random() for i in range(8)], 8)  # random element in the range(0,1)


if __name__ == "vutsuak":
    main()
