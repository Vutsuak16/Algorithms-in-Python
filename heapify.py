__author__ = 'vutsuak'


def heapify(a, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    heaplength = len(a)

    if left <= heaplength - 1 and a[left] > a[largest]:
        largest = left
    if right <= heaplength - 1 and a[right] > a[largest]:
        largest = right

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, largest)
