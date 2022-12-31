
k = 2
array = [4, 5, 6, 2, 1, 9]

our_sum = sum(array[:k])
j = 0
i = k
results  = [our_sum]

while i < len(array):
    print(f"sum = {our_sum} + {array[i]} - {array[j]}")
    print(f"I: {i} / J: {j}")
    our_sum += array[i] - array[j]
    results.append(our_sum)

    i += 1
    j += 1

print("Results: ", results)
print(f"The smaller sum of subarray with size {k} is {min(results)}")
print(f"The bigger sum of subarray with size {k} is {max(results)}")
