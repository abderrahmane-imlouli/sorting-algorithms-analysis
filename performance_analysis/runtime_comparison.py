import random
import time
from basic_sorts.selection_sort import selection_sort
from basic_sorts.bubble_sort import bubble_sort
from basic_sorts.insertion_sort import insertion_sort
import matplotlib.pyplot as plt

def generate_array(size):
    return [random.randint(0, 10000) for _ in range(size)]

def measure_runtime(sort_func, arr):
    start = time.time()
    sort_func(arr.copy())
    return time.time() - start

sizes = [100, 500, 1000]
selection_times, bubble_times, insertion_times = [], [], []

for size in sizes:
    arr = generate_array(size)
    selection_times.append(measure_runtime(selection_sort, arr))
    bubble_times.append(measure_runtime(bubble_sort, arr))
    insertion_times.append(measure_runtime(insertion_sort, arr))

# Plot results
plt.plot(sizes, selection_times, marker='o', label='Selection Sort')
plt.plot(sizes, bubble_times, marker='o', label='Bubble Sort')
plt.plot(sizes, insertion_times, marker='o', label='Insertion Sort')
plt.xlabel('Array Size')
plt.ylabel('Runtime (s)')
plt.title('Sorting Algorithms Runtime Comparison')
plt.legend()
plt.grid(True)
plt.show()