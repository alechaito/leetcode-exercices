from max_heapify import max_heapify, left, right

A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
n = int((len(A)//2)-1)

def build_max_heap(A):
    for k in range(n, -1, -1):
        max_heapify(A, k)
    
    return A