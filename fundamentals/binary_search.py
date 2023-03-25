array = [0, 1, 2, 3, 5, 6, 7]
target = 7

def binary_search(array: list, target: int) -> int:

    l, r = 0, len(array) - 1
    while l <= r:
        m = (r+l)//2

        if array[m] < target:
            l = m + 1
        elif array[m] > target:
            r = m - 1
        else:
            return array[m]

print(binary_search(array, target))    



