
k = 2 # window size
array = [4, 5, 6, 2, 1, 9] # input array

sum_result = sum(array[:k])
results  = []

i = k
j = 0

#put our first sum in results array
results.append(sum_result)

while i < len(array):
    print(f"sum = {sum_result} + {array[i]} - {array[j]}")
    print(f"Indexes => I: {i} / J: {j}")
    sum_result += array[i] - array[j]
    results.append(sum_result)

    i += 1
    j += 1

print(f"Array of results: {results}")
print(f"The smaller sum of subarray with size {k} is {min(results)}")
print(f"The bigger sum of subarray with size {k} is {max(results)}")
