def bubble_sort(arr):
    """Sorts an array using Bubble Sort (optimized)."""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    arr = [9, 2, 4, 1, 7]
    print("Bubble Sort:", bubble_sort(arr))