s = "dvdf"

def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    l = 0
    result = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        
        charSet.add(s[r])
        result = max(result, r - l +1)
    
    return result

"""
Remove always from the left to keep our window with unique chars
"""