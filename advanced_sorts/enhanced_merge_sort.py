INSERTION_SORT_THRESHOLD = 10

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_enhanced(arr, aux, left, mid, right):
    i = left
    j = mid + 1
    k = left

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            aux[k] = arr[i]
            i += 1
        else:
            aux[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        aux[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        aux[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right+1):
        arr[i] = aux[i]

def enhanced_merge_sort(arr, aux=None, left=0, right=None):
    if right is None:
        right = len(arr)-1
        aux = arr[:]
    if right - left + 1 <= INSERTION_SORT_THRESHOLD:
        insertion_sort(arr, left, right)
        return arr

    if left < right:
        mid = (left + right) // 2
        enhanced_merge_sort(arr, aux, left, mid)
        enhanced_merge_sort(arr, aux, mid+1, right)
        merge_enhanced(arr, aux, left, mid, right)
    return arr

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7, 20, 15, 4, 9, 3]
    print("Enhanced Merge Sort:", enhanced_merge_sort(arr))