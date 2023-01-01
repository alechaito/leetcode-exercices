# TODO: use pytest to assert input values

input = "LVIII"
input = "MCMXCIV"
input = "D"

romans = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500, 
    "M": 1000
}

def roman_to_integer(s: str) -> int:
    i = 0
    roman_sum = 0

    for i in range(len(s)):
        if i + 1 < len(s) and romans[s[i]] < romans[s[i+1]]:
            roman_sum -=  romans[s[i]]
        else:
            roman_sum += romans[s[i]]


print("Result: ", roman_to_integer(s))