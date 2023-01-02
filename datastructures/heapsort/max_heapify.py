# T(n) = O(lgn)

A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]

def right(i):
    return 2*i + 2

def left(i):
    return 2*i + 1

def max_heapify(A, i):
    l = left(i)
    r = right(i)
    largest = None

    if l < len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    
    if r < len(A) and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)
    

