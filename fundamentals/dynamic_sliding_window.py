x = 7
array = [1, 2, 3, 4, 5, 6]

start = 0
end = 0
sum_subarray = 0
min_lenght = 99999

while end < len(array):
    sum_subarray += array[end]
    end += 1
    print("Expanding...")
    print(f"Start: {start} / End: {end} / Sum: {sum_subarray}")

    while sum_subarray >= x and start < end:
        print("Contracting...")
        sum_subarray -= array[start]
        start += 1
        print(f"Start: {start} / End: {end} / Sum: {sum_subarray}")
        
        min_lenght = min(min_lenght, end-start+1)


print(f"The min lenght is: {min_lenght}")