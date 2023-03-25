s = "{[]}"

def isValid(s: str) -> bool:
    map = {
        ")": "(", 
        "]": "[", 
        "}": "{"
    }
    stack = []

    for c in s:
        #append open brackets to stack
        if c not in map:
            stack.append(c)
            continue
        # if the last char in stack is differente from the closing in the map is wrong order
        if not stack or stack[-1] != map[c]:
            return False
        stack.pop()

    return not stack

print(isValid(s))