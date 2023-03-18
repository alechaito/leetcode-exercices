height = [1,8,6,2,5,4,8,3,7]

def maxArea(height: list) -> int:
    left, right = 0, len(height)-1
    max_area = 0

    while left < right:
        area = (right - left) * min(height[right], height[left])
        max_area = max(area, max_area)

        if height[right] > height[left]:
            left += 1
        else:
            right -= 1

    return max_area

print(maxArea(height))

"""
Trick: try the bruteforce solution first to get some clue

we want to maximize the area so lets shift the smaller height found,
if the right height is higher than left we shift left,
but if the right and left size have the same size doesn't matter what pointer we shift
so lets asume that we will shift the right so we can use a else instead of elif+else
to comtemple two cases:
1 - right is smaller than left (shift right)
2 - right and left same size (shift right)
"""