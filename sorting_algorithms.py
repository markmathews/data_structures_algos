import time


def insertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break
    return arr


def selectionSort(arr):
    for i in range(len(arr)):
        min_pos = i
        min_val = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[j] < min_val:
                min_pos = j
                min_val = arr[j]
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
    return arr


def bubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def _merge(arr1, arr2):
    if len(arr1) == 0 or len(arr2) == 0:
        return arr1 + arr2
    merged = []
    i, j = 0, 0
    for _ in range(len(arr1) + len(arr2)):
        if i != len(arr1) and (j == len(arr2) or arr1[i] <= arr2[j]):
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    return merged


def mergeSort(arr):
    if len(arr) < 2:
        return arr
    mid = int(len(arr) / 2)
    arr1 = arr[:mid]
    arr2 = arr[mid:]
    return _merge(mergeSort(arr1), mergeSort(arr2))


def quickSort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    border_pos = 1
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            arr[border_pos], arr[i] = arr[i], arr[border_pos]
            border_pos += 1
    arr[border_pos - 1], arr[0] = arr[0], arr[border_pos - 1]
    return quickSort(arr[:border_pos - 1]) + [arr[border_pos - 1]] + \
        quickSort(arr[border_pos:])


if __name__ == "__main__":
    a = [0, 2, 32, 11, 2, 12, 3, 5, 7, 43,
         7, 2, 1, 0, 0, 1, 45, -1, -10] * 100

    sorting_algs = (insertionSort, selectionSort, bubbleSort,
                    mergeSort, quickSort)

    # Check that all functions sort
    sorted_arr = sorted(a)
    for alg in sorting_algs:
        assert alg(a) == sorted_arr

    # Find sorting times
    t = [0] * len(sorting_algs)
    for index, alg in enumerate(sorting_algs):
        t0 = time.time()
        alg(a)
        t[index] = time.time() - t0

    # Show sorting times
    for alg, t in zip(sorting_algs, t):
        print('{}: {}'.format(alg, t))
