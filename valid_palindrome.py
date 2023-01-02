# https://leetcode.com/problems/valid-palindrome/description/

s = "A man, a plan, a canal: Panama"
l, r = 0, len(s) - 1

def check(s):
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        
        while l < r and not s[r].isalnum():
            r -= 1

        print(f"{s[l].lower()} != {s[r].lower()}")
        
        if s[l].lower() != s[r].lower():
            return False
        
        l += 1
        r -= 1
    
    return False

check(s)

# trick: increment points when you not find a alpha