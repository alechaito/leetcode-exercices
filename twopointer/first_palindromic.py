words = ["abc","car","ada","racecar","cool"]

def find_first_palindromic_in_array(words: list) -> str:
    for word in words:
        palindromic = True
        for i in range((len(word)+1)//2):
            if word[i] != word[~i]:
                palindromic = False
                break
        
        # we found just return because its the first found
        if palindromic:
            return word
    # if not found anything just return empty string
    return ""

# trick: use operator "~"

# Time complexity: O(n)
# Memory complexity: O(1)