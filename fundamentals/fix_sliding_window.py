
k = 3 # window size
array = [1, 2, 3, 4, 5, 6] # input array

subarray_sum = sum(array[:k])
results  = [subarray_sum]

i = 1

while i <= len(array)-k:
    print(f"sum = {subarray_sum} + {array[k+i-1]} - {array[i-1]}")
    subarray_sum += array[k+i-1] - array[i-1]
    results.append(subarray_sum)
    i += 1

print(f"Array of results: {results}")
print(f"The smaller sum of subarray with size {k} is {min(results)}")
print(f"The bigger sum of subarray with size {k} is {max(results)}")
