s = ['A', 'A', 'B', 'A', 'B', 'B', 'A']
k = 1


def characterReplacement(s: str, k: int) -> int:
        count = {}
        l, r = 0, 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            while (r - l +1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
                

            res = max(res, (r -l +1))
        
        return res

print(characterReplacement(s, k))

"""
We need to guarantee that or window will not excede K, if that happens
- need to shift the left pointer and decrement the char set counter
- we get the max of count set because we need to change the less frequency char
"""



