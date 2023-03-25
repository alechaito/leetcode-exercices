array = [4,5,6,7,0,1,2]

def find_min(array: list) -> int:
    l, r = 0, len(array) - 1
    result = float("inf")

    while l <= r:
        m = (r+l)//2
        result = min(result, array[m])

        if array[m] > array[r]: #right portion must contain the min value
            l = m + 1
        else: #left portion must contain the min value
            r = m - 1
    
    return result
        

print(find_min(array))



