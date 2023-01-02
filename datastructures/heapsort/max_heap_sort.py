from build_max_heap import build_max_heap
from max_heapify import max_heapify

A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]

def max_heap_sort(A):
    build_max_heap(A)
    for i in range(len(A)-1, 0, -1):
        print(A[1])
        A[1], A[i] = A[i], A[1]
        max_heapify(A, 0)

max_heap_sort(A)
