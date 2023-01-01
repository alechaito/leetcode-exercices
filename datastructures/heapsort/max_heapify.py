# T(n) = O(lgn)

A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]

def right(i):
    return 2*i + 1

def left(i):
    return 2*i

def max_heapify(A, i):
    l = left(i)
    r = right(i)
    largest = None
    tmp_A = None

    if l <= len(A) and A[l-1] > A[i-1]:
        largest = l
    else:
        largest = i
    
    if r <= len(A) and A[r-1] > A[largest-1]:
        largest = r
    
    if largest != i:
        tmp_A = A[i-1]
        A[i-1] = A[largest-1]
        A[largest-1] = tmp_A
        max_heapify(A, largest)
    
    return A

print("Before heapify: ", A)

A = max_heapify(A, 2)

print("After heapify: ", A)
