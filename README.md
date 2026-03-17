# Sorting Algorithms in Python

This repository contains classical and enhanced sorting algorithms implemented in Python.  
It demonstrates algorithm design, optimization techniques, and performance analysis.

## Algorithms

- **Basic**: Selection Sort, Bubble Sort, Insertion Sort
- **Enhanced**: Optimized Bubble Sort, Enhanced Merge Sort (Hybrid)
- **Performance Analysis**: Counts comparisons and swaps for insights

## Features

- Clean and professional Python implementations
- Runtime measurement and visualizations
- Analysis of algorithm efficiency
- Highlights enhanced versions for optimization

## Usage Example

```python
from enhanced_sorts.enhanced_merge_sort import enhanced_merge_sort

arr = [12, 11, 13, 5, 6, 7]
enhanced_merge_sort(arr)
print(arr)