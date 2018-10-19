def quickSort(arr: list):
    """
    Sorts an array using quick sort algoritm and returns result array
    """
    from random import randint

    arrLength = len(arr)

    if arrLength <= 1:
        return arr

    else:
        pivot = arr[randint(0,arrLength -1)]
        bigger = []
        less = []
        duplicates = 0

        for item in arr:
            if item > pivot:
                bigger.append(item)
            elif item < pivot:
                less.append(item)
            else:
                duplicates += 1
        
        return quickSort(less) + [pivot] * duplicates + quickSort(bigger)
