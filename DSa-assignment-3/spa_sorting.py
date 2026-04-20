import random
import time
import sys

sys.setrecursionlimit(20000)

# -------------------------------
# 1. Insertion Sort
# -------------------------------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# -------------------------------
# 2. Merge Sort
# -------------------------------
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


# -------------------------------
# 3. Quick Sort
# -------------------------------
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# -------------------------------
# Timing Function
# -------------------------------
def measure_time(func, arr, is_quick=False):
    arr_copy = arr.copy()

    start = time.time()

    if is_quick:
        func(arr_copy, 0, len(arr_copy) - 1)
    else:
        result = func(arr_copy)
        if result is not None:
            arr_copy = result

    end = time.time()

    return round((end - start) * 1000, 3)  # ms


# -------------------------------
# Dataset Generator
# -------------------------------
def generate_data(size):
    random.seed(42)

    random_list = [random.randint(1, 100000) for _ in range(size)]
    sorted_list = list(range(size))
    reverse_list = list(range(size, 0, -1))

    return random_list, sorted_list, reverse_list


# -------------------------------
# Main Execution
# -------------------------------
def main():
    sizes = [1000, 5000, 10000]

    print("Correctness Check:")
    test = [5, 2, 9, 1, 5, 6]

    insertion_sort(test)
    print("Insertion:", test)

    print("Merge:", merge_sort([5, 2, 9, 1, 5, 6]))

    arr = [5, 2, 9, 1, 5, 6]
    quick_sort(arr, 0, len(arr) - 1)
    print("Quick:", arr)

    print("\nPerformance Table (Time in ms)\n")

    print("Size | Type | Insertion | Merge | Quick")
    print("-" * 50)

    for size in sizes:
        random_list, sorted_list, reverse_list = generate_data(size)

        datasets = [
            ("Random", random_list),
            ("Sorted", sorted_list),
            ("Reverse", reverse_list)
        ]

        for dtype, data in datasets:
            t1 = measure_time(insertion_sort, data)
            t2 = measure_time(merge_sort, data)
            t3 = measure_time(quick_sort, data, True)

            print(f"{size} | {dtype} | {t1} | {t2} | {t3}")


if __name__ == "__main__":
    main()