# T(n) = O(lgn)

A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]

def right(i):
    return 2*i + 2

def left(i):
    return 2*i + 1

def min_heapify(A, i):
    l = left(i)
    r = right(i)
    smallest = None

    if l < len(A) and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, smallest)
    

