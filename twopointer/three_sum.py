nums = [0,0,0,0]
#nums = [-1,0,1,2,-1,-4]

def threeSum(nums):
    result = []
    nums.sort() # O(n*log(n))

    for i, a in enumerate(nums):
        # this will avoid duplicated solution, not picking up the same value as first
        if i > 0 and a == nums[i-1]:
            continue

        l, r = i+1, len(nums)-1

        while l < r:
            summ = a + nums[l] + nums[r]
            # array sorted
            if summ > 0:
                r -= 1 #decreasing the sum
            elif summ < 0:
                l += 1 #increasing the sum
            else:
                result.append([a, nums[l], nums[r]])
                l += 1 # just need to update 1 pointer another one our code will do
                # check if it is a different value
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return result

print(threeSum(nums))