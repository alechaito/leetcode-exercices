string = "ADOBECODEBANC" 
substr = "ABC"

def minWindow(string: str, substr: str) -> str:
    if substr == "":
        return ""
    
    countT = {}
    window = {}

    for char in substr:
        countT[char] = 1 + countT.get(char, 0)
    
    have, need = 0, len(countT)
    l = 0
    res, resLen = [-1, -1], float("infinity")
    
    for r in range(len(string)):
        char = string[r]
        window[char] = 1 + window.get(char, 0)

        # just update have if reach the exact number that we need
        # such as W[char] == C[char]
        if char in countT and window[char] == countT[char]:
            have += 1
        
        # we will minimize and update our result just when have=need
        while have == need:
            if (r - l + 1) < resLen:
                resLen = r - l + 1
                res = [l, r]
            
            # lets remove left char try to minimize our window
            window[string[l]] -= 1
            if string[l] in countT and window[string[l]] < countT[string[l]]:
                have -= 1
            
            l += 1
        
    l, r = res
    
    return string[l : r + 1] if resLen != float("infinity") else ""


print(minWindow(string, substr))


"""
1 - Just update have and need when reach the exact number in the two hashes
2 - We will add every char independent if its in countT or not
3 - When we reach our goal that its have=need we need to try to update the result
3 - And we need to try to minimize our window until have=need
"""
