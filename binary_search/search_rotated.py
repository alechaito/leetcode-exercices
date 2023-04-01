nums = [1, 3] 
target = 3

def search_rotated(nums: list, target: int) -> int:
    l, r = 0, len(nums) - 1
    result = float("inf")

    while l <= r:
        print(f"l: {l} / r: {r}")
        m = (r+l)//2
        result = min(result, nums[m])

        # left sorted portion
        if nums[l] <= nums[m]:
            if target > nums[m] or target < nums[l]:
                l = m + 1
            else:
                r = m - 1
        # right sorted portion
        else:
            if target < nums[m] or target > nums[r]:
                r = m - 1
            else:
                l = m + 1

    return -1
        

print(search_rotated(nums, target))

"""
1 - check where Middle is, right or left, for this we check the left and right pointer values
2 - After that we check if the target value is between the middle and left/right value
3 - With step 2 we know if we go to left or right
"""

