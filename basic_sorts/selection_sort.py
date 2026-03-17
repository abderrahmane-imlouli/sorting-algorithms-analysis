def selection_sort(arr):
    """Sorts an array using Selection Sort."""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":
    arr = [9, 2, 4, 1, 7]
    print("Selection Sort:", selection_sort(arr))