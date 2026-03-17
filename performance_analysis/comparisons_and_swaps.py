import random
from basic_sorts.selection_sort import selection_sort
from basic_sorts.bubble_sort import bubble_sort
from basic_sorts.insertion_sort import insertion_sort

def selection_sort_comp_swap(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    return comparisons, swaps

def bubble_sort_comp_swap(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return comparisons, swaps

def insertion_sort_comp_swap(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j+1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break
        arr[j+1] = key
    return comparisons, swaps

if __name__ == "__main__":
    arr = [random.randint(0,100) for _ in range(10)]
    print("Selection Sort:", selection_sort_comp_swap(arr.copy()))
    print("Bubble Sort:", bubble_sort_comp_swap(arr.copy()))
    print("Insertion Sort:", insertion_sort_comp_swap(arr.copy()))