def longestConsecutive(nums) -> int:
    if len(nums) == 0:
        return 0

    seq = set(nums)
    longest = 0

    for num in nums:
        # it is the start of a sequence
        if num-1 not in seq:
            count = 1
            while(count+num in seq):
                count += 1

            longest = max(longest, count)

    return longest