def optimized_bubble_sort(arr):
    """Optimized Bubble Sort with early termination."""
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    arr = [9, 2, 4, 1, 7, 6, 3, 5, 8]
    print("Optimized Bubble Sort:", optimized_bubble_sort(arr))